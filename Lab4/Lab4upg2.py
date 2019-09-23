from linkedQfilen import LinkedQ
from Lab3use import Bintree

q = LinkedQ()

def makechildren(start_ordet, slut_ordet):
    svenska = Bintree()
    gamla = Bintree()
    with open("word3.txt", "r", encoding = "utf-8") as svenskfil:
        for rad in svenskfil:
            ordet = rad.strip()
            q.enqueue(ordet)
            counter = 0

            for i in range(len(start_ordet)):
                if ordet[i] != start_ordet[i]:
                    counter += 1
                if counter > 1:
                    break

            if counter == 1:
                barn = ordet
                if barn not in svenska:
                    svenska.put(barn)
                if barn not in gamla:
                    gamla.put(barn)
                    q.enqueue(barn)
                    while not q.isEmpty():
                        nod = q.dequeue()
                        makechildren(nod, q)
                        if ordet == slut_ordet:
                            print("Hittat en väg från")



makechildren(input(str("ange start ord: ")), input(str("slut ord: ")))



