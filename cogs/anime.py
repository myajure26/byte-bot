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

  @commands.hybrid_command(name='anime_girl', description="Obtiene una imagen de un personaje de anime femenino aleatorio")
  async def anime_girl(self, ctx, category: str = None):
    content = self.api.anime_girl(category=category)
    if not content:
      await ctx.send("❌ No se pudo obtener la imagen del personaje de anime.")
      return
    embed = discord.Embed(title="Personaje de anime femenino aleatorio", color=discord.Color.purple(),)
    embed.set_image(url=content["image"]["original"]["url"])  
    await ctx.send(embed=embed)

  """ 
    LOS COMANDOS DE ABAJO SON DE DIVERSIÓN MIENTRAS SE PRUEBA EL BOT
  
  """

  @commands.hybrid_command(name='mi_esposo_1', description="Obtiene una imagen de mi esposo 1")
  async def mi_esposo_1(self, ctx):
    
    embed = discord.Embed(title="Mi esposo 1", color=discord.Color.purple(),)
    embed.set_image(url="https://s1.zerochan.net/Jinshi.600.4473633.jpg")  
    await ctx.send(embed=embed) 

  @commands.hybrid_command(name='mi_esposo_2', description="Obtiene una imagen de mi esposo 2")
  async def mi_esposo_2(self, ctx):
    
    embed = discord.Embed(title="Mi esposo 2", color=discord.Color.purple(),)
    embed.set_image(url="https://i.pinimg.com/originals/b3/00/5b/b3005b1f9061a06a2df6661203ec6754.jpg")  
    await ctx.send(embed=embed)

  @commands.hybrid_command(name='mi_esposo_3', description="Obtiene una imagen de mi esposo 3")
  async def mi_esposo_3(self, ctx):

    embed = discord.Embed(title="Mi esposo 3", color=discord.Color.purple(),)
    embed.set_image(url="https://i.pinimg.com/736x/95/3f/a4/953fa426cc1697557900f52891d41cf5.jpg")
    await ctx.send(embed=embed)

  @commands.hybrid_command(name='mi_esposo_4', description="Obtiene una imagen de mi esposo 4")
  async def mi_esposo_4(self, ctx):

    embed = discord.Embed(title="Mi esposo 4", color=discord.Color.purple(),)
    embed.set_image(url="https://pm1.aminoapps.com/6348/74b4030c4214adaa9cc21ec3717852840428a769_hq.jpg")
    await ctx.send(embed=embed)

  @commands.hybrid_command(name='mi_esposo_5', description="Obtiene una imagen de mi esposo 5")
  async def mi_esposo_5(self, ctx):

    embed = discord.Embed(title="Mi esposo 5", color=discord.Color.purple(),)
    embed.set_image(url="https://i.pinimg.com/736x/11/81/04/1181047981fe2ee55c3508d48138e86c.jpg")
    await ctx.send(embed=embed)
  
  @commands.hybrid_command(name='mi_esposo', description="Obtiene una imagen de mi esposo")
  async def mi_esposo_5(self, ctx):

    embed = discord.Embed(title="Mi esposo", color=discord.Color.purple(),)
    embed.set_image(url="https://i.pinimg.com/474x/11/cf/f4/11cff4725ed6aed68f75ac7fda7a44da.jpg")
    await ctx.send(embed=embed)

# Función para que el bot cargue este módulo
async def setup(bot):
  await bot.add_cog(Anime(bot))