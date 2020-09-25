import config
import logging
from aiogram import Bot, Dispatcher, executor


logging.basicConfig(level=logging.INFO)
bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher(bot=bot)


if __name__ == '__main__':
    from handlers import dp
    executor.start_polling(dp, skip_updates=True)