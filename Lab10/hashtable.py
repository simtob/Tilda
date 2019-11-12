class HashNode:
	def __init__(self, key, value, next = None):
		self.key = key
		self.value = value
		self.next = next

	def __str__(self):
		if self.key != None and self.value != None:
			return "key = " + str(self.key) + " and value = " + str(self.value)
		else:
			return None

class Hashtabell:

    def __init__(self, size):
        """size: hashtabellens storlek"""
        self.dictionary = {}
        self.size = size

    def store(self, key, data):
        """key: nyckeln
           data: objektet som ska lagras
           Stoppar in "data" med nyckeln "key" i tabellen."""
        self.dictionary[key] = data

    def search(self, key):
        """key: nyckeln
           Hamtar det objekt som finns lagrat med nyckeln "key" och returnerar det.
           Om "key" inte finns ska vi få en Exception, KeyError """
        try:
            print("Data: ", self.dictionary[key])
            return key
        except KeyError:
                print("Wrong key")


def hashfunction(key):
    """key: nyckeln
    Beräknar hashfunktionen för key"""
    result = 0
    for c in key:
        result = result * 15 + ord(c)  # The ord() method takes a single parameter c,
        # where c is character string of length 1
        # and and returns an integer representing the Unicode code point of the character.
    print(result%len(key))
    return result % len(key)

class DictHash:
    def __init__(self):
        self.dictionary = {}
    def store(self, nyckel, data):
        self.dictionary[nyckel] = data
    def search(self, nyckel):
        try:
            print("Data: ", self.dictionary[nyckel])
        except KeyError:
            print("Wrong key")

def storeArtist(a):

	with open("unique_tracks.txt", "r", encoding = "ISO-8859-1") as fil:
		for rad in fil:
			attr = rad.split('<SEP>')
			a.put(attr[0], attr[3])


def main():
	a = Hashtabell(1000000)
	storeArtist(a)
	print(a.search("TRMMJXK128F93315E9"))
	print("Antal krockar:", a.krockantal)

if __name__ == "__main__":
    main()