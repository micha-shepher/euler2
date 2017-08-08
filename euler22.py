__author__ = 'mshepher'

class Euler22(object):
    def __init__(self):
        value = {k:v for k,v in zip(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), range(1, 27))}
        with open('names.txt') as f:
            self.names = f.read().split(',')
        d = list()
        for i, name in enumerate(self.names):
            d.append(sum([value[i] for i in list(name)])*i)
        self.sss = sum(d)
    def result(self):
        return self.sss