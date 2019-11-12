KAPACITET = 500


class Node:  # Själva verket en node datastruktor, som en linkedlist node
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.nesta = None


class Hashtabell:
    # initisiserar en hash tabell
    def __init__(self, size):
        self.size = size
        self.kapasitet = KAPACITET
        self.luckor = [None] * self.kapasitet
        self.krockantal = 0

    def store(self, key, data):
        # steg 1 blir att öka storleken
        self.size += 1
        # steg 2 blir att beräkna index av key
        index = self.hashfunction(key)

        node = self.luckor[index]  # går till noden

        # om luckan är tom så skapas ny node och retunerar
        if node is None:
            self.luckor[index] = Node(key, data)
            return

        # annars gå igenomen länkade listan på given index, sedan lägg till ny node på slutet av listan
        tidigare = node
        while node is not None:
            tidigare = node
            node = node.nesta

        tidigare.nesta = Node(key, data)

    def search(self, key):
        index = self.hashfunction(key)
        currNode = self.luckor[index]

        while currNode != None:
            if currNode.key == key:
                return currNode
            currNode = currNode.nesta



    def put(self, key, value):
        index = self.hashfunction(key)
        if self.luckor[index] == None:
            self.luckor[index] = Node(key, value)
        else:
            self.krockantal += 1
            krock = self.luckor[index]
            self.luckor[index] = Node(key, value)
            self.luckor[index].next = krock

    def hashfunction(self, key):
        hashsumman = 0
        for i, c in enumerate(key):  # för varje karaktär i key
            hashsumman += (i + len(key)) ** ord(c)  # lägger till index ? längden av key upphöjt till nuvarnde char Node
            hashsumman = hashsumman % self.size
        return hashsumman