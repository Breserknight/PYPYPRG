class Matrix:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        dst = [[a + b for a, b in zip(self.a[i], self.b[i])] for i in range(3)]
        display(dst)

    def multiply(self):
        yet = []
        c = []
        counter = 0
        while counter < 3:
            for i in range(3):
                c.append(self.b[i][counter])
            yet.append(c)
            c = []
            counter += 1
        self.b = yet
        ctr = 0
        ctr1 = 0
        res = []
        temp = []

        while ctr1 < 3:
            sum1 = 0
            for i in range(3):
                sum1 += self.a[ctr1][i] * self.b[ctr][i]
            temp.append(sum1)
            ctr += 1
            if ctr % 3 == 0 and ctr != 0:
                ctr1 += 1
                ctr = 0
                res.append(temp)
                temp = []
        display(res)


def display(l):
    for i in range(len(l)):
        print(f"{l[i][0]} {l[i][1]} {l[i][2]}")


def inputs():
    lst = ['+', '*', 'deter']
    # input format is
    # Matrix A
    # 1 2 3
    # 4 5 6
    # 7 8 9
    # same for mat B
    while True:
        read = input(f'Enter one operation from the following list {lst}\n')
        if read in lst:
            break
    if read != 'deter':
        print("Matrix A")
        x = [list(map(int, input().split())) for _ in range(3)]
        print("Matrix B")
        y = [list(map(int, input().split())) for _ in range(3)]
        c = Matrix(x, y)
    else:
        print("Matrix A")
        x = [list(map(int, input().split())) for _ in range(3)]
        c = Matrix(x, 0)
    if read == '+':
        c.add()
    if read == '*':
        c.multiply()
    if read == 'deter':
        # pending
        print('pending')


inputs()
