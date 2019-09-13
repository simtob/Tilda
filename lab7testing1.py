# Uppgift 1

import operator
import csv


class Pokemon():
    def __init__(self, number, name, type1, type2, total, hp, attack, defense, sp_attack, sp_defense, sp_speed,
                 generation, legendary):
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
        return str(
            self.number + " " + self.name + " " + self.type1 + " " + self.type2 + " " + self.total + " " + self.hp + " " + self.attack + " " + self.defense + " " + self.sp_attack + " " + self.sp_defense + " " + self.sp_speed + " " + self.generation + " " + self.legendary)

    def __lt__(self, other):
        return self.attack < other.attack, self.hp < other.hp

    def __gt__(self, other):
        return self.defense > other.defense

    def __eq__(self, other):
        return self.generation == other.generation


pokemon_list = []


# Uppgift 1

class DictHash:
    def __init__(self):
        self.dictionary = {}

    def store(self, key, data):
        self.dictionary[key] = data

    def search(self, key):
        try:
            print("Data: ", self.dictionary[key])
        except KeyError:
            print("Wrong key")


q = DictHash()


def main():
    with open("pokemons.csv", encoding="utf8") as file:
        for line in file:
            attributes = line.strip().split(",")
            # attributes = item[2], item[3], item[4], item[5], item[6], item[7], item[8], item[9], item[10], item[11], item[12]
            pokemon = Pokemon(attributes[0], attributes[1], attributes[2], attributes[3], attributes[4], attributes[5],
                              attributes[6], attributes[7], attributes[8], attributes[9], attributes[10],
                              attributes[11], attributes[12])
            q.store(attributes[1], pokemon)


main()

x = q.search("Bulbasaur")



class Node:

    def __init__(self, key = "", data = None):
        self.key = key
        self.data = data

class Hashtable(object):

    def __init__(self, size):
        self.size = size
        self.luckor = [None] * self.size
        self.data = [None] * self.size

    def store(self, key, data):
        hashvarde = self.hashfunction(key,len(self.luckor))

        if self.luckor[hashvarde] == None:
            self.luckor[hashvarde] = key
            self.data[hashvarde] = data

        else:

            if self.luckor[hashvarde] == key:
                self.data[hashvarde] = data

            else:

                nestalucka = self.goraom_hachen(hashvarde,len(self.luckor))

                while self.luckor[nestalucka] != None and self.luckor[nestalucka] != key:
                    nestalucka = self.goraom_hachen(nestalucka,len(self.luckor))

                if self.luckor[nestalucka] == None:
                    self.luckor[nestalucka] = key
                    self.data[nestalucka] = data

                else:
                    self.data[nestalucka] = data

    def hashfunction(self,key,size):
        #själva hash funktionen
        return int(key)% size

    def goraom_hachen(self, gamlahashen, size):
        return (gamlahashen+1)%size

    def search(self, key):

        startluckan = self.hashfunction(key,len(self.luckor))
        data = None
        stoppa = False
        hittad = False
        positionen = startluckan

        while self.luckor[positionen] != None and not hittad and not stoppa:

            if self.luckor[positionen] == key:
                hittad = True
                data = self.data[positionen]

            else:
                positionen = self.goraom_hachen(positionen,len(self.luckor))
                if positionen == startluckan:

                    stoppa = True
        print(data)

        return data


    def print(self):
        print(str(self.data))







def main():
    with open("pokemons.csv", encoding="utf8") as file:
        for line in file:
            attributes = line.strip().split(",")
            # attributes = item[2], item[3], item[4], item[5], item[6], item[7], item[8], item[9], item[10], item[11], item[12]
            pokemon = Pokemon(attributes[0], attributes[1], attributes[2], attributes[3], attributes[4], attributes[5],
                              attributes[6], attributes[7], attributes[8], attributes[9], attributes[10],
                              attributes[11], attributes[12])
            q.store(attributes[1], pokemon)


main()

v = Hashtable(10)

v.store("1", "Bulbasaur")
v.store("2", "Bulbasaur2")
v.store("0", "Bulbasaur3")

v.print()

v.search("2")
