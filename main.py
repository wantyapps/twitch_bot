from twitchio.ext import commands
import sys
import os
# import colored
import dotenv

dotenv.load_dotenv()

class Bot(commands.Bot):

    def __init__(self):
        super().__init__(
            token=os.environ["TMI_TOKEN"],
            prefix=os.environ["BOT_PREFIX"],
            initial_channels=[sys.argv[1]]
        )

    async def event_ready(self):
        print(f"Logged in as | {self.nick}")

    async def event_message(self, message):
        if message.echo:
            return

        # print(f"{colored.fg(message.author.color)}{message.author.display_name}{colored.attr('reset')}: {message.content}")
        print(f"{message.author.display_name}: {message.content}")
        with open(f"/home/{os.getlogin()}/Stream/chatLogs/log.txt", "a+") as f:
            f.write(f"{message.author.display_name}: {message.content}\n")

        await self.handle_commands(message)

bot = Bot()
bot.run()
