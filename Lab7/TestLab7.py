
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

TableCapacity = 500

class Node:
    def __init__(self, key="", data=None):
        self.key = key
        self.data = data
        self.next = None

class Hashtable:
    def __init__(self):
        self.capacity = TableCapacity
        self.size = 0
        self.box = [None] * self.capacity

    def hash(self, key):
        sum = 0
        for indx, c in enumerate(key):
    #idx, c lets us iterate over the index and value
    # of an item in a list by using a basic for loop
    # enumerate makes key instantly iterable,
    # enumerate() returns a tuple containing a count (from start which defaults to 0)
    # and the values obtained from iterating over iterable
            sum += (indx + len(key)) ** ord(c) # The ord() method takes a single parameter c,
                                            # where c is character string of length 1
                                           # and and returns an integer representing the Unicode code point of the character.
            sum = sum % self.capacity
        return sum

    def store(self, key, data):
        self.size += 1
        index = self.hash(key) #hashar key
        node = self.box[index]

        if node is None: #Fall 1, ingen node finns, skapar en nod
            self.box[index] = Node(key, data)
            return

        OldNode = node
        while node is not None: #Fall 2 finns en nod på platsen
            OldNode = node
            node = node.next
        OldNode.next = Node(key, data) #Blir vår nya Nod

    def search(self, key):
        index = self.hash(key) #hashar key
        node = self.box[index]

        while node is not None and node.key != key:
            node = node.next
        if node is None: #nått slutet av listan eller så fanns det ingen nod till att börja med
            return None
        else:
            return node.data #annars node.key = vad vi söker efter och vi får tillbaks data


q = Hashtable()

def main():
   with open("pokemons.csv", encoding = "utf8") as file:
       for line in file:
           attributes = line.strip().split(",")
           #attributes = item[2], item[3], item[4], item[5], item[6], item[7], item[8], item[9], item[10], item[11], item[12]
           pokemon = Pokemon(attributes[0], attributes[1], attributes[2], attributes[3], attributes[4], attributes[5], attributes[6], attributes[7], attributes[8],attributes[9], attributes[10], attributes[11], attributes[12])
           q.store(attributes[1], pokemon)

main()


try:
    print(str(q.search("Bulbasaur")))
    print(str(q.search("Charmander")))
except KeyError:
    print("Error...")
    
