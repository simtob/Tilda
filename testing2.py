class Pokemon():
    def __init__(self, name, type1, type2, total, hp, attack, defense, sp, sp_attack, sp_defense, sp_speed, generation,
                 legendary):
        self.name = name
        self.type1 = type1
        self.type2 = type2
        self.total = total
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.sp = sp
        self.sp_attack= sp_attack
        self.sp_defense = sp_defense
        self.sp_speed = sp_speed
        self.generation = generation
        self.legendary = legendary

    def __str__(self):
        return "{0}, {1}, {2}, {3}, {4},{5}, {6}, {7}, {8}, {9}, {10}, {11}".format(self.name, self.type1, self.type2, self.total, self.hp, self.attack, self.defense, self.sp, self.sp_attack, self.sp_defense, self.sp_speed,
                                          self.generation, self.legendary)



def new_object():
    pokemon_object = Pokemon()
    print(pokemon_object)



def read_list():
    with open("pokemons.csv") as listor:
        list = [line.split() for line in listor]  # create a list of lists
        for i, x in enumerate(list):  # print the list items
            print("line{0} = {1}".format(i, x))

read_list()