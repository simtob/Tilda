from array import array

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
class Queue:

    def __init__(self):
       self.first = None
       self.last = None
       self._queue = []
       self.size = 0

    def enqueue(self,x):
        """Stoppar in x sist i kön """
        self.size += 1
        if self.first == None:
            x = self.last
            print(x)
            return x

    def dequeue(self):
        """Plockar ut och returnerar det som står först i kön """
        x = self.first
        self.first = self.first.next
        return x

    def isEmpty(self):
        """Returnerar True om kön är tom, False annars """
        if self._queue == 0:
            print("Tom kö...")
            return self._queue==0

class Node:

   def __init__(self, x, next = None):
      self.data = x
      self.next = next

def hotPotato():
    namelist = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)
        print(name)

    while simqueue != 0:
        for i in range(13):
            simqueue.enqueue(simqueue.dequeue())
        simqueue.dequeue()

    return simqueue.dequeue()

hotPotato()



