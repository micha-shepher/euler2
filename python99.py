from math import log


class euler99(object):
    def __init__(self):
        self.num = open('p099_base_exp.txt').readlines()
        self.numbers = list()
        for i in self.num:
            print(i)
            self.numbers.append([int(j) for j in i.split(',')])

    def logger(self):
        l = list()
        for b, e in self.numbers:
            l.append(e*log(b))
        ml = max(l)
        return ml, l.index(ml), self.numbers[l.index(ml)]

if __name__ == '__main__':
    e = euler99()
    print(e.logger())
