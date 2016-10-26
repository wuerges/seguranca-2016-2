from bitarray import *

def addprefixos(xs, p):
    return dict((k, bitarray(p) + v) for (k,v) in xs.items())

class N:
    def __init__(self, x, f):
        self.x = x
        self.f = f
        self.l = None
        self.r = None

    def join(self, o):
        n = N(None, self.f + o.f)
        n.l = self
        n.r = o
        return n

    def coding(self):
        l = {}
        r = {}
        if self.x:
            return {self.x: bitarray()}
        if self.l: 
            l = self.l.coding()
        if self.r:
            r = self.r.coding()
        ret = {}
        ret.update(addprefixos(l, '0'))
        ret.update(addprefixos(r, '1'))
        return ret

    def __lt__(self, o):
        return self.f > o.f

    def __repr__(self):
        return "N(%s,%f)" % (self.x, self.f)


a = N('a', 0.5)
b = N('b', 0.1)
c = N('c', 0.11)
d = N('d', 0.1)



j1 = a.join(b)
j2 = c.join(d)
j3 = j1.join(j2)

print("a:", a.coding())
print("b:", b.coding())
print("c:", c.coding())
print("d:", d.coding())
print("j1:", j1.coding())
print("j2:", j2.coding())
print("j3:", j3.coding())

# l = [a, b, c, d]
l = [N('a', 4), N(' ', 2), N('c', 1), N('s', 2), N('r', 1), N('o', 1)]

def huffmann(l):
    while(len(l) > 1):
        l.sort()
        a = l.pop()
        b = l.pop()
        c = a.join(b)
        l.append(c)
    return l.pop().coding()

print(huffmann(l))
