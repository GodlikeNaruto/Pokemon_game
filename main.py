import telebot 
from config import token

from logic import Pokemon

bot = telebot.TeleBot(token) 

@bot.message_handler(commands=['go'])
def go(message):
    if message.from_user.username not in Pokemon.pokemons.keys():
        pokemon = Pokemon(message.from_user.username)
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_img())
        stats = pokemon.get_stats()
        mess = f'hp: {stats[0]}\nattack: {stats[1]}\nspeed: {stats[2]}'
        bot.send_message(message.chat.id, mess)
    else:
        bot.reply_to(message, "Ты уже создал себе покемона")

@bot.message_handler(commands=['hp'])
def get_hp(message):
    func = message.text().split()
    if len(func) == 2:
        bot.send_message(Pokemon.hp(float(func[1])))
    else:
        bot.send_message(Pokemon.hp())

@bot.message_handler(commands=['attack'])
def get_hp(message):
    func = message.text().split()
    if len(func) == 2:
        bot.send_message(Pokemon.attack(float(func[1])))
    else:
        bot.send_message(Pokemon.attack())

@bot.message_handler(commands=['speed'])
def get_hp(message):
    func = message.text().split()
    if len(func) == 2:
        bot.send_message(Pokemon.speed(float(func[1])))
    else:
        bot.send_message(Pokemon.speed())

bot.infinity_polling(none_stop=True)

