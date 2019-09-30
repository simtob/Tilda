import timeit

class Enfinlat:
    def __init__(self, trackensid, lotid, artistensnamn, latenstitel):
        self.trackensid = trackensid
        self.lotid = lotid
        self.artistensnamn = artistensnamn
        self.latenstitel = latenstitel

    def __str__(self):
        return "TrackID: " + self.trackensid + " låtid: " + self.lotid + " artistnamn: " + self.artistensnamn + \
               " åttitel: " + self.latenstitel

    def __lt__(self, other):
        return self.artistensnamn < other.artistensnamn

    def tafram_artisten(self):
        return self.artistensnamn


def lasafilen(dencoolafilen):
    okjektlista = []
    objektdictianry = {}

    with open(dencoolafilen, encoding="utf8") as track_file:
        allarader = track_file.readlines()

        for rader in allarader:
            saken = rader.strip().split("<SEP>")
            song = Enfinlat(saken[0], saken[1], saken[2], saken[3])
            okjektlista.append(song)
            objektdictianry[song.artistensnamn] = song

    return okjektlista, objektdictianry


def linsok(listan, namnetpaartisten):
    hittad = False

    for saken in listan:
        if saken.artistensnamn == namnetpaartisten:
            hittad = True

    return hittad

def main():

    filename = "unique_tracks.txt"

    lista, dicten = lasafilen(filename)
    n = len(lista)
    print("Antal element =", n)

    sista = lista[n-1]
    testartist = sista.artistensnamn

    linjtid = timeit.timeit(stmt = lambda: linsok(lista, testartist), number = 10)
    print("Linjärsökningen tog", round(linjtid, 4) , "sekunder")

    dicttid = timeit.timeit(stmt=lambda: dicten[testartist], number=10)
    print("Dictsökningen tog", round(dicttid, 10), "sekunder")



if __name__ == '__main__':
    main()