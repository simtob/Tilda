class Pokemon():
    def __init__(self, pokemons):
        clean_line = pokemons.strip()
        seperated = clean_line.split(",")
        self.name = seperated[0]
        self.type1 = seperated[1]
        self.type2 = seperated[2]
        self.total = seperated[3]
        self.hp = seperated[4]
        self.attack = seperated[5]
        self.defense = seperated[6]
        self.sp = seperated[7]
        self.sp_attack = seperated[8]
        self.sp_defense = seperated[9]
        self.sp_speed = seperated[10]
        self.generation = seperated[11]
        self.legendary = seperated[12]

    def __str__(self):
        return "{0}, {1}, {2}, {3}, {4},{5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}".format(self.name, self.type1, self.type2, self.total, self.hp, self.attack, self.defense, self.sp, self.sp_attack, self.sp_defense, self.sp_speed,
                                          self.generation, self.legendary)
    def __lt__(self, other):
        return self.attack > other.attack

pokemon_list = []


def main():
   with open("pokemons.csv", encoding = "utf8") as file:
       for line in file:
           pokemon_list.append(line)
           pokemon = Pokemon(line)
           print(pokemon)

main()
