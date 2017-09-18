class BackTrack(Exception):
    pass

class Ready(Exception):
    pass

class Sudoku(object):
    def __init__(self, sudoku=None):
        self.sudoku = sudoku
        self.rows = list()
        self.columns = list()
        self.squares = list()
        self.stack = list()

        for row in range(9):
            self.rows.append({i for i in sudoku[row] if int(i) > 0})
        for col in range(9):
            self.columns.append({sudoku[r][col] for r in range(9) if int(sudoku[r][col]) > 0})
        for sq in range(9):
            s = set()
            rbase = sq // 3 * 3
            cbase = (sq % 3) * 3
            for r in range(rbase, rbase + 3):
                for c in range(cbase, cbase + 3):
                    if sudoku[r][c] != '0':
                        s.add(sudoku[r][c])
            self.squares.append(s)

    def checkcolumn(self, col):
        fixed = False
        for i in list('123456789'):
            if i in self.columns[col]:
                continue
            s = [j[col] for j in self.sudoku]
            for pos, elem in enumerate(s):
                sq = self.get_square(pos, col)
                if elem == '0':
                    if i in self.rows[pos] or i in self.squares[sq]:
                        s[pos] = 'x'
            if s.count('0') == 1:
                fixed = True
                pos = s.index('0')
                sq = self.get_square(pos, col)
                self.fixcol(sq, pos, col, i, 'col')
            elif s.count('0') == 0:
                raise BackTrack('fail {} at col {}'.format(i, col+1))

        return fixed

    def checkrow(self, row):
        fixed = False
        for i in list('123456789'):
            if i in self.rows[row]:
                continue
            s = [i for i in self.sudoku[row]]
            for col, elem in enumerate(s):
                sq = self.get_square(row, col)
                if elem == '0':
                    if i in self.columns[col] or i in self.squares[sq]:
                        s[col] = 'x'
            if s.count('0') == 1:
                fixed = True
                col = s.index('0')
                sq = self.get_square(row, col)
                self.fixcol(sq, row, col, i, 'row')
            elif s.count('0') == 0:
                raise BackTrack('fail {} at row {}'.format(i, row+1))
        return fixed

    def checkposition(self):
        fixed = False
        for r in range(9):
            for c in range(9):
                if self.sudoku[r][c] == '0':
                    sq = self.get_square(r, c)
                    s = {i for i in list('123456789')}  # all possibilities
                    s -= self.rows[r]
                    s -= self.columns[c]
                    s -= self.squares[sq]
                    if len(s) == 0:
                        raise BackTrack('fail at position {}:{}'.format(r+1, c+1))
                    elif len(s) == 1:
                        self.fixposition(sq, r, c, s.pop())
                        fixed = True
        return fixed

    def fixposition(self, sq, r, c, i):
        print(self)
        self.sudoku[r][c] = i
        print('fixed pos {}:{} <- {}'.format(r+1, c+1, i))
        print(self)
        self.squares[sq].add(i)
        self.rows[r].add(i)
        self.columns[c].add(i)
        if self.solved():
            raise Ready
        #self.checksquare(sq)
        #self.checkrow(r)
        #self.checkcolumn(c)

    def fixcol(self, sq, r, c, i, rc):
        print(self)
        self.sudoku[r][c] = i
        print('fixed {} {}:{} <- {}'.format(rc, r + 1, c + 1, i))
        print(self)
        self.squares[sq].add(i)
        self.rows[r].add(i)
        self.columns[c].add(i)
        if self.solved():
            raise Ready
        #self.checksquare(sq)
        #self.checkrow(r)

    def fix(self, sq, r, c, i):
        rr = sq // 3 * 3 + r
        cc = sq % 3 * 3 + c
        print(self)
        self.sudoku[rr][cc] = i
        print('fixed square {}:{} <- {}'.format(rr + 1, cc + 1, i))
        print(self)
        self.squares[sq].add(i)
        print(self.squares[sq])
        self.rows[rr].add(i)
        self.columns[cc].add(i)
        if self.solved():
            raise Ready
        #self.checkrow(r)
        #self.checkcolumn(c)

    def checksquare(self, sq):
        # this is going to limit the candidates
        #
        def count0(s):
            c = s[0].count('0') + s[1].count('0') + s[2].count('0')
            if c == 1:
                for r, row in enumerate(s):
                    if '0' in row:
                        return r, row.index('0'), c
            else:
                return 0, 0, c

        rbase = sq // 3 * 3
        cbase = sq % 3 * 3
        fixed = False
        for i in list('123456789'):
            if i in self.squares[sq]:
                continue
            s = list()
            for row in range(rbase, rbase + 3):
                s.append(self.sudoku[row][cbase:cbase + 3])
            for r, row in enumerate(range(rbase, rbase + 3)):
                for c, col in enumerate(range(cbase, cbase + 3)):
                    # mark squares where i cannot fit
                    if s[r][c] == '0':
                        if i in self.rows[row] or i in self.columns[col]:
                            s[r][c] = 'x'
            r, c, n = count0(s)
            if n == 0:
                raise BackTrack('fail {} at square {}'.format(i, sq))
            elif n == 1:
                self.fix(sq, r, c, i)
                print(self)
                fixed = True
        return fixed

    def solved(self):
        return '0' not in [item for row in self.sudoku for item in row]

    def solve(self):
        changes = [False for i in range(9)]
        rowchanges = [False for i in range(9)]
        colchanges = [False for i in range(9)]
        poschanges = [False]
        try:
            while True:
                for i in range(9):
                    changes[i] = self.checksquare(i)
                    colchanges[i] = self.checkcolumn(i)
                    rowchanges[i] = self.checkrow(i)
                poschanges[0] = self.checkposition()  # all numbers
                if True not in (changes + rowchanges + colchanges + poschanges):
                    break

            repeat = True
            while repeat:
                self.push()
                r, c, candidates = self.guess()
                solved = False
                while not solved and len(candidates) > 0:
                    candidate = candidates.pop()
                    self.fixposition(self.get_square(r, c), r, c, candidate)
                    try:
                        repeat = not self.solve()
                    except BackTrack:
                        print('backtracking bad guess {} at {}:{}'.format(candidate, r, c))
                        self.pop()
                        if len(candidates) == 1:
                            self.fixposition(self.get_square(r, c), r, c, candidates.pop())
                    except Ready:
                        print('DONE!')
                        return True

        except Ready:
            return True

    def push(self):
        self.stack.append((self.sudoku, self.rows, self.columns, self.squares,))
        print('pushing... depth {}'.format(len(self.stack)))

    def pop(self):
        self.sudoku, self.rows, self.columns, self.squares = self.stack.pop()
        print('popping... depth {}'.format(len(self.stack)))

    def get_square(self, r, c):
        return r // 3 * 3 + c // 3

    def guess(self):
        minmin = [9, 0, 0, {}]
        for r in range(9):
            for c in range(9):
                if self.sudoku[r][c] == '0':
                    s = {i for i in list('123456789')}
                    s -= self.rows[r]
                    s -= self.columns[c]
                    s -= self.squares[self.get_square(r, c)]
                    if 0 < len(s) < minmin[0]:
                        minmin = [len(s), r, c, s]
                        if minmin[0] == 2:
                            print('guessing * {}'.format(minmin))
                            return minmin[1:]
        print('guessing {}'.format(minmin))
        return minmin[1:]

    def __str__(self):
        s = ''
        for i, l in enumerate(self.sudoku):
            if i % 3 == 0:
                s += '-' * 12 + '\n'
            l = ''.join(l).replace('0', '.')
            for t in range(3):
                s += l[t * 3:t * 3 + 3]
                s += '|'
            s += '\n'

        return s


class Euler96(object):
    def __init__(self):
        self.sudokus = list()
        self.f = open('p096_sudoku.txt')
        for i in range(50):  # read 50 grids
            s = list()
            self.f.readline()
            for j in range(9):
                s.append(list(self.f.readline().strip()))
            self.sudokus.append(Sudoku(s))


if __name__ == '__main__':
    e = Euler96()
    e.sudokus[-1].solve()
    # for i in range(50):
    #    e.sudokus[i].solve()
    #    print(e.sudokus[i])
