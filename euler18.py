from time import time

__author__ = 'mshepher'

class Euler18(object):
    def __init__(self):
        self.t = []
        self.base = '''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''
        for r, row in enumerate(self.base.split('\n')):
            l = list()
            for c, col in enumerate(row.split()):
                l.append(int(col))
            self.t.append(l)
        for r in self.t:
            print(r)
        self.tt = self.t[:4]
        self.teller = 0

    def search(self, r, c):
        """
        brute force recursive algo
        :param r: row
        :param c: column
        :return: greater of left or right triangles plus current
        """
        self.teller += 1
        if r == len(self.t)-1:
            return self.t[r][c]
        else:
            m = self.t[r][c] + max(self.search(r+1, c), self.search(r+1, c+1))
            return m

    def resetteller(self):
        self.teller = 0

    def smart(self, t):
        """
        smart bottom to top, right to left algorithm
        can be used to solve euler67
        :return: sum of the heaviest root will find itself in t[0][0]
        """
        for r in range(len(t)-2, -1, -1):
            for c in range(len(t[r])):
                self.teller += 1
                t[r][c] += max(t[r+1][c], t[r+1][c+1])
            print(t[r])
        return t[0][0]

if __name__ == '__main__':
    e=Euler18()
    t1 = time()
    print(e.search(0, 0))
    print(time()-t1)
    print(e.teller)
    e.resetteller()
    t2 = time()
    print(e.smart(e.t))
    print(time()-t2)
    print(e.teller)
