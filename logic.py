import random
import requests

class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer   

        self.pokemon_number = random.randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()
        info = self.get_stats()
        self.hp = float(info[0])
        self.power = float(info[1])
        self.speed = float(info[2])
        self.effect = False
        self.category = random.choice(["Wizard", "Fighter", "Healer", "Tank", "Assasin"])

        Pokemon.pokemons[pokemon_trainer] = self

    def hp_f(self):
        return self.hp
        
    def power_f(self):
        return self.power
        
    def speed_f(self):
        return self.speed
    
    def sup_attack(self, enemy):
        super_power = random.randint(10,1000)
        self.power += super_power
        result = self.attack(enemy)
        self.power -= super_power
        return result + f"\
    Боец применил супер-атаку силой:{super_power} "

    def shield(self):
        if self.effect:
            self.effect = False
            return "Pokemon were sick so he didn't use his abilities"
        else:
            chance = random.randint(1,5)
            if chance == 1:
                return "Покемон-волшебник применил щит в сражении"
    
    def heal_100(self):
        if self.effect:
            self.effect = False
            return "Pokemon were sick so he didn't use his abilities"
        else:
                
            chance = random.randint(1,100)
            if chance % 20 == 0:
                info = self.get_stats()
                self.hp = float(info[0])
                self.attack = float(info[1]) + random.randint(1, 50)
            return "Enemy heals himself to 100 percent of his hp and increases his dmg"
    
    def dmg_reflect(self, enemy):
        if self.effect:
            self.effect = False
            return "Pokemon were sick so he didn't use his abilities"
        else:
            chance = random.randint(1,100)
            if chance % 3 == 0:
                self.hp -= 0.8 * enemy.attack()
                enemy.hp -= enemy.attack()
            return "Enemy reflects 100 percent damage back to you and takes only 80 percent of damage dealed"
        
    def special_skill(self, enemy):
        if self.effect:
            self.effect = False
            return "Pokemon were sick so he didn't use his abilities"
        else:
            chance = random.randint(1,100)
            if chance % 10 == 0:
                enemy.effect = True
            return "Now enemy is sick so he cannot use his special abilities"

    def attack(self, enemy):
        if self.hp > 0:
            if enemy.hp > self.power:
                enemy.hp -= self.power
                return f"Сражение @{self.pokemon_trainer} с @{enemy.pokemon_trainer}\n Enemy's hp is now {enemy.hp_f()}"
            else:
                enemy.hp = 0
                return f"Победа @{self.pokemon_trainer} над @{enemy.pokemon_trainer}! "
        else:
            return 'What are you doing man? Your Pokemon already dead!'

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
            power = data['stats'][1]['base_stat']
            speed = data['stats'][5]['base_stat']
            return (hp, power, speed)
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
        return f"Имя твоего покеомона: {self.name}\nHis category is {self.category}"

    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img
            
