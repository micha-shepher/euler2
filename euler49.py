from pprint import pprint

import sympy
class Euler49():
    def __init__(self):
        self.primes = list()
        self.candidates = list()
        p = 1000
        while p < 9973:
            p = sympy.nextprime(p)
            self.primes.append(p)
        for i in self.primes:
            ii = i + 3330
            iii = ii + 3330
            if ii in self.primes and iii in self.primes:
                print(i, ii, iii)
if __name__ == '__main__':
    e = Euler49()
    #pprint(e.primes)