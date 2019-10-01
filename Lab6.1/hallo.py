
import timeit
import random
class Bintree:
    def __init__(self):
        self.root = None

    def put(self,newvalue):
        # Sorterar in newvalue i trädet
        node = Node(newvalue) #gör om strängen till en nod
        self.root = putta(self.root,node)


    def __contains__(self,value):
        return finns(self.root,value)
        # True om value finns i trädet, False annars

    def write(self):
        # Skriver ut trädet i inorder
        skriv(self.root)
        print("\n")

class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def finns(p, value):
    letar = True
    while letar:
        if p == None:
            return False
        if value == p.value:
            return True
        if value < p.value:
            return finns(p.left, value)
        if value > p.value:
            return finns(p.right, value)

def putta(p, newNode): #Trädet skickar sin rotpekare och det nya ordet till funktionen putta som
    # Ser till att en ny nod skapas på rätt ställe.
    if p is None:
        p = newNode
        return p
    if newNode.value < p.value:
        if p.left == None: #Två fall, Fall 1: antingen är noden som pekar till vänster tom
            p.left = newNode
            return p
        else: #Fall 2: puttar igen tills newNode inte pekar på ett nytt värde
            putta(p.left, newNode)
            return p
    if newNode.value > p.value:
        if p.right == None:
            p.right = newNode
            return p
        else:
            putta(p.right, newNode)
            return p
    return p

def skriv(p): #skriver inordning, skriver ut först vänsterträdet sedan rottalet och sist höger trädet
    if p != None:
        skriv(p.left)
        print(p.value)
        skriv(p.right)



class Lat:
    def __init__(self, trackid, lattid, artist, lattitel):
        self.trackid = trackid
        self.lattid = lattid
        self.artist = artist
        self.lattitel = lattitel

    def __lt__(slef, other):
        return self.artist < other.artist

    def __str__(self):
        return "TrackID: " + self.trackid + " Låttid: " + self.lattid + " Artist: " + self.artist + " Låttitel: " + self.lattitel


def readfile(filename):
    latList = []
    latDict = {}
    latTree = Bintree()
    artistTree = Bintree()
    with open(filename, "r", encoding="utf-8") as fil:
        for rader in fil:
            attr = rader.split("<SEP>")
            lat = Lat(attr[0], attr[1], attr[2], attr[3])

            latList.append(lat)
            latDict[lat.artist] = lat
            artistTree.put(lat.artist)

    return latList, latDict, artistTree


def linsok(listan, nyckel):
    """hämtad från föreläsning 3"""
    """den söker igenom hela listan tills den hittar nyckel eller det uppenbaras att den inte finns"""
    for x in listan:
        if x == nyckel:
            return True
    return False


def binsok(listan, nyckel):
    """Från föreläsning 3"""
    """Söker i "listan" efter "nyckel". Returnerar True om den hittas, False annars"""
    """Den räknar ut vart mitten är och avgör vänster eller höger. Sedan fortsätter den så tills den hittar nyckeln eller nyckeln inte finns"""
    vanster = 0
    hoger = len(listan) - 1
    found = False

    while vanster <= hoger and not found:
        mitten = (vanster + hoger) // 2
        if listan[mitten].artist == nyckel:
            found = True
        else:
            if nyckel < listan[mitten].artist:
                hoger = mitten - 1
            else:
                vanster = mitten + 1
    return found


def main():
    testartist2 = input("Välj en artist: ")

    filename = "unique_tracks.txt"

    lista, dictionary, artistTree = readfile(filename)
    n = len(lista)
    print("Antal element =", n)

    sista = lista[n - 6]
    testartist1 = sista.artist

    """# To return a new list, use the sorted() built-in function...
    newlist = sorted(ut, key=lambda x: x.count) från stack overflow, inbyggd pythonmetod"""
    sorteradLista = sorted(lista, key=lambda x: x.artist)

    bintid = timeit.timeit(stmt=lambda: sorted(lista, key=lambda x: x.artist), number=1)
    print("Sorteringen tog", round(bintid, 4), "sekunder")

    linjtid = timeit.timeit(stmt=lambda: linsok(lista, testartist1), number=10)
    print("Linjärsökningen tog", round(linjtid, 4), "sekunder")

    bintid = timeit.timeit(stmt=lambda: binsok(sorteradLista, testartist1), number=10)
    print("Binärsökningen tog", round(bintid, 4), "sekunder")

    dicttid = timeit.timeit(stmt=lambda: dictionary[testartist1], number=10)
    print("Dictsökningen tog", round(dicttid, 4), "sekunder")

    bintreetid = timeit.timeit(stmt=lambda: testartist1 in artistTree, number=10)
    print("Bintreesökningen tog", round(bintreetid, 4), "sekunder")

    """linjtid = timeit.timeit(stmt = lambda: linsok(lista, testartist2), number = 10)
    print("Linjärsökningen av artisten tog", round(linjtid, 4) , "sekunder")"""

    """bintid = timeit.timeit(stmt = lambda: binsok(sorteradLista, testartist2), number = 10)
    print("Binärsökningen av artisten tog", round(bintid, 4) , "sekunder")"""

    """if testartist2 in artistTree:
        print(testartist2 + " finns")
    else:
        print("Finns inte")
    dicttid = timeit.timeit(stmt = lambda: dictionary[testartist2], number = 10)
    print("Dictsökningen av artisten tog", round(dicttid, 4) , "sekunder")"""


if __name__ == '__main__':
    main()

"""Analys:
Linjärsökningen är O(n), i värsta fall ska det ta 10s men det tar 1.58s
Binärsökningen är O(log2(n)), i värsta fall tar den 3.32s och för oss tar den 0.0001s.
Dictsökningen är supersnabb, o.o s. I värsta fall O(1) Går direkt till det sökta elementet.
Sorted() har i både vanliga fallet och västa fallet O(n*log2(n)). n=10 ger värsta fallet ca 33.219s, vi får 17.03s"""

