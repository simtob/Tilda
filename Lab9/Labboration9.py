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

ATOMER = ["H","He","Li","Be","B","C","N","O","F","Ne","Na","Mg","Al","Si","P","S","Cl","Ar","K","Ca","Sc","Ti","V","Cr" \
"Mn","Fe","Co","Ni","Cu","Zn","Ga","Ge","As","Se","Br","Kr","Rb","Sr","Y","Zr","Nb","Mo","Tc","Ru","Rh","Pd","Ag","Cd", \
"In","Sn","Sb","Te","I","Xe","Cs","Ba","La","Ce","Pr","Nd","Pm","Sm","Eu","Gd","Tb","Dy","Ho","Er","Tm","Yb","Lu","Hf", \
"Ta","W","Re","Os","Ir","Pt","Au","Hg","Tl","Pb","Bi","Po","At","Rn","Fr","Ra","Ac","Th","Pa","U","Np","Pu","Am","Cm", \
"Bk","Cf","Es","Fm","Md","No","Lr","Rf","Db","Sg","Bh","Hs","Mt","Ds","Rg","Cn","Fl","Lv"]


def readformel(q):
    while q.peek():
        readmol(q)

def readmol(q):
    readgroup(q)
    if q.peek():
        if q.peek() == "(" or q.peek().isalpha():
            readmol(q)

def readgroup(q):
    if q.peek().isalpha(): #kollar om det är bokstav
        readatom(q)
    elif q.peek() == "(":
        q.dequeue()
        readmol(q)
        if q.peek() == ")":
            q.dequeue()
            readnum(q)
        else:
            raise Syntaxfel("Saknad högerparentes vid radslutet ")

    elif q.peek() == ")" or q.peek().isdigit():
        raise Syntaxfel("Felaktig gruppstart vid radslutet ")


def readatom(q):
    if q.peek().isupper():
        first = q.dequeue()
        if q.peek():
            if q.peek().islower():
                atomen = first + q.dequeue() #q.dequeue är den andra
                if atomen in ATOMER:
                    if q.peek():
                        if q.peek().isdigit():
                            readnum(q)
                        elif q.peek().isalpha():
                            readatom(q)
                else:
                    raise Syntaxfel("Okänd atom vid radslutet ")

            else: #om nästa bokstav inte är en lower då kollar vi om atomen t.ex. H är i ATOMER (LISTAN)
                if first in ATOMER:
                    if q.peek():
                        if q.peek().isdigit():
                            readnum(q)
                        elif q.peek().isalpha():
                            readatom(q)
                    else:
                        raise Syntaxfel("Okänd atom vid radslutet ")

        else:
            if first not in ATOMER:
                raise Syntaxfel("Okänd atom vid radslutet ")

    elif q.peek().islower():
        raise Syntaxfel("Saknad stor bokstav vid radslutet ")
    elif q.peek().isdigit():
        raise Syntaxfel("Felaktig gruppstart vid radslutet ")


def readnum(q):
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
                            print("APA")
                            break
            if int(number) >= 2:
                return
            else:
                raise Syntaxfel("För litet tal vid radslutet ")
    else:
        raise Syntaxfel("Saknad siffra vid radslutet ")

def printQ(q):
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
        q = LinkedQ()
        for char in line:
            q.enqueue(char)
        try:
            if not q.peek():
                raise Syntaxfel("Felaktig gruppstart vid radslutet ")
            readformel(q)
            print("Formeln är syntaktiskt korrekt ")
        except Syntaxfel as felet:
            rest = printQ(q)
            print(str(felet) + rest)

if __name__ == '__main__':
    file_name1 = "correct_sample.in"
    file_name2 = "incorrect_sample.in"
    main()