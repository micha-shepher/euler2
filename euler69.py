from sympy import totient


class Euler69():
    def __init__(self, top):
        self.top = top

    def findmax(self):
        max = 1.0
        imax = 1
        for i in range(1, self.top+1):
            f = i/totient(i)
            if f > max:
                print(i, f)
                max = f
                imax = i
        return max,  imax


if __name__ == '__main__':
    e = Euler69(1000000)
    print(e.findmax())
