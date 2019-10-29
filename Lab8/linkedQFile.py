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

    def peek(self):
        """Returnerar en kopia av nästa item i kön, utan att ta bort den.
        Nästa item är samma värde som skulle ha blivit returnerat av dequeuen operationen.
        Ett item kan inte bli dequeued från en tom kö."""
        if not self.isEmpty():
            return self._first.value
        else:
            return None
