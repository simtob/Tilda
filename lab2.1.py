import unittest

from arrayQFile_1 import ArrayQ
from linkedQFile import LinkedQ


if __name__ == "__main__":

    class Empty(Exception):
        pass


""""
class TestQueue(unittest.TestCase):

    def test_isEmpty(self):
        #isEmpty ska returnera True för tom kö, False annars
        q = LinkedQ()
        self.assertTrue(q.isEmpty(), "isEmpty på tom kö")
        q.enqueue(17)
        self.assertFalse(q.isEmpty(), "isEmpty på icke-tom kö")

    def test_order(self):
        #Kontrollerar att kö-ordningen blir rätt
        q = LinkedQ()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.dequeue(), 2)
        self.assertEqual(q.dequeue(), 3)

if __name__ == "__main__":
    unittest.main()
"""

"""q = ArrayQ()
q.enqueue(1)
q.enqueue(2)
x = q.dequeue()
y = q.dequeue()
if (x == 1 and y == 2):
    print("OK")
else:
    print("FAILED")
"""







"""
korten = [int(x) for x in input("skriv in 13 kort med mellanrum: ").split()]

print(korten)

q = ArrayQ()

temp = korten.copy()

for kort in temp:
    q.enqueue(kort)

while not q.isEmpty():
    for kort in temp:
        q.enqueue(kort)
        d = q.dequeue()
        kort = q.dequeue()
        print(kort)

"""



def cardTrick():
    q = LinkedQ()
    cardNumb = [int(x) for x in input("Ange kort: ").split()]
    for i in cardNumb:
        q.enqueue(i)
    print("kort i rätt ordning: ")

    while not q.isEmpty():
        cardNumb[0] = q.dequeue()
        q.enqueue(cardNumb[0])
        print(q.dequeue(), end=" ")

cardTrick()










#7 1 12 2 8 3 11 4 9 5 13 6 10







