from linkedQfilenuseLab5 import LinkedQ
from Lab3useLab5 import Bintree

q = LinkedQ()
svenska = Bintree()
gamla = Bintree()

class SolutionFound(Exception):
    pass

class ParentNode:
    def __init__(self, word, parent = None):
        self.word = word
        self.parent = parent

    def writechain(self, barn):
        if barn.parent == None: #om barn inte har en parent. printar vi ut ordet som finns på barn, första fallet
            print(barn.word)
        else:
            self.writechain(barn.parent) #annars skriver vi in barnets förälder i chain
            print(barn.word) #och printar ut nuvarande barnet

def read_file():
    with open("word3.txt", "r", encoding="utf-8") as svenskfil:
        for rad in svenskfil:
            ordet = rad.strip()  # Ett trebokstavsord per rad
            if ordet in svenska:
                gamla.put(ordet)
            else:
                svenska.put(ordet)

def makechildren(start_ordet):
    alphabet = "abcdefghijklmnopqsrtuvwxyzåäö"
    for i in range(len(start_ordet.word)):
        for letter in alphabet:
            barn = start_ordet
            barn = list(barn.word)  # skapar list för att enkelt byta ut bokstaven
            if letter != barn[i]:
                barn[i] = letter #ersätter första förekomsten av barn av [i]
                barn_str = "".join(barn) #joinar listan till en sträng, med avseende på en avskiljare i vårt fall ""
                if barn_str in svenska and barn_str not in gamla:
                    gamla.put(barn_str)
                    nyNod = ParentNode(barn_str)
                    nyNod.parent = start_ordet
                    q.enqueue(nyNod)

def main():
    read_file()
    start_ordet = str(input("ange startord: ")).lower()
    slut_ordet = str(input("ange slutord: ")).lower()
    parent_node = ParentNode(start_ordet)
    q.enqueue(parent_node)  #lägger in vårt sökord som inte har en parent som en nod, i kön

    try:
        while not q.isEmpty() and start_ordet in svenska:
            nod = q.dequeue()
            makechildren(nod)
            if nod.ordet == slut_ordet:
                print("\n" + "Väg existerar, vägen från", start_ordet, "till", slut_ordet, "är:")
                nod.writechain(nod)  # Skriver ut kedjan till slutord
                raise SolutionFound(nod) #stoppar loopen när nod har hittats
        print("Det finns tyvärr ingen väg till ordet:", slut_ordet)
    except SolutionFound:
        print()

if __name__ == '__main__':
    main()

"""
Vid redovisningen ska du kunna:
-visa upp och redogöra för de förberedande uppgifterna ovan (se labb5 instruktionen),
-rita och förklara skillnaden i datastrukturen jämfört med förra labben,
-visa hur utskriften av lösningen fungerar med din rekursiva funktion
"""