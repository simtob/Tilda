#LABB 3: Binära Träd

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

"""
svenska = Bintree()  # Skapa ett trädobjekt
svenska.put("gurka")  # Sortera in "gurka" i trädet
svenska.put("tomat")
svenska.put("sallad")
svenska.put("apelsin")
svenska.put("broccoli")

if "gurka" in svenska:
    svenska.write() # Skriver alla trädobjektets ord i bokstavsordning
"""
#Uppgift 2:
"""
svenska = Bintree()
with open("word3.txt", "r", encoding = "utf-8") as svenskfil:
    for rad in svenskfil:
        ordet = rad.strip()                # Ett trebokstavsord per rad
        if ordet in svenska:
            print(ordet, end = " ")
        else:
            svenska.put(ordet)             # in i sökträdet
print("\n")
"""
#Uppgift 3:
"""
engelska = Bintree()
with open("engelska.txt", "r", encoding = "utf-8") as engelskfil:
    for rad in engelskfil:
        rad = rad.strip()
        ordlista = rad.split()
        for ord in ordlista:
            if not ord in engelska:
                if ord in svenska:
                    print(ord, end= " ")
                engelska.put(ord)
"""
#Balanserat träd -  För varje nod i trädet så är skillnaden i höjden
# mellan det högra och det vänstra subträdet högst 1

#Rekursivt - Repeterar en kodrad