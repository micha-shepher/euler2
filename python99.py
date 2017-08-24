class euler99(object):
    def __init__(self):
        self.num = open('p099_base_exp.txt').readlines()
        self.numbers = list()
        for i in self.num:
            self.numbers.append([(int(k), int(l)) for k, l in i.split(',')])


if __name__ == '__main__':
    e = euler99()
    print(e.numbers)
