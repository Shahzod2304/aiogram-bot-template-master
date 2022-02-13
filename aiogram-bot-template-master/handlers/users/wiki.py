# import logging
# import wikipedia
# from loader import dp
#
# from aiogram import Bot, Dispatcher, executor, types
#
#
#
# # Configure logging
# logging.basicConfig(level=logging.INFO)
#
# @dp.message_handler(commands=['start', 'help'])
# async def send_welcome(message: types.Message):
#     """
#     This handler will be called when user sends `/start` or `/help` command
#     """
#     await message.reply("Wikipeida Botiga Xush Kelibsiz!")
#
# @dp.message_handler()
# async def sendWiki(message: types.Message):
#     try:
#         respond = wikipedia.summary(message.text)
#         await message.answer(respond)
#     except:
#         await message.answer("Bu mavzuga oid maqola topilmadi")
#
#
