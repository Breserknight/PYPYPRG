def printing(x):
    x = [str(i) for i in x]
    y = ''.join(x)
    print(y)


def calling(n):
    x = []
    y = []
    counter = 0
    while True:
        counter += 1
        if counter == n:
            break
        if len(x) == 0:
            print(1)
            x.append(1)
        y.append(1)
        for i in range(len(x)-1):
            y.append(x[i]+x[i+1])
        y.append(1)
        printing(y)
        x = y
        y = []


u = int(input())
calling(u)