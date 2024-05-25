import telebot 
from config import token
from random import randint

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

@bot.message_handler(commands=['attack'])
def attack(message):
    if message.reply_to_message:
        pokemon_1 = Pokemon.pokemons[message.from_user.username]
        pokemon_2 = Pokemon.pokemons[message.reply_to_message.from_user.username]
        if pokemon_1.category == 'Assasin':
            skill = pokemon_1.special_skill(pokemon_2)
            if skill:
                bot.send_message(message.chat.id, skill)
        elif pokemon_1.category == 'Fighter':
            skill = pokemon_1.sup_attack(pokemon_2)
            if skill:
                bot.send_message(message.chat.id, skill)
        if pokemon_2.category() == 'Wizard':
            skill = pokemon_2.shield()
            if skill:
                bot.send_message(message.chat.id, skill)
            else:
                result = pokemon_1.attack(pokemon_2)
        elif pokemon_2.category == 'Healer':
            skill = pokemon_2.heal_100()
            if skill:
                bot.send_message(message.chat.id, skill)
        elif pokemon_2.category == 'Tank':
            skill = pokemon_2.dmg_reflect(pokemon_1)
            if skill:
                bot.send_message(message.chat.id, skill)
        result = pokemon_1.attack(pokemon_2)
        bot.send_message(message.chat.id, result)
    else:
        bot.reply_to(message, "Выбери противника (ответь на другое сообщение командой /attack)")

@bot.message_handler(commands=['hp'])
def get_hp(message):
    pokemon = Pokemon.pokemons[message.from_user.username]
    bot.send_message(message.chat.id, pokemon.hp_f())

@bot.message_handler(commands=['attack'])
def get_attack(message):
    pokemon = Pokemon.pokemons[message.from_user.username]
    bot.send_message(message.chat.id, str(pokemon.attack_f()))

@bot.message_handler(commands=['speed'])
def get_speed(message):
    pokemon = Pokemon.pokemons[message.from_user.username]
    bot.send_message(message.chat.id, pokemon.speed_f())

bot.infinity_polling(none_stop=True)

