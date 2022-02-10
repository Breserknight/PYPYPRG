# Print Designs
# x, a is x * a [mat size] : a is 3*x
x, a = map(int, input().split())
c = '.|.'
ctr = 1
for i in range(int(x/2)):
    y = c*ctr
    print(y.center(a, '-'))
    ctr += 2
print('WELCOME'.center(a, '-'))
ctr -= 2
for i in range(int(x/2)):
    y = c*ctr
    print(y.center(a, '-'))
    ctr -= 2
