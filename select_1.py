from discord import Interaction, SelectOption, app_commands, Object
from discord.ext import commands
from discord.ui import View, Select


class select(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name="메뉴")
    async def select(self, interaction: Interaction) -> None:
        selects = Select(options=[
            SelectOption(
                label="1번",
                description="1번"
            ),
            SelectOption(
                label="2번",
                description="2번"
            )
        ])

        async def select_callback(interaction: interaction) -> None:
            await interaction.response.send_message(f"{selects.values}를 선택하셨습니다.")

        selects.callback = select_callback
        view = View()
        view.add_item(selects)
        await interaction.response.send_message("메뉴를 선택해주세요.", view=view)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        select(bot),
        guilds=[Object(id=1072809889329594430)]
    )