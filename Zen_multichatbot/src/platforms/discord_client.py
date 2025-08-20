import discord
from discord.ext import commands
from src.utils.logger import setup_logger

logger = setup_logger("DiscordClient")

class DiscordClient(commands.Cog):
    def __init__(self, bot, storage):
        self.bot = bot
        self.storage = storage

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        self.storage.log_message("discord", message.author.id, message.content)
        await message.channel.send(f"Got your message: {message.content}")

def start_discord(config, storage):
    intents = discord.Intents.default()
    intents.messages = True
    bot = commands.Bot(command_prefix="!", intents=intents)
    bot.add_cog(DiscordClient(bot, storage))
    logger.info("Discord client started")
    bot.run(config["token"])
