from pprint import pprint


class Euler62():
    def __init__(self):
        self.cubes = list()
        self.perms = list()
        self.d = dict()
        self.res = dict()
        for i in range(345, 9000):
            cube = i*i*i
            self.cubes.append(cube)
            perm = list(str(cube))
            perm.sort()
            perm = ''.join(perm)
            self.perms.append(perm)
            if perm in self.d:
                self.d[perm] += 1
                self.res[perm].append(i)
            else:
                self.res[perm] = [i]
                self.d[perm] = 1

        for key in self.d:
            if self.d[key] > 3:
                print('{}={} {} {}'.format(key, self.d[key], self.res[key], [i**3 for i in self.res[key]]))

if __name__ == '__main__':
    e = Euler62()
    e.perms.sort()
