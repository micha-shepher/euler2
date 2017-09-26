"""
See also Euler35
"""
import sympy

class Euler37():
    def __init__(self):
        self.primes = [2, 3, 5]
        self.cyclic = list()

    def produce_1379_primes(self):
        p = 5
        bad = set(list('024568'))
        while p < 1000000:
            p = sympy.nextprime(p)
            s = set(list(str(p)[1:]))
            s1 = set(list(str(p)))
            if str(p)[0] in ['2', '5']:
                if s.intersection(bad) == set() :
                    yield p
            else:
                if s1.intersection(bad) == set():
                    yield p

    def truncate_left(self, n):
        nn = list(str(n))
        return int(''.join(nn[1:]))

    def truncate_right(self, n):
        nn = list(str(n))
        return int(''.join(nn[:-1]))

if __name__ == '__main__':
    e = Euler37()
    for i in e.produce_1379_primes():
        e.primes.append(i)
    print(e.primes)
    for i in e.primes:
        if len(str(i)) == 1:
            e.cyclic.append(i)
        else:
            t = True
            p = i
            q = i
            for j in range(len(str(i))-1):
                p = e.truncate_left(p)
                if not p in e.primes:
                    t = False
                    break
                q = e.truncate_right(q)
                if not q in e.primes:
                    t = False
                    break
            if t:
                e.cyclic.append(i)
    e.cyclic = set(e.cyclic) - {2, 3, 5, 7}
    print(set(e.cyclic))
    print(len(e.cyclic))
    print(sum(list(set(e.cyclic))))