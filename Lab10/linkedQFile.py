class Node:
	"""Skapar ett simpelt nod-objekt med ett värde och en next-pekare"""
	def __init__(self, value):
		self.value = value
		self.next = None
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

    def restart(self):
        self._first = None
        self._last = None


    def peek(self):
        if not self.isEmpty():
            return self._first.value
        else:
            return None
