from pprint import pprint


class Euler45():
    def __init__(self):
        self.tri = {1}
        self.pent = {1}
        self.hex = {1}
        inc = 2
        prev = 1
        while len(self.tri) < 500000:
            prev += inc
            self.tri.add(prev)
            inc += 1

        inc = 4
        prev = 1
        while len(self.pent) < 500000:
            prev += inc
            self.pent.add(prev)
            inc += 3

        inc = 5
        prev = 1
        while len(self.hex) < 500000:
            prev += inc
            self.hex.add(prev)
            inc += 4


if __name__ == '__main__':
    e = Euler45()
    print(e.tri.intersection(e.pent).intersection(e.hex))
