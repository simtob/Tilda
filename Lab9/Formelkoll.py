from sys import stdin


class Syntaxfel(Exception):
    pass


class Toosmall(Exception):
    pass


class LinkedStack:
    def __init__(self):
        self.top = None

    def push(self, x):
        """Lägger x överst på stacken """
        ny = Stack_Node(x)
        ny.next = self.top
        self.top = ny

    def pop(self):
        """Plockar ut och returnerar det översta elementet """
        x = self.top.data
        self.top = self.top.next
        return x

    def isEmpty(self):
        """Returnerar True om stacken är tom, False annars"""
        if self.top is None:
            return True
        else:
            return False


class Stack_Node:
    def __init__(self, x, next=None):
        self.data = x
        self.next = next


class Node:
    # Definierar objekt med två attribut, dess data och pekare på nästa nod
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return self.data


class LinkedQ:
    # den länkade listan definieras med denna klass. De enda attributen är den första och den sista noden.
    def __init__(self):
        self.__first = None
        self.__last = None

    def enqueue(self, x):
        """Stoppar in x sist i kön """
        ny = Node(x)
        if self.__first is None:
            self.__first = ny
            self.__last = ny

        else:
            self.__last.next = ny
            self.__last = ny

    def dequeue(self):
        removed_element = self.__first.data
        self.__first = self.__first.next
        if self.__first is None:
            self.__last = None
        return removed_element

    def isEmpty(self):
        if self.__first is None:
            return True
        else:
            return False

    def size(self):
        size_number = 0
        copy_start = self.__first
        if self.__first is not None:
            while copy_start is not None:
                size_number += 1
                copy_start = copy_start.next

        return size_number

    def peek(self):
        if self.__first is None:
            return
        else:
            copy_start = self.__first
            return copy_start.data

    def peekNum(self):
        if self.__first.next is None:
            return
        else:
            copy_start = self.__first.next
            return copy_start.data

    def flush(self):
        str = ""
        while not self.isEmpty():
            str += self.dequeue()
        return str


sign_stack = LinkedStack()


def readnumber(q):
    if q.peek() == str(0) or (q.peek() == str(1) and q.peekNum() is not None):
        try:
            int(q.peekNum())
        except ValueError:
            raise Toosmall("För litet tal")
        except TypeError:
            raise Toosmall("För litet tal")
    if q.peek() == str(0) or (q.peek() == str(1) and q.peekNum() is None):
            raise Toosmall("För litet tal")
    try:
        int(q.peek())
        q.dequeue()
    except ValueError:
        raise Syntaxfel("Saknad siffra")
    except TypeError:
        raise Syntaxfel("Saknad siffra")
    try:
        while q.peek() is not None:
            int(q.peek())
            q.dequeue()
    except ValueError:
        raise ValueError


def readletter(input_letter):
    if type(input_letter) is str and input_letter.islower():
        return
    else:
        raise Syntaxfel


def read_cap_letter(input_cap):
    if type(input_cap) is str and input_cap.isupper():
        return
    else:
        try:
            int(input_cap)
            raise Syntaxfel("Felaktig gruppstart")
        except ValueError:
            if input_cap.islower():
                raise Syntaxfel("Saknad stor bokstav")
            else:
                if input_cap == ")" and sign_stack.isEmpty() is False:
                    sign_stack.pop()
                    return
                raise Syntaxfel("Felaktig gruppstart")


def readatom(q):
    atom_string = ""
    read_cap_letter(q.peek())
    atom_string += q.dequeue()
    try:
        readletter(q.peek())
        atom_string += q.dequeue()
    except Syntaxfel:
        if atom_string == ")":
            return
        if atom_string not in valid_atoms:
            raise Syntaxfel("Okänd atom")
        return
    if atom_string not in valid_atoms:
        raise Syntaxfel("Okänd atom")


def readformula(input_string):
    letterque = LinkedQ()
    if sign_stack.isEmpty() is False:
        sign_stack.pop()
    try:
        if len(input_string) < 2:
            raise Syntaxfel("För kort input")
        for letter in input_string:
            if letter is "\n":
                break

            letterque.enqueue(letter)

        readmol(letterque)
        if sign_stack.isEmpty() is False:
            sign_stack.pop()
            raise Syntaxfel("Saknad högerparentes")

    except Syntaxfel as error:
        raise Syntaxfel(str(error) + " vid radslutet " + letterque.flush())


def readmol(q):
    readgroup(q)

    if q.isEmpty():
        return
    elif q.peek() is ")":
        if sign_stack.isEmpty() is True:
            raise Syntaxfel("Felaktig gruppstart")
        else:
            return

    readmol(q)


def readgroup(q):
    if q.peek() is "(":
        sign_stack.push(q.dequeue())
        if q.peek() is ")":
            raise Syntaxfel("Felaktig gruppstart")
        readmol(q)
    if q.peek() is ")":
        if sign_stack.isEmpty():
            raise Syntaxfel("Felaktig gruppstart")
        sign_stack.pop()
        q.dequeue()
        try:
            readnumber(q)
            return
        except Syntaxfel:
            raise Syntaxfel("Saknad siffra")
        except ValueError:
            readgroup(q)
        except Toosmall:
            raise Syntaxfel("För litet tal")
    if q.isEmpty() is True:
        return
    else:
        readatom(q)
        if q.isEmpty():
            return
        try:
            readnumber(q)
        except Syntaxfel:
            return
        except ValueError:
            return
        except Toosmall:
            q.dequeue()
            raise Syntaxfel("För litet tal")


valid_atoms = {
    "H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K", "Ca", "Sc",
    "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr", "Rb", "Sr", "Y", "Zr", "Nb",
    "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "I", "Xe", "Cs", "Ba", "La", "Ce", "Pr", "Nd", "Pm",
    "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl",
    "Pb", "Bi", "Po", "At", "Rn", "Fr", "Ra", "Ac", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md",
    "No", "Lr", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg", "Cn", "Fl", "Lv"
}


def main():
    for line in stdin:
        if line[:1] is "#":
            break
        try:
            readformula(line)
            print("Formeln är syntaktiskt korrekt")
        except Syntaxfel as error:
            print(error)


# main()
