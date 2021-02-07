from templatebot import Bot
from discord import AllowedMentions
from os import environ as env
from dotenv import load_dotenv

load_dotenv(".env")

bot = Bot(
    name="BakerBot",
    command_prefix="b!",
    allowed_mentions=AllowedMentions(
        everyone=False, roles=False, users=False, replied_user=True
    ),
)

bot.VERSION = "1.0.0"

bot.load_initial_cogs(
    "cogs.profile",
    "cogs.dev"
)

bot.run(env.get("TOKEN", None))
