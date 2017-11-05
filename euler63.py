from math import log10
class Euler63(object):
    def __init__(self):
        self.c = 0
    def count(self):
        for i in range(1, 10):
            print('testing {}'.format(i))
            for powers in range(1, 100):
                x = i**powers
                # print(x, log10(x))
                if powers-1<=log10(x)<=powers:
                    print('{}^{}'.format(i, powers))
                if len(str(x)) == powers:
                    print('len {} {}'.format(len(str(x)), powers))
                    self.c += 1
        return self.c
if __name__ == '__main__':
    e = Euler63()
    print(e.count())
