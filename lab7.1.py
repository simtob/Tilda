
from lab7pokemon import Pokemon

class DictHash(object):

    def __init__(self, storlek):
        self.storlek = storlek
        self.luckor = [None] * self.storlek
        self.info = [None] * self.storlek

    def laggatill(self, nyckel, info):
        hashvarde = self.hashensfunktion(nyckel,len(self.luckor))

        if self.luckor[hashvarde] == None:
            self.luckor[hashvarde] = nyckel
            self.info[hashvarde] = info

        else:

            if self.luckor[hashvarde] == nyckel:
                self.info[hashvarde] = info

            else:

                nestalucka = self.goraom_hachen(hashvarde,len(self.luckor))

                while self.luckor[nestalucka] != None and self.luckor[nestalucka] != nyckel:
                    nestalucka = self.goraom_hachen(nestalucka,len(self.luckor))

                if self.luckor[nestalucka] == None:
                    self.luckor[nestalucka] = nyckel
                    self.info[nestalucka] = info

                else:
                    self.info[nestalucka] = info





    def hashensfunktion(self,nyckel,storlek):
        #själva hash funktionen
        return nyckel%storlek

    def goraom_hachen(self, gamlahashen, storlek):
        return (gamlahashen+1)%storlek


    def tafram(self, nyckel):

        startluckan = self.hashensfunktion(nyckel,len(self.luckor))
        info = None
        stoppa = False
        hittad = False
        positionen = startluckan

        while self.luckor[positionen] != None and not hittad and not stoppa:

            if self.luckor[positionen] == nyckel:
                hittad = True
                info = self.info[positionen]

            else:
                positionen = self.goraom_hachen(positionen,len(self.luckor))
                if positionen == startluckan:

                    stoppa = True

        return info

    def __getitem__(self, nyckel):
        return self.tafram(nyckel)

    def __setitem__(self,nyckel,info):
        self.laggatill(nyckel,info)


x = DictHash(4)

x[1] = "one"

x[2] = "two"

print(x[1])

def mainss():
   with open("pokemons.csv", encoding = "utf8") as file:
       #file.readline() #för att skippa header
       for i, line in enumerate(file):
           if i == 2:
               attributes = line.strip().split(",")
               pokemon = Pokemon(attributes[0], attributes[1], attributes[2], attributes[3], attributes[4], attributes[5],
                                 attributes[6], attributes[7], attributes[8], attributes[9], attributes[10], attributes[11],
                                 attributes[12])

               x = DictHash(1000)
               x[1] = attributes[0]
               print(x[1])






mainss()