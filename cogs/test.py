from discord.ext import commands

class Test(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.hybrid_command(name='saludar', description="Te saludo cordialmente")
  async def saludar(self, ctx):
    await ctx.send(f'Hola, {ctx.author.mention}!')
  
  @commands.hybrid_command(name='ping', description="Responde con Pong!")
  async def ping(self, ctx):
    await ctx.send('Pong!')
  
  @commands.hybrid_command(name='saludar_a', description="Saluda a un usuario específico")
  async def saludar_a(self, ctx, usuario: commands.MemberConverter):
    await ctx.send(f'Hola, {usuario.mention}! {ctx.author.mention} te ha saludado.')

# Función para que el bot cargue este módulo
async def setup(bot):
  await bot.add_cog(Test(bot))