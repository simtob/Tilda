import timeit
from Lab3useLab6 import Bintree

class Song:
    def __init__(self, trackid, songid, artistname, songtitle):
        self.trackid = trackid
        self.songid = songid
        self.artistname = artistname
        self.songtitle = songtitle

    def __str__(self):
        return "TrackID: " + self.trackid + " låtid: " + self.songid + " artistname: " + self.artistname + \
               " åttitel: " + self.songtitle

    def __lt__(self, other):
        return self.artistname < other.artistname

    def find_artist(self):
        return self.artistname


def read_file(file):
    obj_list = []
    obj_dict = {}
    obj_bintree = Bintree()

    with open(file, encoding="utf8") as track_file:
        lines = track_file.readlines()
        for line in lines:
            item = line.strip().split("<SEP>")
            song = Song(item[0], item[1], item[2], item[3])
            obj_list.append(song)
            obj_dict[song.artistname] = song #den sista artisten ligger på denna plats
            obj_bintree.put(song.artistname)
            #-Varför blir linj sökning mindre efter varje anropp?

    return obj_list, obj_dict, obj_bintree

def linsok(our_list, name_of_artist):
    for item in our_list:
        if item == name_of_artist: #Söker efter artistnamn, om artistnamn är den sökta artisten returnerar true
            return True

def binsearch(our_list, name_of_artist):
	"""Från föreläsning 3"""
	"""Söker i "listan" efter "nyckel" dvs (name_of_artist). Returnerar True om den hittas, False annars"""
	"""Den räknar ut vart mitten är och avgör vänster eller höger. Sedan fortsätter den så tills den hittar nyckeln eller nyckeln inte finns"""

	left = 0
	right = len(our_list)-1
	found = False

	while left <= right and not found:
		mid = (left + right)//2
		if our_list[mid].artistname == name_of_artist:
			found = True
		else:
			if name_of_artist < our_list[mid].artistname:
				right = mid-1
			else:
				left = mid+1
	return found


def main():
    filename = "unique_tracks.txt"

    lista, obj_dict, obj_bintree = read_file(filename)
    n = len(lista)
    print("Antal element =", n)

    last = lista[n-1]
    testartist = last.artistname

    linjtid = timeit.timeit(stmt = lambda: linsok(lista, testartist), number = 10)
    print("Linjärsökningen tog", round(linjtid, 4), "sekunder")

    dicttime = timeit.timeit(stmt = lambda: obj_dict[testartist], number = 10)
    print("Hashsökning (Dictionary) tog", round(dicttime, 10) , "sekunder")

    #Sorterar med hjälp av inbyggd funktion
    sorted_list = (sorted(lista, key=lambda x: x.artistname))
    bintime = timeit.timeit(stmt = lambda:  binsearch(sorted_list, testartist) , number = 10)
    print("Binärsökning i sorterad lista tog", round(bintime, 4) , "sekunder")



if __name__ == '__main__':
    main()