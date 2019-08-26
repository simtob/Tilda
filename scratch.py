class Pokemon():
    def __init__(self):
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
        self.sp_speed = speed
        self.generation = generation
        self.legendary = legendary

    def __str__(self):
        return "{0}, {1}, {2}, {3}, {4},{5}, {6}, {7}, {8}, {9}, {10}, {11}".format(self.name, self.type1, self.type2, self.total, self.hp, self.attack, self.defense, self.sp, self.sp_attack, self.sp_defense, self.sp_speed,
                                          self.generation, self.legendary)

    def __lt__(self, other):







    Name,Type 1,Type 2,Total,HP,Attack,Defense,Sp. Atk,Sp. Def,Speed,Generation,Legendary