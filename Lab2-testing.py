from array import array

class ArrayQ():

    def __init__(self):
        self.data = []

    def __str__(self):
        return str(self.data)

    def isEmpty(self):
        return self.data == []

    def enqueue(self, item):
        self.data.insert(0, item)

    def dequeue(self):
        return self.data.pop()


q = ArrayQ()
q.enqueue(1)
q.enqueue(2)
x = q.dequeue()
y = q.dequeue()
if (x == 1 and y == 2):
    print("OK")
else:
    print("FAILED")

z = ArrayQ()
for i in range(1,14):
    z.enqueue(i)
print(z)


while not z.isEmpty():
    card = z.dequeue()
    z.enqueue(card)


