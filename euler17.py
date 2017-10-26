from pprint import pprint


class Euler17(object):
    def __init__(self):
        self.d = dict()
        s = 'one,two,three,four,five,six,seven,eight,nine,ten'.split(',')
        for i, n in enumerate(s):
            self.d[i+1] = n
        s = 'eleven,twelve,thirteen,fourteen,fifteen,sixteen,seventeen,eighteen,nineteen,twenty'.split(',')
        for i, n in enumerate(s):
            self.d[i + 11] = n
        s = 'thirty,forty,fifty,sixty,seventy,eighty,ninety'.split(',')
        for i, n in enumerate(s):
            self.d[(i+1)*10+20] = n
        self.d[100] = len('hundred')
        self.d[1000] = len('thousand')

    def sentence(self, i):
        s = ''
        if 1 <= i <= 20:
            s = self.d[i]
        elif 21 <= i <= 99:
            if i % 10 == 0:
                s = self.d[i]
            else:
                s = '{} {}'.format(self.d[10*(i//10)], self.d[i%10])
        elif 100 <= i < 1000:
            hundreds = i // 100
            remainder = i % 100
            s = '{} hundred'.format(self.d[hundreds])
            if remainder > 0:
                s += ' and {}'.format(self.sentence(remainder))
        elif i == 1000:
            s = 'one thousand'
        else:
            print('wasda????')
        return s

if __name__ == '__main__':
    e = Euler17()
    sum = 0
    for i in range(1, 1001):
        sent = e.sentence(i)
        print(sent)
        sum += len(sent.replace(' ', ''))
    print(' sum = {}'.format(sum))


