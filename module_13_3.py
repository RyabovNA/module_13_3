from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


# @dp.message_handler(text=['Urban', 'ff']) # Обрабатывает сообщения указанные в text
# async def urban_message(message):
#     print("Urban message")
#     await message.answer("Urban message!") # Отправляет ответ пользователю


@dp.message_handler(commands=['start']) # Обрабатывает сообщения после нажатия кнопки START
async def start_message(message):
    await message.answer("Рады вас видеть в нашем боте помощнике!") # Отправляет ответ пользователю


@dp.message_handler() # Обрабатывает любые сообщения
async def all_message(message):
    await message.answer("Введите команду /start, чтобы начать общение.")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True) # участок кода запускает программу
