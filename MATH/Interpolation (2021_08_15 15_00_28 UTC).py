import math


def forward(a, b, val1):
    h = a[1] - a[0]
    r = (val1 - a[0])/h
    print(f'{r} value of r')
    # counter
    ct = 0
    # sum1 is initialized for factorial summed values
    sum1 = 0
    # v fact number (divided)
    v = len(b)
    while True:
        while True:
            d = [r-i for i in range(v)]
            break
        prd = 1
        for i in d:
            prd *= i
        sum1 += prd*b[v-1]/math.factorial(v)
        ct += 1
        v -= 1
        if ct == len(b):
            break
    return orig[0] + sum1


def backward(a, b, val1):
    h = a[1] - a[0]
    r = (val1 - a[-1]) / h
    ct = 0
    sum1 = 0
    v = len(b)
    print(f'{r} value of r')
    while True:
        while True:
            # r + i instead of -
            d = [r+i for i in range(v)]
            break
        prd = 1
        for i in d:
            prd *= i
        sum1 += prd*b[v-1]/math.factorial(v)
        ct += 1
        v -= 1
        if ct == len(b):
            break
    return orig[-1] + sum1


x = list(map(float, input().split()))
y = list(map(float, input().split()))
orig = y
first = []
last = []
while True:
    c = [round(y[i+1] - y[i], 5) for i in range(len(y)-1)]
    print(c)
    first.append(c[0])
    last.append(c[-1])
    y = c
    if len(y) == 1:
        break
val = float(input('Value = '))
choice = int(input('1-Forward\n2-Backward \n'))
if choice == 1:
    print(forward(x, first, val))
elif choice == 2:
    print(backward(x, last, val))
else:
    print("wrong choice")
