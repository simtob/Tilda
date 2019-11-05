from linkedQFile import *
from sys import stdin
import string
class Node:
   def __init__(self, x, next = None):
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

    def restart(self):
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

class Syntaxfel(Exception):
    pass

atoms = ["H","He","Li","Be","B","C","N","O","F","Ne","Na","Mg","Al","Si","P","S","Cl","Ar","K","Ca","Sc","Ti","V","Cr" \
"Mn","Fe","Co","Ni","Cu","Zn","Ga","Ge","As","Se","Br","Kr","Rb","Sr","Y","Zr","Nb","Mo","Tc","Ru","Rh","Pd","Ag","Cd", \
"In","Sn","Sb","Te","I","Xe","Cs","Ba","La","Ce","Pr","Nd","Pm","Sm","Eu","Gd","Tb","Dy","Ho","Er","Tm","Yb","Lu","Hf", \
"Ta","W","Re","Os","Ir","Pt","Au","Hg","Tl","Pb","Bi","Po","At","Rn","Fr","Ra","Ac","Th","Pa","U","Np","Pu","Am","Cm", \
"Bk","Cf","Es","Fm","Md","No","Lr","Rf","Db","Sg","Bh","Hs","Mt","Ds","Rg","Cn","Fl","Lv"]

atompair = []

def storemol(mol): #Lagrar molekyl
    for char in mol:
        q.enqueue(char)
    return q

def readformel(mol):
    storemol(mol)
    try:
        readmol()
        if len(atompair) > 0:
            raise Syntaxfel('Saknad högerparentes vid radslutet ')
        else:
            return "Formeln är syntaktiskt korrekt"
    except Syntaxfel as error:
        return str(error) + printQ()

def readmol():
    readgroup() #Läser gruppen
    if q.peek() == ")":
        if len(atompair) < 1:
            raise Syntaxfel("Felaktig gruppstart vid radslutet ")
        else:
            return
    elif q.peek():
        if q.peek() == "(" or q.peek().isupper() or q.peek().islower():
            readmol()
    elif q.isEmpty():
        return
    else:
        readmol()

def readgroup():
    if q.isEmpty():
        raise Syntaxfel("Felaktig gruppstart vid radslutet ")
    if q.peek().isupper() or q.peek().islower(): #kollar om det är bokstav
        readatom()
        if q.peek() is None:
            return
        if q.peek().isdigit():
            readnum()

    elif q.peek() == "(":
        atompair.append(q.dequeue())
        readmol()
        if q.peek() != ")":
            raise Syntaxfel("Saknad högerparentes vid radslutet ")
        if q.isEmpty() or q.peek().isdigit():  # Kan ej börja med tal, blir raise. Och kan ej vara tom
            raise Syntaxfel("Saknad siffra vid radslutet ")

        else:
            atompair.pop()  # Ifall inget funkar tas pairingen bort
            q.dequeue()  # Bort från kön
            if q.isEmpty():  # Eller om kön är tom blir det ju fel.
                raise Syntaxfel("Saknad siffra vid radslutet ")
        readnum()  # Numret läses då när grupp inte finns

    else:  # Annars blir det fel gruppstart
        raise Syntaxfel("Felaktig gruppstart vid radslutet ")


def readatom():
    if q.peek().isupper():
        first = q.dequeue()

    else:
        raise Syntaxfel("Saknad stor bokstav vid radslutet ")

    if q.peek() != None:
        if q.peek().islower():
            second = q.dequeue()
            first = first + second

    if first in atoms:
        return
    else:
        raise Syntaxfel("Okänd atom vid radslutet ")


def readnum():
    """<num>   ::= 2 | 3 | 4 | ..."""
    if q.peek().isdigit():
        if q.peek() == "0":
            q.dequeue()
            raise Syntaxfel("För litet tal vid radslutet ")
        num = ""
        if q.isEmpty():
            return

        while not q.isEmpty():
            if q.peek() == None:
                pass
            elif q.peek().isdigit():
                num += q.dequeue()
            else:
                break

        if int(num) < 2:
            raise Syntaxfel("För litet tal:" + num)
        else:
            return

def printQ():
	items = ""
	while not q.isEmpty():
		items = items + q.dequeue()
	return items



def main():
    #stdin = open(file_name1)
    for line in stdin:
        mol = line.strip()
        if mol != "#":
            res = readformel(mol)
            del atompair[:]
            printQ()
            q.restart()
            print(res)
            main()


if __name__ == '__main__':
    file_name1 = "correct_sample.in"
    file_name2 = "incorrect_sample.in"
    main()