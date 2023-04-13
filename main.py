import asyncio
from config.config import cfg
from core.handlers.mainhandler import register_handlers
from aiogram import Bot, Dispatcher

async def main_telegram():
    bot = Bot(token=cfg.ConfigTelegram())
    dp = Dispatcher(bot=bot)
    register_handlers(dp=dp)
    await dp.start_polling()

if __name__ == '__main__':
    asyncio.run(main_telegram())