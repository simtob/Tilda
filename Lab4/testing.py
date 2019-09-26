
from linkedQfilen import LinkedQ
from Lab3use import Bintree


class SolutionFound(Exception):
    pass



q = LinkedQ()
#Hämta alla ord från filen och stoppa in i binärträd, sen när du genererar ord för de här tre ord bokstävena,
# titta om det existerar i vårt binärt träd

class ParentNode:
    def __init__(self, word, parent = None):
        self.word = word
        self.parent = parent

    def writechain(self, child):
        if child.parent == None:
            print(child.word)
        else:
            self.writechain(child.parent)
            print(child.word)

def read_file():
    svenska = Bintree()
    with open("word3.txt", "r", encoding = "utf-8") as svenskfil:
        for rad in svenskfil:
            ordet = rad.strip()
            svenska.put(ordet)
    return svenska




def makechildren(start_ordet, q, svenska, gamla):

    alphabet = "abcdefghijklmnopqsrtuvwxyzåäö"
    for i in range(len(start_ordet)):
        barn = start_ordet
        barn = list(barn) #skapar list för att enkelt byta ut bokstaven

        for letter in alphabet:
            if letter != barn[i]:
                barn[i] = letter #ersätter första förekomsten av barn av [i]
                barn_str = "".join(barn) #joinar listan till en sträng, med avseende på en avskiljare i vårt fall ""
                if barn_str in svenska and barn_str not in gamla:
                    gamla.put(barn_str)
                    q.enqueue(barn_str)




def main():
    start_ordet = str(input("ange startord: "))
    slut_ordet = str(input("ange slutord: "))
    q.enqueue(start_ordet)

    svenska = read_file()
    gamla = Bintree()
    gamla.put(start_ordet)

    while not q.isEmpty():
        nod = q.dequeue()
        makechildren(nod, q, svenska, gamla)
        if nod == slut_ordet:
            print("Hittat en väg till", slut_ordet)


main()



svenska = Bintree()
gamla = Bintree()
q = LinkedQ()


def makechildren(startord):
    alphabet = "abcdefghijklmnopqrstuvwxyzåäö"
    gamla.put(startord.word)
    for i in range(len(startord.word)):  # Varje element i startordet
        for j in alphabet:  # Ersätter med varje bokstav i alfabetet
            newWord = list(startord.word)
            newWord[i] = j
            newWord = "".join(newWord)
            if newWord in svenska and newWord not in gamla:
                gamla.put(newWord)
                newNode = ParentNode(newWord)
                newNode.parent = startord
                q.enqueue(newNode)


def readfile():
    with open("word3.txt", "r", encoding="utf-8") as svenskfil:
        for rad in svenskfil:
            ordet = rad.strip()  # Ett trebokstavsord per rad
            if ordet in svenska:
                gamla.put(ordet)
            else:
                svenska.put(ordet)  # in i sökträdet


def main():
    readfile()
    startord = input("Mata in startord: ")
    slutord = input("Mata in slutord: ")
    pnode = ParentNode(startord)
    q.enqueue(pnode)
    try:
        while not q.isEmpty():
            nod = q.dequeue()
            makechildren(nod)
            if nod.word == slutord:
                print("\nVägen från", startord, "är:")
                nod.writechain(nod)  # Skriver ut kedjan till slutord
                raise SolutionFound(nod)
        print("Det finns ingen väg till", slutord)
    except SolutionFound as nod:
        print()


if __name__ == '__main__':
    main()

