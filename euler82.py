from pprint import pprint
from random import randint
import sympy

class Euler81(object):
    def __init__(self):
        self.m5 = [[131, 673, 234, 103,  18],
                  [201,  96, 342, 965, 150],
                  [630, 803, 746, 422, 111],
                  [537, 699, 497, 121, 956],
                  [805, 732, 524,  37, 331]]

        self.m10 = [[74,  80, 28, 84, 73, 83, 80, 16, 59, 32],
                  [90,  32, 80, 48, 79, 28, 73,  7, 17, 56],
                  [43,  56, 34, 77, 66, 53, 68, 62, 66, 23],
                  [58,  97, 35, 47, 58, 52, 25, 66, 82, 76],
                  [100, 97, 60, 16,  5, 40, 81, 68, 37,  6],
                  [23,  16, 64, 34, 97, 82, 98, 76, 12, 78],
                  [7,   46, 24, 39, 16, 22, 77, 63, 82, 37],
                  [89,  78, 80, 13, 13, 11, 40, 75, 36, 50],
                  [81,  97,  5, 91, 61, 15, 97, 62,  8, 84],
                  [54,  72, 64, 82, 36, 84, 23, 81, 18,  2]]

        self.m = self.m5

        #with open('../p081.txt') as f:
        #    mm = f.read().strip().split('\n')
        #    for row in mm:
        #        self.m.append([int(i) for i in row.split(',')])

        #    print(self.m)
        #    print(len(self.m))
        self.top = len(self.m)-1
        self.complexity = 0
        self.cache = dict()

    def brute(self, sum, r, c):
        self.complexity += 1
        sum += self.m[r][c]
        if r == self.top == c:
            return sum  # left bottom, no recursion necessary
        elif r == self.top:
            return self.brute(sum, r, c+1)
        elif c == self.top:
            return self.brute(sum, r+1, c)
        else:
            return min(self.brute(sum, r+1, c), self.brute(sum, r, c+1))

    def downup(self, sum, r, c):
        self.complexity += 1
        sum += self.m[r][c]
        if r == 0 == c:
            return sum
        elif r == 0:
            return self.downup(sum, r, c-1)
        elif c == 0:
            return self.downup(sum, r-1, c)
        else:
            return min(self.downup(sum, r-1, c), self.downup(sum, r, c-1))

    def smart(self, sum, r, c):
        for c in range(self.top, -1, -1):
            for r in range(self.top, -1, -1):
                key = '{}:{}'.format(r, c)
                if key not in self.cache:
                    self.complexity += 1
                    if c == self.top: # in this case no min is necessary.
                        self.cache[key] = self.m[r][c]
                    else:
                        if r > 0:
                            min1 = self.m[r-1][c]
                        else:
                            min1 = 0
                        if r == self.top:
                            min2 = 0
                        else:
                            min2 = self.m[r+1][c]
                        if c == 0:
                            min3 = 0
                        else:
                            min3 = self.m[r][c-1]
                        self.cache[key] = self.m[r][c] + min(min1, min2, min3)
        return min([self.cache['0:{}'.format(i)] for i in range(5)])

    def bottomup(self):
        for c in range(self.top-1, -1, -1):
            vec = list()
            for r in range(5):
                vec.append(self.m[r][c]+self.m[r][c+1])
        pprint(self.m)

if __name__ == '__main__':
    e = Euler81()
    #print(e.brute(0, 0, 0))
    #print(e.complexity)
    e.complexity = 0
    #print(e.downup(0, 9, 9))
    #print(e.complexity)
    #print(e.brute(0,0,0))
    #print(e.complexity)
    #e.complexity = 0
    #print('result={}'.format(e.smart(0,0,0)))
    #print('complexity = {}'.format(e.complexity))
    #for i in range(5):
    #    print(e.cache['0:{}'.format(i)])
    pprint(e.m)
    e.bottomup()