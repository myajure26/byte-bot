import discord
from discord.ext import commands
from apis.nekosia_api import NekosiaAPI  # Importa la clase NekosAPI

class Anime(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.nekosiaApi = NekosiaAPI()  # Instancia la clase NekosiaAPI

  """ 
    NEKOSIA COMANDOS
  
  """

  @commands.hybrid_command(name='get_random_catgirl', description="Obtiene una imagen de catgirl aleatoria")
  async def get_random_catgirl(self, ctx):
    content = self.nekosiaApi.get_random_catgirl()
    embed = discord.Embed(title="Catgirl aleatoria", color=discord.Color.purple(),)
    embed.set_image(url=content["image"]["original"]["url"])  
    await ctx.send(embed=embed) 

  @commands.hybrid_command(name='anime_girl', description="Obtiene una imagen de un personaje de anime femenino aleatorio")
  async def anime_girl(self, ctx, category: str = "catgirl"):
    content = self.nekosiaApi.anime_girl(category=category)
    if not content:
      await ctx.send("❌ No se pudo obtener la imagen del personaje de anime.")
      return
    embed = discord.Embed(title="Personaje de anime femenino aleatorio", color=discord.Color.purple(),)
    embed.set_image(url=content["image"]["original"]["url"])  
    await ctx.send(embed=embed)

# Función para que el bot cargue este módulo
async def setup(bot):
  await bot.add_cog(Anime(bot))