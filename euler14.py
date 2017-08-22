__author__ = 'mshepher'
class Euler14(object):
    def __init__(self):
        self.result = dict()
    def chain(self, num):
        length = 0
        n = num
        l = list()
        while n > 1:
            l.append(n)
            if n in self.result:
                self.result[num] = self.result[n] + length
                return self.result[num]
            if n % 2 == 0:
                n //= 2
            else:
                n = 3*n + 1
            length += 1
        l.append(1)
        length += 1
        self.result[num] = length
        return length

    def longest(self):
        m = 0, 0
        for i in range(1, 1000001):
            m1 = self.chain(i)
            if m1 > m[1]:
                m = i, m1
            if i % 1000 == 0:
                print(i, m)

if __name__ == '__main__':
    e = Euler14()
    print(e.chain(10))
    print(e.chain(80))
    print(e.chain(106))
    print(e.chain(190))
    print(e.longest())
