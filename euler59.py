__author__ = 'mshepher'

class Euler59(object):
    def __init__(self):
        self.code = None
        with open('p059_cipher.txt') as f:
            self.code = [int(i) for i in f.readlines()[0].strip().split(',')]
        print(self.code)

    def gen(self):
        r = range(ord('a'), ord('z')+1)
        print(r, len(r))
        for i in r:
            for j in r:
                for k in r:
                    yield (i, j, k)

    def decypher(self):
        pass

    def find_words(self):
        pass


if __name__ == '__main__':
    e = Euler59()
    for e in e.gen():
        print(e)