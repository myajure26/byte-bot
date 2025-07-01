import discord
from discord.ext import commands
from apis.nekosia_api import NekosAPI  # Importa la clase NekosAPI

class Anime(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.api = NekosAPI()  # Instancia la clase NekosAPI

  @commands.hybrid_command(name='get_random_catgirl', description="Obtiene una imagen de catgirl aleatoria")
  async def get_random_catgirl(self, ctx):
    content = self.api.get_random_catgirl()
    embed = discord.Embed(title="Catgirl aleatoria", color=discord.Color.purple(),)
    embed.set_image(url=content["image"]["original"]["url"])  
    await ctx.send(embed=embed) 

# Función para que el bot cargue este módulo
async def setup(bot):
  await bot.add_cog(Anime(bot))