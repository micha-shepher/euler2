from math import sqrt

__author__ = 'mshepher'

class Euler12(object):

    def __init__(self):
        self.triangles = [1]
        self.primes = [2, 3, 5, 7, 11, 13, 17, 19]
        b = 1
        diff = 2
        for i in range(100000):
            next = b+diff
            self.triangles.append(next)
            b = next
            diff += 1
        print(self.triangles[-10:-1])

    def check(self, n):
        return n*(n+1)/2 in self.triangles

    def gen(self):
        for a1 in range(5):
            for a2 in range(5):
                for a3 in range(5):
                    for a4 in range(5):
                        for a5 in range(5):
                            for a6 in range(5):
                                for a7 in range(5):
                                    for a8 in range(5):
                                        pass


if __name__ == '__main__':
    e = Euler12()
    print(e.check(10))
    print(e.check(28))
    for i in range(10,30):
        print(e.check(i))
