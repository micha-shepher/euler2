__author__ = 'mshepher'

class Euler59(object):
    def __init__(self):
        self.code = None
        self.common = ['the', 'is', 'to', 'of', 'and', 'Gospel', 'John']
        with open('p059_cipher.txt') as f:
            self.code = [int(i) for i in f.readlines()[0].strip().split(',')]

    def gen(self):
        r = range(ord('a'), ord('z')+1)
        print(r, len(r))
        for i in r:
            for j in r:
                for k in r:
                    yield (i, j, k)

    def decypher(self, key):
        res = list()
        for i, j in enumerate(self.code):
            res.append(chr(j ^ key[i % 3]))
        return ''.join(res)

    def find_words(self, res):
        yes = 0
        for i in self.common:
            if i in res:
                yes += 1
        return yes


if __name__ == '__main__':
    e = Euler59()
    #for i in e.gen():
    #    res = e.decypher(i)
    #    if e.find_words(res)>=5:
    #        print(res)
    #        print('found ', i)

    res = e.decypher((103, 111, 100))  # key = god
    s = sum(ord(c) for c in res)
    print(res)
    print(s)