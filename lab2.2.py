"""
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
class Node:
   def __init__(self, x, next = None):
      self.datan = x
      self.next = next


class Queue():
    def __init__(self):
       self.__queue = []
       self.__size = 0
       self.first = None
       self.last = None

    def enqueue(self,element):
        """Stoppar in x sist i kön """
        z = self.__queue.append(element)
        self.__size = self.__size + 1
        self.first = self.__queue[0]
        return z


    def dequeue(self):
        """Plockar ut och returnerar det som står först i kön """
        self.__size -= 1
        self.first = self.first.next
        self.__queue.pop()
        return self.first


    def isEmpty(self):
        """Returnerar True om kön är tom, False annars """
        return self.__queue == []




q = Queue()
q.enqueue(1)
q.enqueue(2)
x = q.dequeue()
y = q.dequeue()
if (x == 1 and y == 2):
    print("OK")
else:
    print("FAILED")

def makeQueue():
    myQueue = Queue()
    queue = 0
    while queue < 3:
        queue += 1
        numberInput = input("Input number: ")
        numberList = []
        numberList.append(int(numberInput))
        for i in numberList:
            myQueue.enqueue(i)
            print(i)
    return numberList





makeQueue()
