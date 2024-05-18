from random import randint
import requests

class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer   

        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()

        Pokemon.pokemons[pokemon_trainer] = self
        info = self.get_stats()
        self.hp = info[0]
        self.attack = info[1]
        self.speed = info[2]

    def hp(self, hp=-1):
        if hp > 0:
            self.hp = hp
        if hp == -1:
            return self.hp
        
    def attack(self, attack=-1):
        if attack > 0:
            self.attack = attack
        if attack == -1:
            return self.attack
        
    def speed(self, speed=-1):
        if speed > 0:
            self.speed = speed
        if speed == -1:
            return self.speed

    # Метод для получения картинки покемона через API
    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['sprites']['other']['showdown']['front_default'])
        else:
            return "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png"
    
    def get_stats(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            hp = data['stats'][0]['base_stat']
            attack = data['stats'][1]['base_stat']
            speed = data['stats'][5]['base_stat']
            return (hp, attack, speed)
        else:
            return (35, 55, 90)
        
    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"


    # Метод класса для получения информации
    def info(self):
        return f"Имя твоего покеомона: {self.name}"

    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img
