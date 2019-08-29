from array import array

class ArrayQ(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()


q = ArrayQ()
q.enqueue(1)
q.enqueue(2)
x = q.dequeue()
y = q.dequeue()
if (x == 1 and y == 2):
    print("OK")
else:
    print("FAILED")



nummer = input("Nummer: ")
korten = nummer.split()

class ArrayKort(object):

    def __init__(self):
        self.kortnummer = korten

    def isEmpty(self):
        return self.kortnummer == korten

    def enqueue(self, korten):
        self.kortnummer.insert(0, korten)

    def dequeue(self):
        return self.kortnummer.pop()


for i in korten:
    v = ArrayKort()
    x = v.dequeue()
    v.enqueue(x)

print(x)
