from pprint import pprint
class Euler36():
    def __init__(self):
        self.both = list()
        self.pali10 = list()
        self.pali2 = list()
        for i in range(1000000):
            s = str(i)
            if list(s) == list(reversed(s)):
                self.pali10.append(i)
    def do2(self):
        for i in self.pali10:
            binary = '{:b}'.format(i)
            if list(binary) == list(reversed(binary)):
                self.both.append((i, binary))


if __name__ == '__main__':
    e = Euler36()
    #print(e.pali10)
    e.do2()
    pprint(e.both)
    print(sum([i[0] for i in e.both]))