

from linkedQFile import *
import sys
import string
from molgrafik import *
from hashtest import *

q = LinkedQ()

pairing = []

ALLAATOMER = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K',
              'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb',
              'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs',
              'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf',
              'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th',
              'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs',
              'Mt', 'Ds', 'Rg', 'Cn', 'Fl', 'Lv']

hashadeAtomer = lagraHashtabell(skapaAtomlista())



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
            readmol()
    elif q.isEmpty():
        return mol
    else:
        mol.next = readmol()
    return mol


def readgroup():
    rutas = Ruta()
    if q.isEmpty() or q.peek().isdigit():  # Om kön är tom, raise syntaxfel, inte får börja med nummer
        raise Syntaxfel("Felaktig gruppstart vid radslutet ")

    if q.peek().isupper() or q.peek().islower():  # kollar om det är bokstav
        rutas.atom = readatom()  # Läser atomen
        if q.peek() is None:  # Om peeken är inget
            return rutas

        if q.peek().isdigit():  # Om nästa tecken är nummer
            rutas.num = int(readnum())  # Anropa funktionen där numret läses


    elif q.peek() == "(":  # Om en grupp börjar med (, ok! Läggs in i kön
        pairing.append(q.dequeue())  # Läggs in i kön gruppvis
        rutas.down = readmol()  # Anropar funktion där molykylen läses

        if q.peek() != ")":  # Eftersom en grupp måste ha () blir det fel om det inte slutar på)
            raise Syntaxfel("Saknad högerparentes vid radslutet ")
        if q.isEmpty() or q.peek().isdigit():  # Kan ej börja med tal, blir raise. Och kan ej vara tom
            raise Syntaxfel("Saknad siffra vid radslutet ")

        else:
            pairing.pop()  # Ifall inget funkar tas pairingen bort
            q.dequeue()  # Bort från kön
            if q.isEmpty():  # Eller om kön är tom blir det ju fel.
                raise Syntaxfel("Saknad siffra vid radslutet ")
        rutas.num = int(readnum())  # Numret läses då när grupp inte finns
    else:  # Annars blir det fel gruppstart
        raise Syntaxfel("Felaktig gruppstart vid radslutet ")
    return rutas


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


def readvikt(ruta):
    if ruta.atom == "()":
        if ruta.down != None:
            x = float(readvikt(ruta.down)) * float(ruta.num)
    else:
        x = float(hashadeAtomer.search(ruta.atom).data.vikt) * float(ruta.num)

    if ruta.next != None:
        y = readvikt(ruta.next)
        return x + y
    else:
        return x


def readFormel(themol):
    storemol(themol)
    try:
        themol = readmol()
        if len(pairing) is None:
            raise Syntaxfel('Saknad högerparentes vid radslutet ')
        else:
            print("Formeln är syntaktiskt korrekt")
            print("Vikten av din molekyl är: " + str(readvikt(themol)))
            return themol
    except Syntaxfel as error:
        return str(error) + printQ()


def main():
    # kodupprepning på alla raise Syntaxfel
    molekyl = input("Molekyl: ")
    mg = Molgrafik()
    if molekyl == "exit":
        pass
    else:
        mol = readFormel(molekyl)
        mg.show(mol)

        del pairing[:]
        printQ()
        q.restart()
        main()


if __name__ == '__main__':
    main()