from linkedQFile import *
import sys


q = LinkedQ()

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
