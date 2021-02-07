from templatebot import Bot
from discord import AllowedMentions
from os import environ as env
from dotenv import load_dotenv

from cogs.help import BakerHelp
from utils.database import DatabaseInterface


load_dotenv(".env")

bot = Bot(
    name="BakerBot",
    command_prefix="b!",
    logging_url=env.get("WEBHOOK", None),
    allowed_mentions=AllowedMentions(
        everyone=False, roles=False, users=False, replied_user=True
    ),
    help_command=BakerHelp(),
)

bot.VERSION = "1.0.0"
bot.db = DatabaseInterface()

bot.load_initial_cogs(
    "cogs.profile",
    "cogs.dev",
    "cogs.recipe",
    "cogs.utility",
    "cogs.help"
)

bot.run(env.get("TOKEN", None))
