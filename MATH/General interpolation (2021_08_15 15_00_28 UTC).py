def printf(a):
    a = [str(i) for i in a]
    a = ' '.join(a)
    print(a)


def poly(a, b):
    global firsts
    length = len(a)
    diff1 = []
    new = []
    counter = 1
    while True:
        se = 0
        for i in range(counter, len(a)):
            diff1.append(a[i] - a[se])
            se += 1
        counter += 1
        for i in range(len(b)-1):
            new.append((b[i+1]-b[i])/diff1[i])
        diff1 = []
        b = new
        printf(new)
        firsts.append(new[0])
        new = []
        if counter == length:
            break
    printf(firsts)


def answer(a, b, val):
    counter = 1
    ct = 0
    fact = 1
    sum1 = 0
    while True:
        for i in range(counter):
            fact *= val-a[i]
        sum1 += fact*b[ct]
        ct += 1
        counter += 1
        fact = 1
        if counter == len(a):
            break
    return sum1


x = list(map(float, input().split()))
y = list(map(float, input().split()))
firsts = []
poly(x, y)
val = int(input('Enter Value\n'))
print(y[0] + answer(x, firsts, val))