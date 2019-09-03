from array import array

class ArrayQ():

    def __init__(self):
        self.__data = array("i") #sign for int

    def isEmpty(self):
        return self.__data == array("i")

    def enqueue(self, item):
        self.__data.insert(0, item)

    def dequeue(self):
        return self.__data.pop()

    def size(self):
        return(len(self.__data))