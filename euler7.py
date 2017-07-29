from math import sqrt

__author__ = 'mshepher'

from array import array

"""
find the 10001 prime number.
"""


class Euler7(object):
    def __init__(self, top):
        self.top = top
        self.primes = array('l', range(2, self.top))
        self.sqrt = int(sqrt(top))

    def sieve(self):
        for i in range(2, self.sqrt):
            if i in self.primes:
                j = i+i
                print(j)
                while j < self.top-1:
                    print (j)
                    try:
                        self.primes[j] = 0
                    except:
                        print('offendign', j)
                    j += i


    def get(self):
        res = array('l', [i for i in self.primes if i > 0])
        return res



if __name__ == '__main__':
    e = Euler7(20)
    e.sieve()
    ew = e.get()
    print(ew)
    print(len(ew))
