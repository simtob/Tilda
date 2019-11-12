import sys
#from linkedQfile import *
import string
from molgrafik import*
from hashtest import*

hash_myAtoms = store_myHashtable(make_myAtomlist())

class Ruta:
    def __init__(self, atom="( )", num=1):
        self.atom = atom
        self.num = num
        self.next = None
        self.down = None

class Node:
    def __init__(self, x, next=None):
        self.value = x
        self.next = next


class LinkedQ():

    def __init__(self):
        self._first = None
        self._last = None  # sign for int
        self._size = 0

    def isEmpty(self):
        if self._first == None:
            return True
        else:
            return False

    def enqueue(self, x):
        new = Node(x)
        if self.isEmpty():
            self._first = new
            self._last = new
        else:
            self._last.next = new
        self._last = new
        self._size += 1

    def dequeue(self):
        x = self._first.value
        self._first = self._first.next
        self._size -= 1
        return x

    def size(self):
        return (self._size)

    def empty(self):
        self._first = None
        self._last = None

    def peek(self):
        if not self.isEmpty():
            return self._first.value
        else:
            return None


"""
<formel>::= <mol> \n
<mol>   ::= <group> | <group><mol>
<group> ::= <atom> |<atom><num> | (<mol>) <num>
<atom>  ::= <LETTER> | <LETTER><letter>
<LETTER>::= A | B | C | ... | Z
<letter>::= a | b | c | ... | z
<num>   ::= 2 | 3 | 4 | ... 
"""
q = LinkedQ()

pairing = []

ALLAATOMER = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K',
              'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb',
              'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs',
              'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf',
              'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th',
              'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs',
              'Mt', 'Ds', 'Rg', 'Cn', 'Fl', 'Lv']


class Syntaxfel(Exception):
    pass

def storemol(themol):  # Lagrar molekyl i en kö
    for everychar in themol:  # varje karaktär i molykylen läggs in i kön
        q.enqueue(everychar)
    return q


def readmol():
    mol = readgroup()  # Läser gruppen
    if q.peek() == ")":
        if len(pairing) < 1:
            raise Syntaxfel("Felaktig gruppstart vid radslutet ")
        else:
            return mol
    elif q.peek():
        if q.peek() == "(" or q.peek().isupper() or q.peek().islower():
            mol.next = readmol()
    elif q.isEmpty():
        return mol
    else:
        mol.next = readmol()
    return mol


def readgroup():
    ruta = Ruta()
    if q.isEmpty() or q.peek().isdigit():  # Om kön är tom, raise syntaxfel, inte får börja med nummer
        raise Syntaxfel("Felaktig gruppstart vid radslutet ")

    if q.peek().isupper() or q.peek().islower():  # kollar om det är bokstav
        ruta.atom = readatom()  # Läser atomen
        if q.peek() is None:  # Om peeken är inget
            return ruta

        if q.peek().isdigit():  # Om nästa tecken är nummer
            ruta.num = int(readnum())  # Anropa funktionen där numret läses


    elif q.peek() == "(":  # Om en grupp börjar med (, ok! Läggs in i kön
        pairing.append(q.dequeue())  # Läggs in i kön gruppvis
        ruta.down = readmol()  # Anropar funktion där molykylen läses

        if q.peek() != ")":  # Eftersom en grupp måste ha () blir det fel om det inte slutar på)
            raise Syntaxfel("Saknad högerparentes vid radslutet ")
        if q.isEmpty() or q.peek().isdigit():  # Kan ej börja med tal, blir raise. Och kan ej vara tom
            raise Syntaxfel("Saknad siffra vid radslutet ")

        else:
            pairing.pop()  # Ifall inget funkar tas pairingen bort
            q.dequeue()  # Bort från kön
            if q.isEmpty():  # Eller om kön är tom blir det ju fel.
                raise Syntaxfel("Saknad siffra vid radslutet ")
        ruta.num = int(readnum())  # Numret läses då när grupp inte finns
    else:  # Annars blir det fel gruppstart
        raise Syntaxfel("Felaktig gruppstart vid radslutet ")
    return ruta

def readatom():
    if q.peek().isupper():
        first = q.dequeue()

    else:
        raise Syntaxfel("Saknad stor bokstav vid radslutet ")

    if q.peek() is not None and q.peek().islower():
        first = first + q.dequeue()

    if first not in ALLAATOMER:
        raise Syntaxfel("Okänd atom vid radslutet ")
    else:
        return first



def readnum():
    if q.peek().isdigit():
        if q.peek() == "0":
            q.dequeue()
            raise Syntaxfel("För litet tal vid radslutet ")

        nummer = ""
        while not q.isEmpty():
            if q.peek() is None:
                pass
            elif q.peek().isdigit():
                nummer += q.dequeue()
            else:
                break
        if int(nummer) < 2:
            raise Syntaxfel("För litet tal vid radslutet ")
        else:
            return nummer
    else:
        raise Syntaxfel("Saknad siffra vid radslutet ")


def printQ():
    items = ""
    while not q.isEmpty():
        items = items + q.dequeue()
    return items

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------


def get_weigth(ruta):

    if ruta.atom == "( )":
        if ruta.down is not None:
            item1 = float(get_weigth(ruta.down)) * float(ruta.num) #hämtar vikten från ner pekare gångrar med numret
            #Kollar om vi har ett parentespar, kollar om down inte är none
            #dvs har en atom, tar då atomen * antalet av den atomen (num)
    else:
        item1 = float(hash_myAtoms.search(ruta.atom).value.vikt) * float(ruta.num)
        #Om den inte är tom kollar efter en atom som finns

    if ruta.next is None:
        return item1 #om nästa ruta är tom, returnera vikt på vår atom
    else:
        item2 = get_weigth(ruta.next) #annars ta vikten på nästa och addera med första
        return item1 + item2


def readformel(themol):
    storemol(themol)
    try:
        themol = readmol()
        if len(pairing) is None:
            raise Syntaxfel('Saknad högerparentes vid radslutet ')
        else:
            print("Vikten av din molekyl är: " + str(get_weigth(themol)))
            print("Ritar atomen....")
            return themol
    except Syntaxfel as error:
        return str(error) + printQ()

def main():
    #sys.stdin = open(f1) #stdin testar input
    mol_input = input("Ange molekyl: ")
    mg = Molgrafik()

    if mol_input == "exit":
        pass
    else:
    #for line in sys.stdin:
     #   mol = line.strip()
      #  if mol != "#":
        mol = readformel(mol_input)
        mg.show(mol)
        pairing.clear()
        printQ()
        q.empty()
        main()

if __name__ == '__main__':
    f1 = "correct_sample.in"
    f2 = "incorrect_sample.in"
    main()