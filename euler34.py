from sympy import factorial
class Euler34(object):
    def __init__(self):
        self.facts = dict()
        for i in range(10):
            self.facts[str(i)] = factorial(i)
        print(self.facts)
    def search(self):
        for i in range(9*factorial(9)):
            ss = sum ([self.facts[i] for i in list(str(i))])
            if i == ss:
                print('found: {}'.format(i))
            if i % 100000 == 9:
                print('at {} ({})'.format(i, ss))
if __name__ == '__main__':
    e = Euler34()
    e.search()


