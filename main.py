from aiogram import Dispatcher, Bot, executor
from aiogram.types import Message
from aiogram.utils.markdown import hbold, hitalic
from _Downloader import GetLink
from dotenv import load_dotenv
import os

load_dotenv()

b = Bot(token=os.getenv('TOKEN'), parse_mode='Html')
dp = Dispatcher(b)

@dp.message_handler(commands=['start', 'download', 'about', 'help'])
async def StartProgram(message: Message):
    if message.text == '/start':
        await message.answer(f'''Бот успешно запушен.
{hbold('Отправьте ссылку чтобы скачать контент.')}''')
    if message.text == '/download':
        await message.answer(f'''{hbold('Отправьте ссылку чтобы скачать контент.')}''')
    if message.text == '/about':
        await message.answer(f'''Бот создан для личного пользования,
для скачивания видео и фото с инстаграм.''')
    if message.text == '/help':
        await message.answer(f'''По каким либо вопросам: @shavkatov3.''')

@dp.message_handler(content_types='text')
async def GetUrl(message: Message):
    ChatId = message.chat.id
    if 'https://www.instagram.com' in message.text:
        await b.send_message(ChatId, f'🔎')
        Media = GetLink(message.text)
        try:
            try:
                for i in Media:
                    await b.send_video(ChatId, i)
            except:

                for i in Media:
                    await b.send_photo(ChatId, i)
        except:
            await b.send_message(ChatId, f'💀')
            await b.send_message(ChatId, f'''Повторите попытку.
В случае повторной ошибки обратитесь за помощью к @shavkatov3''')
    else:
        await b.send_message(ChatId, 'Пожалуйста введите корректную ссылку')

if __name__ == '__main__':
    executor.start_polling(dp)


