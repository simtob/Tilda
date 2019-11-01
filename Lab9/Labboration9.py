from linkedQFile import *
import sys
import string

q = LinkedQ()

pairs = []
ATOMER = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca',
          'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr',
          'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba',
          'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W',
          'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U',
          'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds',
          'Rg', 'Cn', 'Fl', 'Lv']


class Syntaxfel(Exception):
    pass


def storemol(mol):  # Lagrar molekyl
    for char in mol:
        q.enqueue(char)
    return q


def readmol():  # Läser molekyl
    """<mol>   ::= <group> | <group><mol>"""
    """readmol() anropar readgroup() och sedan eventuellt sig själv
    (men inte om inmatningen är slut eller om den just kommit tillbaka från ett parentesuttryck)"""
    readGroup()
    if q.isEmpty():
        return
    elif q.peek() == ")":
        if len(pairs) < 1:
            raise Syntaxfel("Felaktig gruppstart vid radslutet "+ printQ())
        return
    else:
        readmol()


def readGroup():
    if q.isEmpty(): #om q tom
        raise Syntaxfel("Felaktig gruppstart vid radslutet "+ printQ())
    if q.peek().isdigit(): #om första är ett tal
        raise Syntaxfel("Felaktig gruppstart vid radslutet "+ printQ())
    if q.peek().isalpha():  # Kollar om första är alfabet eller inte
        readatom() #läser atom
        if q.peek() is None: #om ingen bokstav return
            return
        if q.peek().isdigit(): #om det är ett tal, run readNum()
            readNum()
        return

    elif q.peek() == "(": #om nästa är parentes för början "("
        pairs.append(q.dequeue) #lagrar den i tom lista
        readmol() #läser av molekylen

        if q.peek != ")":
            raise Syntaxfel("Saknad högerparentes vid radslutet "+ printQ())
        if q.isEmpty():
            raise Syntaxfel("Saknad siffra vid radslutet " + printQ())
        else:
            pairs.pop()
            q.dequeue()
            if q.isEmpty():
                raise Syntaxfel("Saknad siffra vid radslutet "+ printQ())
            readNum()
    else:
        raise Syntaxfel("Felaktig gruppstart vid radslutet " + printQ())


def readatom():
    """<atom>  ::= <LETTER> | <LETTER><letter>"""
    upper = q.dequeue()
    if upper.isupper():
        if q.peek().islower():
            lower  = q.dequeue()
            atomen = str(upper) + str(lower)
            if atomen not in ATOMER:
                raise Syntaxfel("Okänd atom vid radslutet " + printQ())
            if peek.isdigit()


        x = q.dequeue()
    else:
        raise Syntaxfel("Saknad stor bokstav vid radslutet ")

    if q.peek() != None:
        if q.peek().islower():
            x = x + q.dequeue()

    if x in ATOMER:
        return
    else:
        raise Syntaxfel("Okänd atom vid radslutet ")



def readNum():
    if q.peek().isdigit():
        num = ""
        while not q.isEmpty():
            if q.peek() == None:
                pass
            elif q.peek().isdigit():
                num += q.dequeue()
            else:
                break

        if int(num) >= 2:
            return
        else:
            raise Syntaxfel("För litet tal vid radslutet "+ printQ())
    else:
        raise Syntaxfel("Saknad siffra vid radslutet "+ printQ())


def printQ():
    it = ""
    while not q.isEmpty():
        it = it + q.dequeue()
    return it


def readformel(mol):
    storemol(mol)
    try:
        readmol()
        if len(pairs) > 0:
            raise Syntaxfel("Saknad högerparentes vid radslutet "+ printQ())
        return 'Formeln är syntatiskt korrekt!'
    except Syntaxfel as error:
        return str(error) + printQ()


def main():
    # kodupprepning på alla raise Syntaxfel
    mol = sys.stdin.readline().strip()
    if mol != "#":
        result = readformel(mol)
        del pairs[:]
        printQ()
        q.empty()
        print(result)
        main()


if __name__ == '__main__':
    main()
