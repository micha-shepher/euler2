__author__ = 'mshepher'

from decimal import getcontext, Decimal
class Euler80(object):

    def __init__(self):

        getcontext().prec = 102
        self.decimals = [Decimal(i)**Decimal(0.5) for i in range(2, 101) if i not in [4, 9, 16, 25, 36, 49, 64, 81, 100]]
        self.decimals = [str(i).replace('.', '')[:-2] for i in self.decimals]
        self.sums = [sum(int(i) for i in s) for s in self.decimals]
        print(self.sums)
        print(len(self.sums))
        #print(self.decimals)
        print (sum(self.sums))


if __name__ == '__main__':
    e = Euler80()
