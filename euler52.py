class Euler52():
    def __init__(self, top):
        self.top = top

    def admissable(self, n):
        r = True
        ns = sorted(list(str(n)))
        for i in [n*j for j in range(2, 7)]:
            if sorted(list(str(i))) != ns:
                r = False
                break
        return r

    def search(self):
        for i in range(1, self.top+1):
            if i % 1000 == 0:
                print('.', end='')
            if i % 100000 == 0:
                print()
            if self.admissable(i):
                return i

if __name__ == '__main__':
    e = Euler52(10000000)
    print(e.search())