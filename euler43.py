from itertools import permutations
class Euler43(object):
    def __init__(self):
        # create all pandigital numbers
        self.pan = list()
        for i in permutations('0123456789', 10):
            self.pan.append(''.join(i))
    def check(self):
        def check2(i):
            return int(i[1:4]) % 2 == 0
        def check3(i):
            return int(i[2:5]) % 3 == 0
        def check5(i):
            return int(i[3:6]) % 5 == 0
        def check7(i):
            return int(i[4:7]) % 7 == 0
        def check11(i):
            return int(i[5:8]) % 11 == 0
        def check13(i):
            return int(i[6:9]) % 13 == 0
        def check17(i):
            return int(i[7:]) % 17 == 0
        sum = 0
        for i in self.pan:
            if not check2(i): continue
            if not check3(i): continue
            if not check5(i): continue
            if not check7(i): continue
            if not check11(i): continue
            if not check13(i): continue
            if not check17(i): continue
            print('found {}'.format(i))
            sum += int(i)
        return sum

if __name__ == '__main__':
    e = Euler43()
    print(e.pan[:10])
    print(e.check())