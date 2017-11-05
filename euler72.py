from sympy import gcd, isprime, divisors


class Euler72(object):
    def __init__(self, top):
        self.top = top
        self.reduced = 0
        self.divi = [{0}]
        for i in range(1, top+1):
            self.divi.append(set(divisors(i)[:1]))
        print('finished divi')
    def count(self):

        def check(j, i):
            for k in self.divi[j]:
                if k in self.divi[i]:
                    return False
            return True

        for i in range(1, self.top+1):
            if isprime(i):
                self.reduced += (i-1)
            else:
                if i % 100 == 0:
                    print(i, self.reduced)
                for j in range(1, i):
                    if check(j, i):
                        self.reduced += 1

                    # if self.divi[i].intersection(self.divi[j]) == {1}:
                    #    self.reduced += 1
                    # if gcd(i, j) == 1:
                    #    self.reduced += 1
        return self.reduced

if __name__ == '__main__':
    e = Euler72(1000000)
    print(e.count())