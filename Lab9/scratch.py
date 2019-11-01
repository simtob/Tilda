from LinkedQFile import LinkedQ
import unittest
from unittest_9 import *

"""
Syntax enligt BNF:
<formel>::= <mol>
<mol>   ::= <group> | <group><mol>
<group> ::= <atom> |<atom><num> | (<mol>) <num>
<atom>  ::= <LETTER> | <LETTER><letter>
<LETTER>::= A | B | C | ... | Z
<letter>::= a | b | c | ... | z
<num>   ::= 2 | 3 | 4 | ...
"""


class SyntaxError(Exception):  # Eget exceptionfel vi lägger till för syntaxen
    pass


def readFormel(q):  # Bearbetar kö och kollar om den följer <formel>
    while q.peek() != ".":
        readMol(q)


def readMol(q):  # Input: kö. Output: T/F. Kollar syntaxen för en Molekyl enligt BNF.
    readGroup(q)
    if readUpper(q.peek()) or q.peek() == "(":
        readMol(q)


def readGroup(q):  # Tar in kö och kollar om den följer syntax för <group> enl. BNF.
    if q.peek() == "(":
        q.dequeue()
        readMol(q)
        if q.peek() == ")":
            q.dequeue()
            readNum(q)
        else:
            raise SyntaxError("Saknad högerparentes vid radslutet " + printQ(q))
    elif readUpper(q.peek()) or readLower(q.peek()):
        readAtom(q)
    else:
        raise SyntaxError("Felaktig gruppstart vid radslutet " + printQ(q))


def readAtom(q):  # Tar in kö och kollar om den följer syntax för <atom> enl. BNF.
    first = q.dequeue()
    if readUpper(first):
        if readLower(q.peek()):
            second = q.dequeue()
            atom = str(first) + str(second)
            if atom not in atomList:
                raise SyntaxError("Okänd atom vid radslutet " + printQ(q))
        else:
            if first not in atomList:
                raise SyntaxError("Okänd atom vid radslutet " + printQ(q))
        if q.peek().isdigit():
            readNum(q)
    else:
        raise SyntaxError("Saknad stor bokstav vid radslutet " + first + printQ(q))


def readUpper(x):  # Input: kö. Output: T/F. Om första elementet i kön är en stor bokstav: True, annars syntaxfel.
    return x.isupper()


def readLower(x):  # Input: kö. Output: T/F. Om första elementet i kön är en liten bokstav: True, annars syntaxfel.
    return x.islower()


def readNum(q):  # Input: kö. Output: T/F. Kollar om den följer syntax för <Num> enl. BNF.
    if q.peek().isdigit():
        x = q.dequeue()
        if int(x) == 0:
            raise SyntaxError("För litet tal vid radslutet " + printQ(q))
        elif x.isdigit():
            while q.peek().isdigit():
                nextX = q.dequeue()
                x += nextX
            if int(x) < 2:
                raise SyntaxError("För litet tal vid radslutet " + printQ(q))
        else:
            raise SyntaxError("Saknad siffra vid radslutet " + x + printQ(q))
    else:
        raise SyntaxError("Saknad siffra vid radslutet " + printQ(q))


def checkSyntax(mol):
    q = storeMol(mol)
    try:
        readFormel(q)
        return "Formeln är syntaktiskt korrekt"
    except SyntaxError as error:
        return str(error)


def storeMol(mol):
    q = LinkedQ()
    for i in list(mol):
        q.enqueue(i)
    q.enqueue(".")
    return q


def printQ(q):
    rest = ""
    while not q.peek() == ".":
        word = q.dequeue()
        rest += word
    return rest


atomList = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K',
            'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb',
            'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs',
            'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta',
            'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa',
            'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt',
            'Ds', 'Rg', 'Cn', 'Fl', 'Lv']


def testSyntax(filename):
    with open(filename, "r", encoding="utf-8") as sample:
        for line in sample:
            mol = line.strip()
            if mol != "#":
                result = checkSyntax(mol)
            return result


def printFile(filename):
    with open(filename, "r", encoding="utf-8") as sample:
        for line in sample:
            lines = line.strip()
            return lines


def main():  # Mainprogrammet som ger användaren möjlighet till input, printar resultatet av syntaxkollen.
    """
    with open("correct_sample_in.txt", "r", encoding="utf-8") as sample:
        for line in sample:
            mol = line.strip()
            if mol != "#":
                result = checkSyntax(mol)
                print(result)
    """

    mol = input("ge mig en molekyl: ")
    resultat = checkSyntax(mol)
    print(resultat)


if __name__ == "__main__":
    unittest.main()
