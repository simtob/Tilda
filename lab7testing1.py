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

KAPACITET = 500

class Node: #Själva verket en node datastruktor, som en linkedlist node
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.nesta = None

class Hashtable:
    #initisiserar en hash tabell
    def __init__(self, size):
        self.size = size
        self.kapasitet = KAPACITET
        self.luckor = [None] * self.kapasitet

    def store(self, key, data):
        #steg 1 blir att öka storleken
        self.size += 1
        #steg 2 blir att beräkna index av key
        index = self.hashfunction(key)

        node = self.luckor[index] #går till noden

        #om luckan är tom så skapas ny node och retunerar
        if node is None:
            self.luckor[index] = Node(key, data)
            return

    #annars gå igenomen länkade listan på given index, sedan lägg till ny node på slutet av listan
        tidigare = node
        while node is not None:
            tidigare = node
            node = node.nesta

        tidigare.nesta = Node(key, data)

    def search(self, key):
        #steg 1 blir att beräkna hashen
        index = self.hashfunction(key)

        node = self.luckor[index] #går till första noden i listan

        while node is not None and node.key != key: #korsar den länkade listan på noden
            node = node.nesta

        if node is None:
            raise KeyError
        else:
            return node.data

    def hashfunction(self, key):
        hashsumman = 0
        for i, c in enumerate(key): #för varje karaktär i key
            hashsumman += (i+len(key)) ** ord(c) #lägger till index ? längden av key upphöjt till nuvarnde char Node
            hashsumman = hashsumman % self.size
        return hashsumman









