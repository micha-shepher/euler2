class Euler28(object):
    def calc(self, n):

        return 2/3*n*n*n+4*n*n-43/3*n


if __name__ == '__main__':
    e = Euler28()
    print(e.calc(4))