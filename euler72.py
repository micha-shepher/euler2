from sympy import isprime, factorint
from sympy import totient

class Euler72(object):
    def __init__(self, top):
        self.top = top
        self.reduced = 0
        self.divi = [{0}]
        for i in range(1, top+1):
            self.divi.append(set(factorint(i)))
        print('finished divi')
    def count(self):

        def check(j, i):
            return not self.divi[i].intersection(self.divi[j])

        for i in range(1, self.top+1):
            if isprime(i):
                self.reduced += (i-1)
            else:
                self.reduced += 1  # 1 is always a solution
                for j in range(2, i):
                    if check(j, i):
                        self.reduced += 1

                    # if self.divi[i].intersection(self.divi[j]) == {1}:
                    #    self.reduced += 1
                    # if gcd(i, j) == 1:
                    #    self.reduced += 1
            if i % 100 == 0:
                print(i, self.reduced)
        return self.reduced

    def countfast(self):
        c = 0
        for i in range(1, 1000001):
            c += totient(i)
        return c-1  # because 1/1 is not counted.

if __name__ == '__main__':
    e = Euler72(1000000)
    print(e.count())