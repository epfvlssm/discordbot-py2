from discord import app_commands
from discord.ext import commands
from discord import Interaction
from discord import Object

class Check(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        Check(bot),
        guilds=[Object(id=1072809889329594430)]
    )