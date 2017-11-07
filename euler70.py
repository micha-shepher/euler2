from operator import itemgetter

from sympy import totient, isprime


class Euler70():
    def __init__(self, top):
        self.tots = list()
        for i in range(2, top+1):
            tot = totient(i)
            if sorted(list(str(i))) == sorted(list(str(tot))):
                self.tots.append((i, i/tot,))
            if i % 100000 == 0:
                print(i)

    def sorting(self):
        return (sorted(self.tots, key=itemgetter(1)))

if __name__ == '__main__':
    e = Euler70(10000000)
    print(e.sorting())