import discord
from discord.ext import commands
import random
from apis.giphy_api import GiphyAPI  # Importa la clase GiphyAPI

class Gif(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.giphy_api = GiphyAPI()  # Instancia la clase GiphyAPI
  
  @commands.hybrid_command(name='gif', description="Muestra un gif de la búsqueda")
  async def gif(self, ctx, gif_name: str = None):
    if gif_name:
      content = self.giphy_api.search_gif(gif_name)
      title = f"Gif random sobre {gif_name}"
    else:
      content = self.giphy_api.trending_gif()
      title = "Gif random trending"

    gif_data = content.get("data", [])
    if not gif_data:
      await ctx.send("No se encontraron gifs.")
      return

    gif = random.choice(gif_data)
    embed = discord.Embed(title=title, color=discord.Color.purple())
    embed.set_image(url=gif["images"]["original"]["url"])
    await ctx.send(embed=embed)

  @commands.hybrid_command(name='esposo_de', description="Gif del bicho")
  async def esposo_de(self, ctx, user: commands.MemberConverter = None):

    content = self.giphy_api.esposo_de()

    gif_data = content["data"]
    
    if not gif_data:
      await ctx.send("No se encontraron gifs.")
      return

    gif = random.choice(gif_data)

    if not user:
      embed = discord.Embed(title=f"Esposo de la nada", color=discord.Color.purple(),)
    else:
      embed = discord.Embed(title=f"Esposo de {user.display_name}", color=discord.Color.purple(),)
    embed.set_image(url=gif["images"]["original"]["url"])
    await ctx.send(embed=embed)
  
  @commands.hybrid_command(name='esposo_de_mari', description="Muestra un gif del esposo de Mari")
  async def esposo_de_mari(self, ctx):

    names = ["Kakashi Hatake", "Sebastian Michaelis", "Jinshi", "Itachi Uchiha", "Sesshomaru"]
    gif_name = random.choice(names)

    content = self.giphy_api.search_gif(gif_name)
    title = f"Gif random sobre {gif_name}"

    gif_data = content.get("data", [])
    if not gif_data:
      await ctx.send("No se encontraron gifs.")
      return

    gif = random.choice(gif_data)
    embed = discord.Embed(title=title, color=discord.Color.purple())
    embed.set_image(url=gif["images"]["original"]["url"])
    await ctx.send(embed=embed)

# Función para que el bot cargue este módulo
async def setup(bot):
  await bot.add_cog(Gif(bot))