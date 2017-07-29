__author__ = 'mshepher'

class Euler4(object):
    """
    find the largest 6 digit palindrome which is a product of two 3 digit integers.
    """
    def __init__(self):
        pass

    def palindrome(self, i, j):
        st = str(i*j)
        return st == st[::-1]


    def search(self):
        result = list()
        for i in range(100, 999):
            for j in range(100, 999):
                if self.palindrome(i, j):
                    result.append((i*j, i, j))
        result.sort(key=lambda x: x[0])
        return result

if __name__ == '__main__':
    e = Euler4()
    print(e.search())