import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

class MyBot(commands.Bot):
  def __init__(self):
    # Configuración inicial
    self.TOKEN = os.getenv('TOKEN')
    self.PREFIX = os.getenv('PREFIX', '!')
    
    # Intents
    intents = discord.Intents.all()
    intents.message_content = True
    
    super().__init__(
        command_prefix=self.PREFIX,
        intents=intents
    )

  async def setup_hook(self):
    """Carga los Cogs (comandos y eventos) al iniciar."""
    await self.load_extensions()
    await self.tree.sync()  # Sincroniza los comandos con Discord

  async def load_extensions(self):
    """Carga dinámicamente todos los archivos de 'cogs/' y 'events/'."""
    for folder in ["cogs", "events"]:
      for filename in os.listdir(f"./{folder}"):
        if filename.endswith(".py") and not filename.startswith("__"):
          try:
            await self.load_extension(f"{folder}.{filename[:-3]}")
            print(f"✅ {folder}/{filename} cargado correctamente")
          except Exception as e:
            print(f"❌ Error al cargar {folder}/{filename}: {e}")

  async def on_ready(self):
    print(f"Bot conectado como {self.user}")

  def run(self):
    """Inicia el bot con el token."""
    super().run(self.TOKEN)

if __name__ == "__main__":
  bot = MyBot()
  bot.run()