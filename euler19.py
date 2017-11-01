class Euler19(object):
    def __init__(self):
        def is_leap(y):
            return y > 1900 and y % 4 == 0
        self.days = list()
        regularmonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        leapmonths = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        for year in range(1900, 2001):
            if is_leap(year):
                months = leapmonths
                print('{} is leap'.format(year))
            else:
                months = regularmonths
            for month in months:
                for day in range(1, month+1):
                    self.days.append(day)
        print(self.days[:60])
        print(self.days[-60:])
        for loc, day in enumerate(self.days):
            if day == 1 and loc % 7 == 0:
                print (loc, day)


if __name__ == '__main__':
    e = Euler19()