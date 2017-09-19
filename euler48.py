class Euler48():
    def calc(self):
        s = list()
        for i in range(1, 1000):
            s.append((i**i) % 10000000000)
        return sum(s)



if __name__ == '__main__':
    e = Euler48()
    print(e.calc())