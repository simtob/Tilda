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

def hotPotato(namelist, num):
    simqueue = ArrayQ()
    for name in namelist:
        simqueue.enqueue(name)
        print(name)

    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())

        simqueue.dequeue()

    return simqueue.dequeue()

print(hotPotato([1,2,3,4,5,6,7,8,9,10,11,12,13],1))



