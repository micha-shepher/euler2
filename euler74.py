from sympy import factorial

__author__ = 'mshepher'
class Euler74(object):
    def __init__(self):
        self.chains = dict()
    def sumfact(self, n):
        return sum([factorial(int(i)) for i in list(str(n))])
    def chain(self, num):
        l = list()
        c = 0
        n = num
        while not n in l:
            if n in self.chains:
                c += self.chains[n]
                break
            l.append(n)
            n = self.sumfact(n)
            c += 1
        self.chains[num] = c
        return c

if __name__ == '__main__':
    e = Euler74()
    sixty = dict()
    for i in range(1000000):
        x = e.chain(i)
        if x >= 60:
            print(i)
            sixty[i] = x
    print('sixty = {}'.format(sixty))
    print(len(sixty))


