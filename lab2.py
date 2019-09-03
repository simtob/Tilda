from array import array

class ArrayQ():

    def __init__(self):
        self.__data = array("i") #sign for int

    def isEmpty(self):
        return self.__data == array("i")

    def enqueue(self, item):
        self.__data.insert(0, item)

    def dequeue(self):
        return self.__data.pop()

    def size(self):
        return(len(self.__data))


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
    cardNumb = [int(x) for x in input("Ange kort: ").split()]
    for i in cardNumb:
        q.enqueue(i)
    print("kort i rätt ordning: ")

    while not q.isEmpty():
        cardNumb[0] = q.dequeue()
        q.enqueue(cardNumb[0])
        print(q.dequeue(), end=" ")

cardTrick()







