import logging
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
load_dotenv()
import os
from Battinlar import menyu,ovqat,taom,salat,desert,ichimlik,asarte,psql
bot_T = os.getenv("Bot_token")
logging.basicConfig(level=logging.INFO)
bot = Bot(token=bot_T)
db = Dispatcher(bot)
@db.message_handler(commands=["start","help"])

async def BOT(message: types.Message):
    users = message.from_user.username
    await message.reply(f"salom {users}",reply_markup=menyu)
#########################################################################
@db.message_handler(lambda message: message.text == "🇺🇿 O'zbekcha 🇺🇿")
async def MENYU(message: types.Message):
    await message.answer( "MENYULAR : ",reply_markup= ovqat)

@db.message_handler(lambda message: message.text == "⬅️ Chiqish ⬅️")
async def CHIQISH(message: types.Message):
    await message.answer( "MENYULAR : ",reply_markup= menyu)
##########################################################################
# @db.message_handler(lambda message: message.text == "🍨 Taomlar 🍨")
# async def TAOM(message: types.Message):
#     await message.answer( "Taomlar : ",reply_markup= taom)

@db.message_handler(lambda message: message.text == "🍨 Taomlar 🍨")
async def TAOM(message: types.Message):
    await message.answer( "Taomlar : ",reply_markup= taom)


@db.message_handler(lambda message: message.text == "🥦 Salatlar 🥦")
async def SALAT(message: types.Message):
    await message.answer("Salatlar : ", reply_markup=salat)

@db.message_handler(lambda message: message.text == "🥂 Ichimlikla 🥂r")
async def ICHIMLIK(message: types.Message):
    await message.answer("Ichimliklar"  , reply_markup=ichimlik)

@db.message_handler(lambda message: message.text == "🍱 Asartelar 🍱")
async def ASARTE(message: types.Message):
    await message.answer("Asarte : ", reply_markup=asarte)

@db.message_handler(lambda message: message.text == " 🧁 Desert 🧁 ")
async def DESERT(message: types.Message):
    await message.answer("Desert : ", reply_markup=desert)

@db.message_handler(lambda message: message.text == " Orqaga ")
async def ORQAGA (message: types.Message):
    await message.answer(" Orqaga : ", reply_markup=menyu)

@db.message_handler(lambda message: message.text == " PSQL ")
async def PSQL (message: types.Message):
    await message.answer(" PSQL : ", reply_markup=psql)

@db.message_handler(lambda message: message.text  not in ["🍨 Taomlar 🍨","🥦 Salatlar 🥦","🥂 Ichimlikla 🥂","🍱 Asartelar 🍱","🧁 Desert 🧁","PSQL"])
async def PSQL (message: types.Message):
    await message.answer(" Bunday Bo'lim mavjud emas ", reply_markup=psql)


if __name__ == "__main__":
    executor.start_polling(db,skip_updates=True)