import timeit
from Lab3useLab6 import Bintree

filename = "unique_tracks.txt"

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
	"""Koden än från föreläsning 3"""
	"""Vi Söker i "listan" efter "nyckel" dvs (name_of_artist). Returnerar True om den hittas, False annars"""
	"""Den räknar ut vart middle är och avgör vänster eller höger. Sedan fortsätter den så tills den hittar nyckeln eller nyckeln inte finns"""

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

def mergesort(our_list):
    """Tagen från föreläsning 9, avnänvds för att jämföra med Bubblesort"""
    if len(our_list) > 1:
        middle = len(our_list)//2
        leftSide = our_list[:middle]
        rightSide = our_list[middle:]

        mergesort(leftSide)
        mergesort(rightSide)

        i, j, k = 0, 0, 0

        while i < len(leftSide) and j < len(rightSide):
            if leftSide[i] < rightSide[j]:
                our_list[k] = leftSide[i]
                i = i + 1
            else:
                our_list[k] = rightSide[j]
                j = j + 1
            k = k + 1

        while i < len(leftSide):
            our_list[k] = leftSide[i]
            i = i + 1
            k = k + 1

        while j < len(rightSide):
            our_list[k] = rightSide[j]
            j = j + 1
            k = k + 1


def bubblesort(our_list):
    # Den yttre loopen har hand om antalet passeringeringar för att kunna sortera
    # Antalet passeirngar som krävs är längden av listan minus 1
    # Den första loopen ska flytta bubblan längs med listan
    #Kopierad från en tidigare labboration vi hade i ProgTeknik från Våren.
    for i in range(0, len(our_list) - 1):
        for j in range(0, len(our_list) - 1 - i):
            if our_list[j] > our_list[j + 1]:
                our_list[j], our_list[j + 1] = our_list[j + 1], our_list[j]
    return our_list


def main():
    storLista, obj_dict, obj_bintree = read_file(filename)
    mindreLista = storLista[0:500000]

    n = len(mindreLista)
    print("Antal element =", n)

    last = mindreLista[n-1]
    testartist = last.artistname

    mergesorttimer = timeit.timeit(stmt=lambda: mergesort(mindreLista), number=10)
    print("Mergesort tog", round(mergesorttimer, 4), "sekunder")

    bubbletimer = timeit.timeit(stmt=lambda: bubblesort(mindreLista), number =10)
    print("Bubblesortering tog", round(bubbletimer, 4), "sekunder")

    linjtid = timeit.timeit(stmt = lambda: linsok(mindreLista, testartist), number = 10)
    print("Linjärsökningen tog", round(linjtid, 4), "sekunder")

    dicttime = timeit.timeit(stmt = lambda: obj_dict[testartist], number = 10)
    print("Hashsökning tog", round(dicttime, 4) , "sekunder")

    #Sorterar med hjälp av inbyggd funktion
    sorted_list = (sorted(storLista, key=lambda item: item.artistname))
    bintime = timeit.timeit(stmt = lambda:  binsearch(sorted_list, testartist) , number = 10)
    print("Binärsökning i sorterad lista tog", round(bintime, 4) , "sekunder")

"""

Sökning:
	        n = 250 000	 n = 500 000	n = 1 000 000
Linjärsökning	0.3846s	0.7152s	    1,3s
Binärsökning	 0.0s	0.0s	   0,0s
Sökning i Hashtabell 0.0001s	0.0001s	0.0006s

Tidsenhet = sekunder

Sortering:
	    n = 250 000	 n = 500 000  n = 1 000 000
Bubbelsort	37.3594	  84.0401s	  
Mergesort	35.6482	   

Tidskomplexitet:
	• Linjär: O(n)
	• Binär: O(log*n)
	• Hashtabell sökning: O(1)

Tidskomplextitet:
	• Bubblesort: O(n^2)
	• Mergesort: O(n*logn)

"""



if __name__ == '__main__':
    main()