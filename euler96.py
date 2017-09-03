class Sudoku(object):
    def __init__(self, sudoku=None):
        self.sudoku = sudoku
        self.rows = list()
        self.columns = list()
        self.squares = list()
        self.candidates = dict()

        for row in range(9):
            self.rows.append({i for i in sudoku[row] if int(i) > 0})
        for col in range(9):
            self.columns.append({sudoku[r][col] for r in range(9) if int(sudoku[r][col]) > 0})
        for sq in range(9):
            s = set()
            rbase = sq//3*3
            cbase = (sq % 3)*3
            for r in range(rbase, rbase+3):
                for c in range(cbase, cbase+3):
                    if int(sudoku[r][c]) > 0:
                        s.add(sudoku[r][c])
            self.squares.append(s)


    def set_candidates(self):
        for r in range(9):
            for c in range(9):
                if self.sudoku[r][c] == '0':
                    s = {str(i) for i in range(1,10)}
                    s -= self.rows[r]
                    s -= self.columns[c]
                    s -= self.squares[r//3*3+c//3]
                    self.candidates[r*10+c] = s

    def solve(self):
        self.set_candidates()
        print(self.candidates)
        for i in range(9):
            self.checkrow(i)
        for i in range(9):
            self.checkcol(i)
        for i in range(9):
            self.checksquare(i)

    def set(self, sudoku):
        self.sudoku = sudoku
    def __str__(self):
        return '\n'.join(''.join(l).replace('0', '.') for l in self.sudoku)

class Euler96(object):
    def __init__(self):
        self.sudokus = list()
        self.f = open('p096_sudoku.txt')
        for i in range(50):  # read 50 grids
            s = list()
            skip = self.f.readline()
            for j in range(9):
                s.append(list(self.f.readline().strip()))
            self.sudokus.append(Sudoku(s))


if __name__ == '__main__':
    e = Euler96()
    print(e.sudokus[0])
    print()
    print(e.sudokus[-1])
    e.sudokus[-1].solve()