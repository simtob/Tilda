from array import array

class LinkedQ():

    def __init__(self):
        self._first = None
        self._last = None
        self.__data = array("i")  # sign for int

    def isEmpty(self):
        if self._first == None:
            return True
        else:
            return False


    def enqueue(self, x):
        new = Node(x,)
        if self.isEmpty():
            self._first = new
            self._last = new
        else:
            self._last.next = new
        self._last = new

    def dequeue(self):
        x = self._first.value
        self._first = self._first.next
        return x

    def size(self):
        return (len(self.__data))


class Node:

   def __init__(self, x, next = None):
      self.value = x
      self.next = next