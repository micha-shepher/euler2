from sympy import isprime, nextprime


class Euler60():
    def __init__(self, top):
        self.top = top
        self.results = list()
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

    def check(self, s, sl):
        np = nextprime(s[-1])
        while len(s) < sl and np < self.top:
            if self.test(s, np):
                s.append(np)
                if len(s) == sl:
                    self.results.append(s)
                    return True
        return False

    def collect(self):
        self.pairs.append([3, 7])


    def loop(self, sl):
        s = [3, 7]  # 2 and 5 are not good, because xxxxx2 and xxxx5 are not primes.
        while len(s) < sl:
            self.check(s, sl)

if __name__ == '__main__':
    e = Euler60(50000)
    e.loop(5)