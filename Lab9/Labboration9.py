from linkedQFile import *
from sys import stdin
import string
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
        if q.peek().isdigit():
            readnum()
        if q.peek() is None:
            return

    if q.peek.isdigit():
        raise ("Felaktig gruppstart vid radslutet ")

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
        if q.peek():
            if q.peek().islower():
                second = q.dequeue()
                atomen = str(first) + str(second) #q.dequeue är den andra
                if atomen in atoms:
                    return
                else:
                    raise Syntaxfel("Okänd atom vid radslutet ")

        else:
            if first not in atoms:
                raise Syntaxfel("Okänd atom vid radslutet ")
            if first in atoms:
                return
    else:
        raise Syntaxfel("Saknad stor bokstav vid radslutet ")


def readnum():
    """<num>   ::= 2 | 3 | 4 | ..."""
    if q.peek().isdigit():
        number = q.dequeue()
        if number == "0":
            raise Syntaxfel("För litet tal vid radslutet ")
        if q.peek():
            if q.peek().isdigit(): #om nästa också e tal
                while q.peek().isdigit(): #så länge tal
                        number2 = q.dequeue()
                        number = number + number2
                        if not q.peek():
                            break
            if int(number) >= 2:
                return
            else:
                raise Syntaxfel("För litet tal vid radslutet ")
    else:
        raise Syntaxfel("Okänd atom vid radslutet ")

def printQ():
	items = ""
	while not q.isEmpty():
		items = items + q.dequeue()
	return items




def main():
    #stdin = open("Formellkoll_test") #Lätt att ändra för att testa indata från fil
    for line in stdin:
        line = line.strip()
        if line == "#":
            break
        try:
            if not q.peek():
                raise Syntaxfel("Felaktig gruppstart vid radslutet ")
            readformel(q)
            print("Formeln är syntaktiskt korrekt ")
        except Syntaxfel as error:
            rester = printQ()
            print(str(error) + rester)

if __name__ == '__main__':
    file_name1 = "correct_sample.in"
    file_name2 = "incorrect_sample.in"
    main()