from arrayQFile import ArrayQ

q = ArrayQ()
q.enqueue(1)
q.enqueue(2)
x = q.dequeue()
y = q.dequeue()
if (x == 1 and y == 2):
    print("OK")
else:
    print("FAILED")

#Uppgift 3 och 4
#Skilland på privata och inte privata attribut?

def cardTrick():
    q = ArrayQ()
    cardDeck = [int(x) for x in input("Ange kort: ").split()]
    for card in cardDeck:
        q.enqueue(card)

    while not q.isEmpty():
        cardDeck[0] = q.dequeue()
        q.enqueue(cardDeck[0])
        print(q.dequeue(), end=" ") #printar ut korten i rätt ordning

if __name__ == "__main__":
    cardTrick()

#Uppgift 5:






