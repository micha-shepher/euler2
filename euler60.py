from sympy import isprime, nextprime


class Euler60():
    def __init__(self, top):
        self.top = top
        self.pairs = list()
    def test(self, set, x):
        flag = True
        for i in set:
            flag = flag and isprime(int('{}{}'.format(i, x)))
            if not flag:
                return flag
            flag = flag and isprime(int('{}{}'.format(x, i)))
            if not flag:
                return flag
        return flag
    def loop(self, sl):
        s = {3, 7}  # 2 and 5 are not good, because xxxxx2 and xxxx5 are not primes.
        np = 11
        while len(s) < sl and np < self.top:
            if self.test(s, np):
                s.add(np)
                print(s)
            np = nextprime(np)

if __name__ == '__main__':
    e = Euler60(50000)
    e.loop(5)