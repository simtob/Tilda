class Syntaxfel(Exception):
    pass


class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


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

    def peek(self):
        if not self.isEmpty():
            return self._first.value
        else:
            return None


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


def readNum(letter, q):
    try:
        num = int(letter)
        return True
    except ValueError:
        return False

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




