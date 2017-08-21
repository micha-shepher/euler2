__author__ = 'mshepher'

class Euler25(object):
    def __init__(self):
        self.s5 = 5**0.5
        self.phi = (1+self.s5)/2
    def gen(self):
        f = self.phi
        for i in range(10000):
            yield f/self.s5
            f *= self.phi
    def digits(self, n):
        return len(str(n))
    def search(self):
        i = 1
        for fib in self.gen():
            l = self.digits(fib)
            print('leng {}'.format(l))
            if self.digits(fib) > 999:
                print(i)
            i += 1

if __name__ == '__main__':
    e = Euler25()
    e.search()