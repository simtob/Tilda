#uppgift 2

class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,f,t,weight=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], weight)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())


def skapaencoolgraf():
    j = {}
    k = Graph()

    swfile = open("word3.txt", "r")
    #skapar en hink av ord som skiljer sig med en bostav

    for rad in swfile:
        print(rad)
        ord = rad[:-1]
        print(ord)
        for i in range(len(ord)):
            hink = ord[:i] + "_" + ord[i+1:]
            if hink in j:
                j[hink].append(ord)
            else:
                j[hink] = [ord]

    for hink in j.keys():
        for ord1 in j[hink]:
            for ord2 in j[hink]:
                if ord1 != ord2:
                    k.addEdge(ord1,ord2)

    return k

skapaencoolgraf()