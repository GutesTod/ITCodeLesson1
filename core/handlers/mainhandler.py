from aiogram import types
from aiogram import Dispatcher

async def echo(msg: types.Message):
    await msg.answer(msg.text)
    
def register_handlers(dp: Dispatcher):
    dp.register_message_handler(echo)