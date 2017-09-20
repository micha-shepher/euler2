class Euler33():
    def __init__(self):
        self.denominator = [ i for i in range(10, 99) if not i % 10 ==0 ]

    def isfake(self, a, b):
        la = list(str(a))
        lb = list(str(b))
        sa = set(la)
        sb = set(lb)
        inter = sa.intersection(sb) - {1}
        if len(inter) == 0:
            return False
        for num in inter:
            # check cancelling
            laa = la.copy()
            lbb = lb.copy()
            laa.remove(num)
            lbb.remove(num)
            return int(''.join(laa)) / int(''.join(lbb)) == a / b

    def look(self):
        result = list()
        for i in self.denominator:
            for j in [k for k in range(10, i) if not k % 10 == 0] :
                if self.isfake(i, j):
                    result.append((j, i,))
        self.result = result
        return result

    def product(self):
        x = 1
        y = 1
        for i, j in self.result:
            x *= i
            y *= j
        return x, y


if __name__ == '__main__':
    e = Euler33()
    print(e.isfake(98, 39))
    print(e.isfake(98, 49))
    print(e.look())
    print(e.product())