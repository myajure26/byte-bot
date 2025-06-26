from discord.ext import commands

class MessageEvents(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener()  # Decorador para eventos
  async def on_message(self, message):
    
    if message.author.bot:
      return
    
    print(f'Message from {message.author}: {message.content} in #{message.channel}')

async def setup(bot):
  await bot.add_cog(MessageEvents(bot))