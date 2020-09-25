from main import dp
from aiogram import types, filters


@dp.message_handler(filters.CommandStart())
async def start_message(message: types.Message):
    await message.answer(text='Hi send me photo')