from linkedQfilen import LinkedQ
from Lab3use import Bintree

q = LinkedQ()
#Hämta alla ord från filen och stoppa in i binärträd, sen när du genererar ord för de här tre ord bokstävena,
# titta om det existerar i vårt binärt träd

def read_file():
    svenska = Bintree()
    with open("word3.txt", "r", encoding = "utf-8") as svenskfil:
        for rad in svenskfil:
            ordet = rad.strip()
            svenska.put(ordet)
    return svenska




def makechildren(start_ordet, q, svenska, gamla):

    alphabet = "abcdefghijklmnopqsrtuvwxyzåäö"
    for i in range(len(start_ordet)):
        barn = start_ordet
        barn = list(barn) #skapar list för att enkelt byta ut bokstaven

        for letter in alphabet:
            if letter != barn[i]:
                barn[i] = letter #ersätter första förekomsten av barn av [i]
                barn_str = "".join(barn) #joinar listan till en sträng, med avseende på en avskiljare i vårt fall ""
                if barn_str in svenska and barn_str not in gamla:
                    gamla.put(barn_str)
                    q.enqueue(barn_str)




def main():
    start_ordet = str(input("ange startord: "))
    slut_ordet = str(input("ange slutord: "))
    q.enqueue(start_ordet)

    svenska = read_file()
    gamla = Bintree()
    gamla.put(start_ordet)

    while not q.isEmpty():
        nod = q.dequeue()
        makechildren(nod, q, svenska, gamla)
        if nod == slut_ordet:
            print("Hittat en väg till", slut_ordet)


main()

