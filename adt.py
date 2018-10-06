# adt.py
class Eintrag:
    def __init__(self):
        self.inhalt = None
        self.next = None

class Liste:
    def __init__(self):
        self.anf = Eintrag()    
        self.pos = self.anf
       
    def empty(self):
        return self.anf.next is None
    
    def endpos(self):
        return self.pos.next is None

    def reset(self):
        self.pos = self.anf

    def advance(self):
        if self.endpos(): raise RuntimeError("Fehler: Liste am Ende")
        self.pos = self.pos.next

    def elem(self):
        if self.endpos(): raise RuntimeError("Fehler: Liste am Ende")
        return self.pos.next.inhalt
    
    # Fügt x vor das aktuelle Element ein, x wird neues aktuelles Element
    def insert(self, x):
        hilf = Eintrag()
        hilf.inhalt = x
        hilf.next = self.pos.next
        self.pos.next = hilf

    # Löscht das aktuelle Element. Der Nachfolger wird neues aktuelles Element.
    def delete(self):
        if self.endpos(): raise RuntimeError("Fehler: Liste am Ende")
        self.pos.next = self.pos.next.next

class Keller:
    def __init__(self):
        self.tp = None

    def empty(self):
        return self.tp is None

    def push(self, x):
        hilf = Eintrag()
        hilf.inhalt = x
        hilf.next = self.tp
        self.tp = hilf

    def top(self):
        if self.empty(): raise RuntimeError("Fehler: Keller ist leer")
        return self.tp.inhalt

    def pop(self):
         if self.empty(): raise RuntimeError("Fehler: Keller ist leer")
         self.tp = self.tp.next

class Schlange:
    def __init__(self):
        self.head = None
        self.tail = None

    def empty(self):
        return self.head is None

    def enq(self, x):
        if self.empty():
            self.head = Eintrag()
            self.tail = self.head
        else:
            self.tail.next = Eintrag()
            self.tail = self.tail.next
        self.tail.inhalt = x
        self.tail.next = None

    def deq(self):
         if self.empty(): raise RuntimeError("Fehler: Schlange ist leer")
         self.head = self.head.next
         if self.head is None:
             self.tail = None

    def front(self):
         if self.empty(): raise RuntimeError("Fehler: Schlange ist leer")
         return self.head.inhalt

