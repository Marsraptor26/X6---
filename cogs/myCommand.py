import discord
from discord import app_commands
from discord.ext import commands

import os
import sys

sys.path.append( 'D:\Marsraptor\Script\XYZ - Wizard of Mars' )

import env

E = env

GUILD_ID = E.GUILD_ID


class your_command(commands.Cog):
  
  def __init__(self, bot : commands.Bot):
    self.bot = bot
  
  @app_commands.command(name = "first_command", description = "First command")
  async def your_command(self, interaction : discord.Interaction, name : str):

    await interaction.response.send_message(f"Your name {name}!")

async def setup(bot : commands.Bot):
    await bot.add_cog(your_command(bot), guilds = [discord.Object(id = E.GUILD_ID)])