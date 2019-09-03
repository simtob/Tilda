

class Empty(Exception):
    pass


class ArrayQ():

    def __init__(self):
        self._item = [] #Detta blir en lista då vi inte har arrays i phython. Använder alltså lista för att implemetera arrays.
        self._size = 0
        self._fronten = 0

    def __len(self):
        return self._size

    def isEmpty(self):
        return self._size == 0

    def top(self):
        if self.isEmpty():
            raise Empty("Stack är tom")
        return self._item[-1]

    def enqueue(self, element):
        self._item.append(element)
        self._size = self._size + 1

    def dequeue(self):
        if self.isEmpty():
            raise Empty ("Tom")
        v = self._item[self._fronten] #v (kortet) blir första platsen i vår lista
        self._item[self._fronten] = None #gör om den som är först i kön till None
        self._fronten = self._fronten + 1 #fronten går över till kortet efter det första.
        self._size = self._size - 1 #kön minskas då vi lagt ut ett kort
        return v #det som dequeueats

    def first_delete(self):
        value = self._item.pop(self._fronten) #Platsen som blivit till none tas bort.
        return value

q = ArrayQ()
q.enqueue(1)
q.enqueue(2)
x = q.dequeue()
y = q.dequeue()
if (x == 1 and y == 2):
    print("OK")
else:
    print("FAILED")









x, y, z, e, r = [int(x) for x in input("skriv in 5 kort med mellanrum: ").split()]


v = ArrayQ()
v.enqueue(x)
v.enqueue(y)
v.enqueue(z)
v.enqueue(e)
v.enqueue(r)


print ("stack:", v._item)

v.enqueue(x)
v.first_delete()
l = v.dequeue()


v.enqueue(y)
v.first_delete()
m = v.dequeue()

v.enqueue(z)
v.first_delete()
z = v.dequeue()

v.enqueue(e)
v.first_delete()
h = v.dequeue()

v.enqueue(r)
v.first_delete()
g = v.dequeue()




print("stack:", v._item)

print(l, m, z, h, g)



















