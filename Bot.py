import logging
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
load_dotenv()
import os
from Battinlar import menyu,ovqat,psql
from inlayen_keyvord import in_key_1,in_key_2,in_key_3,in_key_4,in_key_5

bot_T = os.getenv("Bot_token")
logging.basicConfig(level=logging.INFO)
bot = Bot(token=bot_T)
db = Dispatcher(bot)
@db.message_handler(commands=["start"])

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


@db.message_handler(lambda message: message.text == "🍨 Taomlar 🍨")
async def TAOM(message: types.Message):
    await message.answer( "Taomlar : ",reply_markup= in_key_1)


@db.message_handler(lambda message: message.text == "🥦 Salatlar 🥦")
async def SALAT(message: types.Message):
    await message.answer("Salatlar : ", reply_markup=in_key_4)

@db.message_handler(lambda message: message.text == "🥂 Ichimliklar 🥂")
async def ICHIMLIK(message: types.Message):
    await message.answer("Ichimliklar", reply_markup=in_key_2)

@db.message_handler(lambda message: message.text == "🍱 Asartelar 🍱")
async def ASARTE(message: types.Message):
    await message.answer("Asarte : ", reply_markup=in_key_5)

@db.message_handler(lambda message: message.text == "🧁 Desert 🧁")
async def DESERT(message: types.Message):
    await message.answer("Desert : ", reply_markup=in_key_3)

    @db.message_handler(lambda message: message.text == " Orqaga ")
    async def ORQAGA(message: types.Message):
        await message.answer(" Orqaga : ", reply_markup=menyu)

@db.message_handler(lambda message: message.text == "Afitsan isimlari")
async def PSQL (message: types.Message):
    await message.answer(" Asitsan isimlari : ", reply_markup=psql)
#
# @db.message_handler(lambda message: message.text  not in ["🍨 Taomlar 🍨","🥦 Salatlar 🥦",
# "🥂 Ichimlikla 🥂","🍱 Asartelar 🍱","🧁 Desert 🧁","Asitsan isimlari"])
# async def PSQL_1 (message: types.Message):
#     await message.answer(" Bunday Bo'lim mavjud emas ", reply_markup=menyu)
# RASIM YUKLASH
@db.message_handler(commands=['image'])
async def send_image(message: types.Message):
    #    photo_url = 'https://www.google.com/imgres?imgurl=https%3A%2F%2Fmedia.licdn.com%2Fdms%2Fimage%2FD5603AQG7m-Wq_-cvSQ%2Fprofile-displayphoto-shrink_800_800%2F0%2F1689072274652%3Fe%3D2147483647%26v%3Dbeta%26t%3D2nlYI39EmN6t7IU6CNN_QLD_WtifM4v5_Tksye5Tllg&tbnid=mst2mXliUaDFkM&vet=12ahUKEwiswqStqPiEAxVPNhAIHWX6C60QMyhUegUIARD-AQ..i&imgrefurl=https%3A%2F%2Fwww.linkedin.com%2Fin%2Fpaytin-joy-mercado-b-a-0a9864187&docid=LVgBphbWsm6JRM&w=800&h=800&q=paytin%20&ved=2ahUKEwiswqStqPiEAxVPNhAIHWX6C60QMyhUegUIARD-AQ.jpg'
    #photo_url = '.jpg'
    photo_url = 'https://www.google.com/imgres?imgurl=https%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fcommons%2Fthumb%2F0%2F0a%2FPython.svg%2F1200px-Python.svg.png&tbnid=XmmuGvoln--UuM&vet=12ahUKEwj9ksf0qfiEAxWGAxAIHWzuAy8QMygCegQIARBM..i&imgrefurl=https%3A%2F%2Fen.wikiversity.org%2Fwiki%2FPython&docid=k36Oe0TGOvdiNM&w=1200&h=1200&q=python&ved=2ahUKEwj9ksf0qfiEAxWGAxAIHWzuAy8QMygCegQIARBM.jpg'
    caption = 'Sizning rasmingiz'
    await bot.send_photo(message.chat.id, photo=photo_url, caption=caption)

#ADMIN
@db.message_handler(commands=['salom'])
async def admin_command(message: types.Message):
    users = message.from_user.first_name
    if message.from_user.id in [5742041673]:
        await message.reply(f"Salom {users}")
    else:
        await message.reply("Bunday buyruq turi mavjud emas")


if __name__ == "__main__":
    executor.start_polling(db,skip_updates=True)