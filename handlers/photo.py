from main import dp
from aiogram import types
from lightshot import upload_photo
from aiogram.types.mixins import Downloadable


@dp.message_handler(content_types=types.ContentTypes.PHOTO)
async def photo_message(message: types.Message):
    await types.ChatActions.typing()
    photo = await message.photo[-1].download()
    data = await upload_photo(photo=open(photo.name, 'rb'))
    if data['error'] == 0:
        await message.reply(text=data['data']['data'])
    elif data['error'] == 1:
        await message.reply(text='Error server')