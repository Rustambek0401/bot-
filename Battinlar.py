from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from PSQ import Data_Basa
menyu = ReplyKeyboardMarkup([
    [KeyboardButton(" 🇺🇿 O'zbekcha 🇺🇿"), KeyboardButton(" 🇷🇺 Ruscha 🇷🇺 ")]
],resize_keyboard=True)

ovqat = ReplyKeyboardMarkup([
    [KeyboardButton("🍨 Taomlar 🍨"), KeyboardButton("🥦 Salatlar 🥦" )],
    [ KeyboardButton(" 🥂 Ichimliklar 🥂 "), KeyboardButton("🍱 Asartelar 🍱")],
    [KeyboardButton("🧁 Desert 🧁"), KeyboardButton("⬅️ Chiqish ⬅️")],
    [KeyboardButton("Afitsan isimlari")]
],resize_keyboard=True)
#
#  taom = ReplyKeyboardMarkup([
#      [KeyboardButton(" Pitsa 🍕 "), KeyboardButton(" Lavash 🌯")],
#      [KeyboardButton("Burger 🍔" ), KeyboardButton(" Klap 🥪" )],
#      [KeyboardButton("Orqaga ")]
# ],resize_keyboard=True)
#
# salat = ReplyKeyboardMarkup([
#     [KeyboardButton(" sezir 🥦"), KeyboardButton(" baxor 🥒")],
#     [KeyboardButton("sviji 🥑" ), KeyboardButton(" alivye 🫒" )],
#     [KeyboardButton("Orqaga ")]
# ],resize_keyboard=True)
#
# ichimlik = ReplyKeyboardMarkup([
#     [KeyboardButton(" Limon choy 🫖"), KeyboardButton(" Cola 🥤")],
#     [KeyboardButton(" Maxito 🧃" ), KeyboardButton(" Pepsi 🧉" )],
#     [KeyboardButton("Orqaga ")]
# ], resize_keyboard=True)
#
# asarte = ReplyKeyboardMarkup([
#     [KeyboardButton(" 2 - kishilik 👫"), KeyboardButton("  3 - kishilik 👨‍👩‍👦")],
#     [KeyboardButton("  5 - kishilik 👩‍👩‍👧‍👦" ), KeyboardButton("  7 - kishilik 👨‍👨‍👦‍👦👨‍👩‍" )],
#     [KeyboardButton("Orqaga ")]
# ],resize_keyboard=True)
#
# desert = ReplyKeyboardMarkup([
#     [KeyboardButton(" Paxlava 🧇  "), KeyboardButton("  Medovi 🥮  ")],
#     [KeyboardButton("  Bolichka 🥠  " ), KeyboardButton("  Tort 🎂" )],
#     [KeyboardButton("Orqaga ")]
# ],resize_keyboard=True)

psql = ReplyKeyboardMarkup(resize_keyboard=True)
quer = f""" SELECT * FROM users;"""
for i in Data_Basa.data_basa(quer,'select'):
    # data = list
    # data = (i[0],i[1])
    psql.add(KeyboardButton(i[1]))
