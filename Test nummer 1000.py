class Queue:

    def __init__(self):
       self.first = None
       self.last = None

    def enqueue(self,x):
        """Stoppar in x sist i kön """
        ny = Node(x)
        if self.first == None:
            ny.next = self.first
                                # Om kön är tom blir det på ett sätt...                           # ...som du får tänka ut själv.
        else:                   # Annars blir det på ett annat sätt..
            ny.next = self.last          # ...som du också får lura ut själv.

    def dequeue(self):
        x = self.first.data
        self.first = self.first.next
        return x

    def isEmpty(self):
        """Returnerar True om kön är tom, False annars """
        if self.first == 0:
            return True
        else:
            return False

myQueue = Queue()
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def makeQueue():
    for i in lista:
        myQueue.enqueue(i)
        print("Lista: " + str(i))
    print(lista)
    return myQueue

makeQueue()

def cardTrick():
    newQueue = Queue()
    if not myQueue.isEmpty():
        for i in range(0,12):
            i = myQueue.dequeue()
            newQueue.enqueue(i)
            second = myQueue.dequeue()
            myQueue.enqueue(second)
            print(newQueue)

cardTrick()
