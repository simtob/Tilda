from linkedQFile import *
import sys
import string


q = LinkedQ()

pairs = []
ATOMER = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Fl', 'Lv']

class Syntaxfel(Exception):
    pass

def storemol(mol): #Lagrar molekyl
    for char in mol:
        q.enqueue(char)
    return q

def readmol(): #Läser molekyl
    readatom()
    if q.peek() == '':
        q.dequeue()
    else:
        readNum()
    if not q.isEmpty():
        raise Syntaxfel("Atomen för lång")



def readatom():
    readStorbokstav()
    if q.peek() is None or q.peek().isdigit():
        return
    else:
        readLitenbokstav()


def readStorbokstav():
    storbokstav = q.dequeue()
    if storbokstav.isupper():
        return
    raise Syntaxfel("Den är inte en storbokstav: " + storbokstav)


def readLitenbokstav():
    litenbokstav = q.dequeue()
    if litenbokstav.islower():
        return
    raise Syntaxfel("Det är inte en litenbokstav: " + litenbokstav)


def readNum():
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


def syntaxcontrol(mol):
    storemol(mol)
    try:
        readmol()
        return 'Syntaxen stämmer!'
    except Syntaxfel as error:
        return str(error)

def main():
    mol = input("Molekyl: ")
    result = syntaxcontrol(mol)
    print(result)


if __name__ == '__main__':
    main()
