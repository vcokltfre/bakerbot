from templatebot import Bot
from os import environ as env
from dotenv import load_dotenv

load_dotenv(".env")

bot = Bot(name="BakerBot", command_prefix="b!")
bot.load_initial_cogs()

bot.run(env.get("TOKEN", None))
