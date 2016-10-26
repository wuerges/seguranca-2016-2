import cifras2016


def pattern(text):
    i = 0
    d = {}
    for c in text:
        if not c in d:
            d[c] = i
            i += 1
        yield d[c]

def frequency(n, text):
    d = {}
    for i in range(len(text) - n):
        k = text[i:i+n]
        if not k in d:
            d[k] = 0
        else:
            d[k] = 1
    for k in d:
        d[k] = float(d[k]) / (len(text) - n)
    return d


class WMap:
    def __init__(self):
        self.d = {}

    def __setitem__(self, a, b):
        if a in self.d:
            if b in self.d[a]:
                self.d[a][b] += 1
            else:
                self.d[a][b] = 1
        else:
            self.d[a] = {b:1}

    def __repr__(self):
        return "WMap" + repr(self.d)



def mixMaps(map1, map2, d):
    def mkl(m):
        l = list(m.items())
        l.sort(key=lambda e: e[1])
        l.reverse()
        return l
    l1 = mkl(map1)
    l2 = mkl(map2)

    for ((k1,_),(k2,_)) in zip(l1, l2):
        for (a, b) in zip(k1, k2):
            d[a] = b

    return d

