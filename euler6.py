__author__ = 'mshepher'


class Euler6(object):
    """
     find the difference between the square of the sum of 1..100 and the sum of the squares of 1..100
     """

    def __init__(self):
        s = (1 + 100) * 50
        sumsquare = s * s
        l = [i * i for i in range(1, 101)]
        print(sumsquare)
        print(sum(l))
        print (sumsquare-sum(l))


if __name__ == '__main__':
    e = Euler6()

