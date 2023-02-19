from discord import app_commands
from discord.ext import commands
from discord import Interaction
from discord import Object


class hello(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name="hello")
    async def hello(self, interaction: Interaction) -> None:
        await interaction.response.send_message("hi")


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        hello(bot),
        guilds=[Object(id=1072809889329594430)]
    )