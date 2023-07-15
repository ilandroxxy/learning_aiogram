from aiogram import Bot, Dispatcher, executor, types

import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('TOKEN_API')
admin = int(os.getenv('ADMIN_ID'))

bot = Bot(token)
dp = Dispatcher(bot)


async def on_startup(_):
    print('Бот успешно запущен!')


@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await message.answer(f"Отвечаю: {message.text}")


@dp.message_handler()
async def echo(message: types.Message):
    if message.chat.id == admin:
        await message.answer(f"Добрый день, Илья Алексеевич!")
    else:
        await message.answer(f"Добрый день, {message.from_user.first_name}!")


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,
                           on_startup=on_startup,
                           skip_updates=True)
