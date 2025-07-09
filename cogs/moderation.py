import discord
from discord.ext import commands
import asyncio

class Moderation(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.hybrid_command(name='purge', description="Borra mensajes en este canal")
  @commands.has_permissions(manage_messages=True)
  @commands.guild_only()
  async def purge(self, ctx, quantity: int = 10):
    """Borra mensajes (máx. 100)
    
    Parámetros:
    quantity: Número de mensajes a borrar (1-100)"""
    
    if quantity <= 0 or quantity > 100:
      await ctx.send("❌ La cantidad debe estar entre 1 y 100.", ephemeral=True)
      return

    # Manejo diferente para comandos de prefijo vs slash
    if ctx.interaction:
      # Para slash commands, responder primero
      await ctx.interaction.response.defer(thinking=True, ephemeral=True)
    else:
      # Para comandos de prefijo, borrar el mensaje
      await ctx.message.delete()

    try:
      deleted = await ctx.channel.purge(limit=quantity)
      
      # Respuesta diferente según el tipo de comando
      if ctx.interaction:
        await ctx.interaction.followup.send(
          f"🗑️ Borrados {len(deleted)} mensajes.",
          ephemeral=True
        )
      else:
        msg = await ctx.send(f"🗑️ Borrados {len(deleted)} mensajes.", delete_after=5)
        await asyncio.sleep(5)
        await msg.delete()
        
    except discord.Forbidden:
      error_msg = "❌ No tengo permisos para borrar mensajes."
      if ctx.interaction:
        await ctx.interaction.followup.send(error_msg, ephemeral=True)
      else:
        await ctx.send(error_msg, delete_after=10)
    except Exception as e:
      error_msg = f"❌ Error: {str(e)}"
      if ctx.interaction:
        await ctx.interaction.followup.send(error_msg, ephemeral=True)
      else:
        await ctx.send(error_msg, delete_after=10)

async def setup(bot):
  await bot.add_cog(Moderation(bot))