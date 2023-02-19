import random
import os
from discord.ext import commands
from discord import app_commands, Interaction, Object
from discord.ext.commands import MissingRequiredArgument


# game 커맨드가 바로 호출할 수 있도록 클래스 밖에 선언

async def make_dir(directory_name):
    try:
        if not os.path.exists(directory_name):
            os.makedirs(directory_name)
    except OSError:
        print('Error: makedirs()')


async def add_result(directory_name, user_name, result):
    file_path = directory_name + '/' + user_name + '.txt'
    if os.path.exists(file_path):
        with open(file_path, 'a', encoding='UTF-8') as f:
            f.write(result)
    else:
        with open(file_path, 'w', encoding='UTF-8') as f:
            f.write(result)


class Game(commands.Cog):

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name="주사위")
    async def dice(self, interaction: Interaction) -> None:
        randnum = random.randint(1, 6)
        await interaction.response.send_message(f'주사위 결과는 {randnum} 입니다.')

    @app_commands.command(name="광물")
    async def mining(self, interaction: Interaction) -> None:
        minerals = ['다이아몬드', '루비', '에메랄드', '자수정', '철', '석탄']
        weights = [1, 3, 6, 15, 25, 50]
        results = random.choices(minerals, weights=weights, k=5)
        await interaction.response.send_message(', '.join(results) + ' 광물들을 획득하였습니다.')

    @app_commands.command(name="가위바위보")
    async def game(self, interaction, user: str) -> None:
        rps_table = ['가위', '바위', '보']
        bot = random.choice(rps_table)
        result = rps_table.index(user) - rps_table.index(bot)
        if result == 0:
            result_text = f'{user} vs {bot} 비김'
            await interaction.response.send_message(f'{user} vs {bot}  비겼습니다.')
        elif result == 1 or result == -2:
            result_text = f'{user} vs {bot} 승리!'
            await interaction.response.send_message(f'{user} vs {bot}  유저가 이겼습니다.')
        else:
            result_text = f'{user} vs {bot} 패배...'
            await interaction.response.send_message(f'{user} vs {bot}  봇이 이겼습니다.')

        directory_name = "game_result"
        await make_dir(directory_name)
        await add_result(directory_name, str(interaction.author), result_text + '\n')

    @game.error  # @<명령어>.error의 형태로 된 데코레이터를 사용한다.
    async def game_error(self, interaction, error):  # 파라미터에 ctx, error를 필수로 한다.
        if isinstance(error, MissingRequiredArgument):  # isinstance로 에러에 따라 시킬 작업을 결정한다.
            await interaction.response.send_message("가위/바위/보 중 낼 것을 입력해주세요.")

    @app_commands.command(name="전적")
    async def game_board(self, interaction: Interaction) -> None:
        user_name = str(interaction.author)
        file_path = "game_result/" + user_name + ".txt"
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="UTF-8") as f:
                result = f.read()
            await interaction.response.send_message(f'{interaction.author}님의 가위바위보 게임 전적입니다.\n==============================\n' + result)
        else:
            await interaction.response.send_message(f'{interaction.author}님의 가위바위보 전적이 존재하지 않습니다.')


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        Game(bot),
        guilds=[Object(id=1072809889329594430)]
    )