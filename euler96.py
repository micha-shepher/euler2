class Euler96(object):
    def __init__(self):
        self.f = open('p096_sudoku.txt')
        for i in self.f.readlines():
            if 'Grid' in i:
                sudoko = Sudoku()
                self.sudokus[].append()