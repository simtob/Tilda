

class Empty(Exception):
    pass



class ArrayQ():

    def __init__(self):
        self.data = []

    def isEmpty(self):
        return self.data == []

    def enqueue(self, item):
        self.data.insert(0, item)

    def dequeue(self):
        return self.data.pop()

    def size(self):
        return(len(self.data))

"""
q = ArrayQ()
q.enqueue(1)
q.enqueue(2)
x = q.dequeue()
y = q.dequeue()
if (x == 1 and y == 2):
    print("OK")
else:
    print("FAILED")
"""

class ArrayQ():

    def __init__(self):
        self._item = [] #Detta blir en lista då vi inte har arrays i phython. Använder alltså lista för att implemetera arrays.
        self._size = 0
        self._fronten = 0

    def __len(self):
        return self._size

    def push(self, elemnt): #elemnt är argumentet
        self._item.append(elemnt)

    def pop(self):
        if self.isEmpty():
            raise Empty("Stack är tom")
        return self._item.pop()

    def top(self):
        if self.isEmpty():
            raise Empty("Stack är tom")
        return self._item[-1]

    def enqueue(self, element):
        self._item.append(element)
        self._size = self._size + 1

    def enqueue_front(self):
        if self.isEmpty():
            raise Empty("Tom")
        z = self._item[self._fronten]
        self._item[self._fronten] = self._item.append(self._fronten)
        self._fronten = self._fronten + 1
        self._size = self._size + 1
        return z

    def dequeue(self):
        if self.isEmpty():
            raise Empty ("Tom")
        v = self._item[self._fronten]
        self._item[self._fronten] = None
        self._fronten = self._fronten + 1
        self._size = self._size - 1
        return v



q = ArrayQ()
q.enqueue(1)
q.enqueue(2)
x = q.dequeue()
y = q.dequeue()
if (x == 1 and y == 2):
    print("OK")
else:
    print("FAILED")

nummerlista = input('listan med kortnummer: ')

korten = [int(x) for x in str(nummerlista)]

v = ArrayQ()
v.enqueue(korten[0])
v.enqueue(korten[1])
v.enqueue(korten[2])
v.enqueue(korten[3])
v.enqueue(korten[4])

print ("stack:", v._item)

v.enqueue_front()

x = v.dequeue()

v.enqueue_front()

y = v.dequeue()

v.enqueue_front()







print ("stack:", v._item)

print(x, y)

















