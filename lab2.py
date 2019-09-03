from array import array

class ArrayQ():

    def __init__(self):
        self.data = array("i") #sign for int

    def isEmpty(self):
        return self.data == array("i")

    def enqueue(self, item):
        self.data.insert(0, item)

    def dequeue(self):
        return self.data.pop()

    def size(self):
        return(len(self.data))


q = ArrayQ()
q.enqueue(1)
q.enqueue(2)
x = q.dequeue()
y = q.dequeue()
if (x == 1 and y == 2):
    print("OK")
else:
    print("FAILED")


def cardTrick():
    q = ArrayQ()
    while not q.isEmpty():
        cardInput = [int(x) for x in input("Ange kort: ").split()]
        for x in cardInput:
            q.enqueue(x)
        print(x)

cardTrick()






