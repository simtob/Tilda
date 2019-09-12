
from lab7pokemon import Pokemon



class Node:

   def __init__(self, key = "key", data = None):
      """key: keyn som anvands vid hashningen
      data: det objekt som ska hashas in"""
      self.key = key
      self.data = data


class Hashtable(object):

    def __init__(self, size):
        self.size = size
        self.luckor = [None] * self.size
        self.data = [None] * self.size

    def store(self, key, data):
        hashvarde = self.hashfunction(key,len(self.luckor))

        if self.luckor[hashvarde] == None:
            self.luckor[hashvarde] = key
            self.data[hashvarde] = data

        else:

            if self.luckor[hashvarde] == key:
                self.data[hashvarde] = data

            else:

                nestalucka = self.goraom_hachen(hashvarde,len(self.luckor))

                while self.luckor[nestalucka] != None and self.luckor[nestalucka] != key:
                    nestalucka = self.goraom_hachen(nestalucka,len(self.luckor))

                if self.luckor[nestalucka] == None:
                    self.luckor[nestalucka] = key
                    self.data[nestalucka] = data

                else:
                    self.data[nestalucka] = data





    def hashfunction(self,key,size):
        #själva hash funktionen
        return key % size

    def goraom_hachen(self, gamlahashen, size):
        return (gamlahashen+1)%size


    def search(self, key):

        startluckan = self.hashfunction(key,len(self.luckor))
        data = None
        stoppa = False
        hittad = False
        positionen = startluckan

        while self.luckor[positionen] != None and not hittad and not stoppa:

            if self.luckor[positionen] == key:
                hittad = True
                data = self.data[positionen]

            else:
                positionen = self.goraom_hachen(positionen,len(self.luckor))
                if positionen == startluckan:

                    stoppa = True

        return data

    def __getitem__(self, key):
        return self.search(key)

    def __setitem__(self,key,data):
        self.store(key,data)


x = Hashtable(4)

x[1] = "one"

x[2] = "two"

print(x[1])

def mainss():
   with open("pokemons.csv", encoding = "utf8") as file:
       #file.readline() #för att skippa header
       for i, line in enumerate(file):
           if i == 2:
               attributes = line.strip().split(",")
               Pokemon(attributes[0], attributes[1], attributes[2], attributes[3], attributes[4], attributes[5],
                                 attributes[6], attributes[7], attributes[8], attributes[9], attributes[10], attributes[11],
                                 attributes[12])

               x = Hashtable(1000)
               x[1] = attributes[0]
               print(x[1])






mainss()





