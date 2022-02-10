def calc(a, b, val):
    counter = 0
    sum1 = 0
    while True:
        numerator = 1
        denominator = 1
        for i in a:
            if a[counter] == i:
                continue
            numerator *= (val - i)
        for i in a:
            if a[counter] == i:
                continue
            denominator *= (a[counter] - i)
        sum1 += numerator / denominator * b[counter]
        counter += 1
        if counter == len(a):
            break
    print(sum1)


x = list(map(float, input().split()))
y = list(map(float, input().split()))
z = float(input('Value\n'))
calc(x, y, z)
