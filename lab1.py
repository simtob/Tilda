import operator
import csv

class Pokemon():
    def __init__(self, number, name, type1, type2, total, hp, attack, defense, sp_attack, sp_defense, sp_speed, generation, legendary):
        self.number = number
        self.name = name
        self.type1 = type1
        self.type2 = type2
        self.total = total
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.sp_attack = sp_attack
        self.sp_defense = sp_defense
        self.sp_speed = sp_speed
        self.generation = generation
        self.legendary = legendary

    def __str__(self):
        return (self.number, self.name, self.type1, self.type2, self.total, self.hp, self.attack, self.defense, self.sp_attack, self.sp_defense, self.sp_speed,
                                          self.generation, self.legendary)
    def __lt__(self, other):
        return self.attack < other.attack, self.hp < other.hp

    def __gt__(self, other):
        return self.defense > other.defense

    def __eq__(self, other):
        return self.generation == other.generation




pokemon_list = []

def test_attack():
    if pokemon_list[1] < pokemon_list[2]:
        print("First pokemon less attack than second")
    else:
        print("Error")

def testa_HP():
    if pokemon_list[1] < pokemon_list[2]:
        print ("First pokemon has less HP than second pokemon")
    else:
        print("Error igen")

def test_defense():
    if pokemon_list[2] > pokemon_list[3]:
        print("Second pokemon more defense than third")
    else:
        print("Error")

def test_generation():
    if pokemon_list[17] == pokemon_list[18]:
        print("#17 pokemon has same generation as #18")
    else:
        print("Error")

def search_pokemon():
    pokemon_searcher = input("Name of Pokemon: ")
    for pokemon in pokemon_list:
        if pokemon.name == pokemon_searcher:
            print(pokemon.name + " exists!")
            return
    print("finns inte med")



def main():
   with open("pokemons.csv", encoding = "utf8") as file:
       file.readline() #för att skippa header
       for line in file:
           attributes = line.strip().split(",")
           pokemon = Pokemon(attributes[0], attributes[1], attributes[2], attributes[3], attributes[4], attributes[5], attributes[6], attributes[7], attributes[8],attributes[9], attributes[10], attributes[11], attributes[12])
           pokemon_list.append(pokemon) #Lägger till i slutet

main()
test_attack()
testa_HP()
test_defense()
test_generation()
search_pokemon()
