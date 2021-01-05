import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from data import config
from utils.db_api.postgresql import Database

bot = Bot(token=str(config.BOT_TOKEN), parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
loop = asyncio.get_event_loop()
db = Database(loop)
