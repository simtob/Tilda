from linkedQFile import *
import sys


q = LinkedQ()


class Syntaxfel(Exception):
    pass

def storemol(mol):
    for char in mol:
        q.enqueue(char)
    return q

def readmol():
    readatom()
    if q.peek() == '':
        q.dequeue()
    else:
        readNum()


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
    num = ''
    if q.isEmpty():
        return
    while not q.isEmpty():
        #print(q.peek(), "dequeueas som num")
        if q.peek() == None:
            pass
        elif q.peek().isdigit():
            num += q.dequeue()
        else:
            raise Syntaxfel("För lång atom: " + q.peek())
    if int(num) >= 2:
        return
    else:
        raise Syntaxfel("För litet tal: " + num)


def checksyntax(mol):
    q = storemol(mol)
    try:
        readmol()
        return 'Följer syntaxen!'
    except Syntaxfel as error:
        return str(error)


def main():
    mol = input("skriv en mol: ")
    resultat = checksyntax(mol)
    print(resultat)


if __name__ == '__main__':
    main()
