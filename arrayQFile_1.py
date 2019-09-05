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


    def dequeue(self):
        if self.isEmpty():
            raise Empty ("Tom")
        v = self._item[self._fronten]
        self._item[self._fronten] = None
        self._fronten = self._fronten + 1
        self._size = self._size - 1
        return v

    def first_delete(self):
        value = self._item.pop(self._fronten)
        return value

    def insert_item(self, index, objectt):
        self._item.insert(index, objectt)

    def remove_first(self, xobj):
        self._item.remove(xobj)

q = ArrayQ()
q.enqueue(1)
q.enqueue(2)
print(q._item)
q.insert_item(1, 76)
print(q._item)
q.remove_first(1)
print(q._item)





