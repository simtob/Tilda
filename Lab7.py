#Uppgift 1

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

q = DictHash()

def main():
   with open("pokemons.csv", encoding = "utf8") as file:
       for line in file:
           item = line.strip().split(",")
           #attributes = item[2], item[3], item[4], item[5], item[6], item[7], item[8], item[9], item[10], item[11], item[12]
           q.store(item[1], item)

main()

x = q.search("Bulbasaur")
