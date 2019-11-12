

from sys import stdin


class Node():
    def __init__(self, x, next=None):
        self.data = x
        self.next = next


class LinkedQ():  # Klassen som skapar Linkedkön

    def __init__(self):
        self.first = None
        self.last = None

    def enqueue(self, x):
        new = Node(x)
        if self.first == None:
            self.first = new
            self.last = new
            new.next = None
        if self.first != None:
            self.last.next = new
            self.last = new
            new.next = None

    def dequeue(self):
        if self.first == None:
            return None
        else:
            popp = self.first
            self.first = self.first.next
            return popp.data

    def isEmpty(self):
        if self.first == None:
            return True
        else:
            return False

    def peek(self):
        if self.first is not None:
            return self.first.data
        else:
            return None


atomList = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K',
            'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb',
            'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs',
            'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta',
            'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa',
            'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt',
            'Ds', 'Rg', 'Cn', 'Fl', 'Lv']


class SyntaxError(Exception):
    pass


def readFormel(q):
    while q.peek() is not ".":
        readMol(q)


def readMol(q):
    readGroup(q)
    if readCapitalLetter(q.peek()) or q.peek() == "(":  # Kollar början av kön
        readMol(q)


def readGroup(q):
    if q.peek() == "(":  # Molekylgrupp i en parantes
        q.dequeue()
        readMol(q)
        if q.peek() == ")":
            q.dequeue()
            readNumber(q)
        else:
            raise SyntaxError("Saknad högerparentes vid radslutet " + printQ(q))
    elif readCapitalLetter(q.peek()) or readSmallLetter(q.peek()):  # Molekyl utan parantes
        readAtom(q)
    else:
        raise SyntaxError("Felaktig gruppstart vid radslutet " + printQ(q))


def readAtom(q):
    capital_letter = q.dequeue()
    if readCapitalLetter(capital_letter):
        if readSmallLetter(q.peek()):
            small_letter = q.dequeue()
            atom = str(capital_letter) + str(small_letter)
            if atom not in atomList:
                raise SyntaxError("Okänd atom vid radslutet " + printQ(q))
        else:
            if capital_letter not in atomList:
                raise SyntaxError("Okänd atom vid radslutet " + printQ(q))
        if q.peek().isdigit():
            readNumber(q)
    else:
        raise SyntaxError("Saknad stor bokstav vid radslutet " + capital_letter + printQ(q))


def readCapitalLetter(capital_letter):
    return capital_letter.isupper()


def readSmallLetter(small_letter):
    return small_letter.islower()


def readNumber(q):
    if q.peek().isdigit():
        tal = q.dequeue()
        if int(tal) == 0:
            raise SyntaxError("För litet tal vid radslutet " + printQ(q))
        elif tal.isdigit():
            while q.peek().isdigit():
                nastaTal = q.dequeue()
                tal += nastaTal
            if int(tal) < 2:
                raise SyntaxError("För litet tal vid radslutet " + printQ(q))
        else:
            raise SyntaxError("Saknad siffra vid radslutet " + tal + printQ(q))
    else:
        raise SyntaxError("Saknad siffra vid radslutet " + printQ(q))


def syntaxkontroll(molekyl):
    q = LinkedQ()
    for char in molekyl:
        q.enqueue(char)
    q.enqueue(".")
    try:
        readFormel(q)
        return "Formeln är syntaktiskt korrekt"
    except SyntaxError as error:
        return str(error)


def printQ(q):
    rest = ""
    while not q.peek() == ".":
        word = q.dequeue()
        rest += word
    return rest


def main():
    while True:
        formel = stdin.readline()
        if "#" in formel:
            return False
        else:
            resultat = syntaxkontroll(formel)
            print(resultat)


main()



