class Func:

    def __init__(self, x):
        self.x = x

    def even(self):
        if self.x == 1:
            print('Reached one \n')
            return
        if self.x % 2 == 0:
            self.x = self.x / 2
        if self.x % 2 == 0:
            self.even()
        else:
            self.odd()

    def odd(self):
        if self.x == 1:
            print('Reached one \n')
            return
        if self.x % 2 != 0:
            self.x = 3 * self.x + 1
            if self.x % 2 != 0:
                self.odd(self)
        self.even()


for i in range(295147905179353105127, 2 ** 100):
    a = Func(i)
    print(i)
    a.even()