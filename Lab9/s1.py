import sys
import string

class Node:
   def __init__(self, x, next = None):
      self.value = x
      self.next = next

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

    def empty(self):
        self._first = None
        self._last = None


    def peek(self):
        if not self.isEmpty():
            return self._first.value
        else:
            return None

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


pairing = []

ALLAATOMER = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Fl', 'Lv']


class Syntaxfel(Exception):
    pass

def storemol(themol): #Lagrar molekyl i en kö
    for everychar in themol:
        q.enqueue(everychar)
    return q



def readmol():
    readgroup()
    if q.isEmpty():
        return
    elif q.peek() == ")":
        if len(pairing) < 1:
            raise Syntaxfel("Felaktig gruppstart vid radslutet ")
        return
    elif q.peek():
        if q.peek() == "(" or q.peek().isalpha():
            readmol()
    else:
        readmol()

def readgroup():

    if q.isEmpty():
        raise Syntaxfel("Felaktig gruppstart vid radslutet ")

    if q.peek().isalpha(): #kollar om det är bokstav
        readatom()
        if q.peek() is None:
            return

        if q.peek().isdigit():
            readnum()
        return

    elif q.peek() == "(":
        pairing.append(q.dequeue())
        readmol()
        if q.peek() != ")":
            raise Syntaxfel("Saknad högerparentes vid radslutet ")
        if q.isEmpty() or q.peek().isdigit():
            raise Syntaxfel("Saknad siffra vid radslutet ")

        else:
            pairing.pop()
            q.dequeue()
            if q.isEmpty():
                raise Syntaxfel("Saknad siffra vid radslutet ")
        readnum()
    else:
        raise Syntaxfel("Felaktig gruppstart vid radslutet ")


def readatom():
    """<atom>  ::= <LETTER> | <LETTER><letter>"""

    if q.peek().isupper():
        x = q.dequeue()
    # print(x, "readAtom stor bokstav")
    else:
        raise Syntaxfel("Saknad stor bokstav vid radslutet ")

    if q.peek() != None:
        if q.peek().islower():
            x = x + q.dequeue()
        # print("Atomen är", x)

    if x in ALLAATOMER:
        return
    else:
        raise Syntaxfel("Okänd atom vid radslutet ")


def readnum():
	"""<num>   ::= 2 | 3 | 4 | ..."""

	if q.peek().isdigit():
		if q.peek() == "0":
			q.dequeue()
			raise Syntaxfel("För litet tal vid radslutet ")

		num = ""
		while q.peek() != None:
			if q.peek().isdigit():
				num = num + q.dequeue()
			else:
				break
		if int(num) >= 2:
			#print(num)
			return
		else:
			raise Syntaxfel("För litet tal vid radslutet ")
	else:
		raise Syntaxfel("Saknad siffra vid radslutet ")

def printQ():
	items = ""
	while not q.isEmpty():
		items = items + q.dequeue()
	return items

def readformel(themol):
    """<formel>::= <mol> \n"""
    q = storemol(themol)
    try:
        readmol()
        if len(pairing) > 0:
            raise Syntaxfel('Saknad högerparentes vid radslutet ')
        return 'Formeln är syntaktiskt korrekt'
    except Syntaxfel as error:
        return str(error) + printQ()




def main():
        themol = sys.stdin.readline().strip()
        if themol != "#":
            resultat = readformel(themol)
            del pairing[:]
            printQ()
            q.empty()
            print(resultat)
            main()

if __name__ == '__main__':
    main()