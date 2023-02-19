import random
from discord import app_commands, Interaction, Object
from discord.ext import commands
from discord.ui import Button, View
from discord import ButtonStyle


class button(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name="버튼")
    async def button(self, interaction: Interaction) -> None:
        button1 = Button(label="하이", emoji="🦶", style = ButtonStyle.primary)
        button2 = Button(label="로우", style = ButtonStyle.primary)
    
        async def button1_callback(interaction: Interaction):
            dice_result = str(random.choice(['하이','로우']))
            await interaction.response.send_message(f'{dice_result}')

        async def button2_callback(interaction: Interaction):
            dice_result = str(random.choice(['하이','로우']))
            await interaction.response.send_message(f'{dice_result}')    

        button1.callback = button1_callback
        button2.callback = button2_callback

        view = View()
        view.add_item(button1)
        view.add_item(button2)
        await interaction.response.send_message("버튼을 선택해주세요.", view=view)

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        button(bot),
        guilds=[Object(id=1072809889329594430)]
    )