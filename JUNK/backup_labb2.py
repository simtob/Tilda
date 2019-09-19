class Empty(Exception):
    pass

class LinkedQ():

    class _Node:
        __slots__ = "_elemnt", "_nesta"

        def __init__(self, elemnt, nesta):
                self._elemnt = elemnt
                self._nesta = nesta

    def __init__(self):
        self._first = None
        self._last = None
        self._storlek = 0

    def __len__(self):
        return self._storlek

    def isEmpty(self):
        return self._storlek == 0


    def enqueue(self, element):
        ny = self._Node(element, None)
        if self.isEmpty():
            self._first = ny
            self._last = ny
        else:
            self._last._nesta = ny
        self._last = ny
        self._storlek += 1

    def dequeue(self):
        if self.isEmpty():
            raise Empty ("Tom")
        varde = self._first._elemnt
        self._first = self._first._nesta
        self._storlek -= 1
        if self.isEmpty():
            self._last = None
        return varde

class LinkedQ():

    class _Node:
        __slots__ = "_elemnt", "_nesta"

        def __init__(self, elemnt, nesta):
                self._elemnt = elemnt
                self._nesta = nesta

    def __init__(self):
        self._first = None
        self._last = None
        self._storlek = 0

    def __len__(self):
        return self._storlek

    def isEmpty(self):
        return self._storlek == 0

    def plus_first(self, element):
        ny = self._Node(element, None)
        if self.isEmpty():
            self._first = ny
            self._last = ny
        else:
            ny._nesta = self._first
        self._first = ny
        self._storlek += 1

    def enqueue(self, element):
        ny = self._Node(element, None)
        if self.isEmpty():
            self._first = ny
            self._last = ny
        else:
            self._last._nesta = ny
        self._last = ny
        self._storlek += 1

    def dequeue(self):
        if self.isEmpty():
            raise Empty ("Tom")
        varde = self._first._elemnt
        self._first = self._first._nesta
        self._storlek -= 1
        if self.isEmpty():
            self._last = None
        return varde

    def radera_last(self):
        if self.isEmpty():
            raise Empty("Tom")
        tempfirst = self._first
        i=0
        while i < len(self) - 2:
            tempfirst = tempfirst._nesta
            i+=1
            self._first = tempfirst
            tempfirst = tempfirst._nesta
            varde = tempfirst._elemnt
            self._last._nesta = None
            self._storlek -= 1
            return varde

    def visa(self):
        tempfirst = self._first
        while tempfirst:
            print(tempfirst._elemnt, end="->")
            tempfirst = tempfirst._nesta
        print()
