#Uppgift 1

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
        return str(self.number + " " + self.name + " " + self.type1 + " " + self.type2 + " " + self.total + " " + self.hp + " " + self.attack + " " + self.defense + " " + self.sp_attack + " " + self.sp_defense + " " + self.sp_speed + " " + self.generation + " " + self.legendary)

    def __lt__(self, other):
        return self.attack < other.attack, self.hp < other.hp

    def __gt__(self, other):
        return self.defense > other.defense

    def __eq__(self, other):
        return self.generation == other.generation


pokemon_list = []


# Uppgift 1

class Node:
    def __init__(self, key="", data=None):
        """key: nyckeln som anvands vid hashningen
        data: det objekt som ska hashas in"""
        self.key = key
        self.data = data
        self.next = None


class Hashtable:

    def __init__(self, size):
        """size: hashtabellens storlek"""
        self.size = size
        self.mytabell = [0] * size * 2

    def store(self, key, data):
        """key: nyckeln
           data: objektet som ska lagras
           Stoppar in "data" med nyckeln "key" i tabellen."""

        index = hashfunction(self, key) #key får ett index
        if self.mytabell[index] is 0: #fall nummer ett, när tabellen är tom
            self.mytabell[index] = Node(key, data) #skapar ny nod

        elif self.mytabell[index].next is None: #Fall nummer två
            self.mytabell[index].next = Node(key,data) #lägger till nod, början på länkade listan

        elif self.mytabell[index].next is not None: #Fall tre
            start = self.mytabell[index].next #pekar på vår nod
            while start.next is not None:
                start = start.next
            if start.next is None:
                start.next = Node(key, data)


    def search(self, key):
        """key: nyckeln
           Hamtar det objekt som finns lagrat med nyckeln "key" och returnerar det.
           Om "key" inte finns ska vi få en Exception, KeyError """
        index = hashfunction(self, key)
        if self.mytabell[index] == 0:
            raise KeyError

        elif self.mytabell[index].key == key:
            return self.mytabell[index].data

        elif self.mytabell[index].next is not None:
            start = self.mytabell[index].next
            while start.next is not None:
                if start.key == key:
                    return start.data
                start = start.next
            if start.key == key:
                return start.data
        raise KeyError


def hashfunction(self, key):
    """key: nyckeln
    Beräknar hashfunktionen för key"""
    result = 0
    for c in key:
        result = result * 15 + ord(c)  # The ord() method takes a single parameter c,
        # where c is character string of length 1
        # and and returns an integer representing the Unicode code point of the character.
    return result % self.size*2

"""
class DictHash:
    def __init__(self):
        self.dictionary = {}

    def store(self, nyckel, data):
        self.dictionary[nyckel] = data

    def search(self, nyckel):
        try:
            print("Data: ", self.dictionary[nyckel])
        except KeyError:
            print("Wrong key")
"""
q = Hashtable(10000)

def main():
   with open("pokemons.csv", encoding = "utf8") as file:
       for line in file:
           attributes = line.strip().split(",")
           #attributes = item[2], item[3], item[4], item[5], item[6], item[7], item[8], item[9], item[10], item[11], item[12]
           pokemon = Pokemon(attributes[0], attributes[1], attributes[2], attributes[3], attributes[4], attributes[5], attributes[6], attributes[7], attributes[8],attributes[9], attributes[10], attributes[11], attributes[12])
           q.store(attributes[1], pokemon)

main()



try:
    print("Bulbasaur " + str(q.search("Bulbasaur")))
except KeyError:
    print("Error...")

