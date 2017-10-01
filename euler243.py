from sympy import divisors
import sys

class Euler243():
    def __init__(self):
        self.target = 15499/94744
    def count(self, n):
        s = set(list(range(1, n)))
        for i in divisors(n)[1:-1]:
            # print(i)
            sys.stdout.flush()
            j = i
            while j < n:
                s -= {j}
                j += i
        return len(s)
    def factor(self, n):
        s = self.count(n)
        #print(s)
        #print(s/(n-1))
        print(int(s/(n-1)*94744))
        return (s/(n-1))



if __name__ == '__main__':
    e = Euler243()
    #
    #
    for i in range(1, 6):
        print(e.factor(2*3*5*7))
    for i in range(1, 6):
        print(e.factor(2*3*5*7))
    # print(e.factor(2 * 2 * 3 * 5 * 7))
    # print(e.factor(2*2*2*3*5*7))
    #
    # print(e.factor(2 * 2 * 2 * 2 * 3 * 5 * 7))
    # print(e.factor(2*2*2*2*2*3*5*7))
    # print(e.factor(2*3*5*7*11))
    # print(e.factor(2*3*5*7*11*13))
    # print(e.factor(2*3*5*7*11*13*17))
    # print(e.factor(2*3*5*7*11*13*17*19))
    # print(e.factor(2*3*5*7*11*13*17*19*23))
    print(e.target)