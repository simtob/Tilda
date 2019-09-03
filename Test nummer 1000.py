class Node:

   def __init__(self, x, next = None):
      self.data = x
      self.next = next

class Queue:

    def __init__(self):
       self.first = None
       self.last = None

    def enqueue(self,x):
        """Stoppar in x sist i kön """
        ny = Node(x)
        if self.first == None:
            ny.next = self.first
                                # Om kön är tom blir det på ett sätt...                           # ...som du får tänka ut själv.
        else:                   # Annars blir det på ett annat sätt..
            ny.next = self.last                 # ...som du också får lura ut själv.

    def dequeue(self):
        """Plockar ut och returnerar det som står först i kön """
        x = self.first.data
        self.first = self.first.next
        self.first.pop()
        return x


    def isEmpty(self):
        """Returnerar True om kön är tom, False annars """
        if self.first == 0:
            return True
        else:
            return False

class Stack:

   def __init__(self):
      self.top = None

   def push(self,x):
      """Lägger x överst på stacken """
      ny = Node(x)
      ny.next = self.top
      self.top = ny

   def pop(self):
      """Plockar ut och returnerar det översta elementet """
      x = self.top.data
      self.top = self.top.next
      return x

   def isEmpty(self):
      """Returnerar True om stacken är tom, False annars"""
      if self.top == None:
         return True
      else:
         return False



