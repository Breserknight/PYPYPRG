import math

# Find Angle of complex number
sg = 1
s = 1
x = input()
y = [i for i in x]
if y[0] == '+' or y[0] == '-':
    if y[0] == '-':
        s = -1
    y.pop(0)

d1 = []
d2 = []
for i in y[:]:
    if i != '+' and i != '-':
        d1.append(i)
        y.remove(i)
    elif i == '+':
        y.remove('+')
        break
    else:
        y.remove('-')
        sg = -1
        break
for i in y:
    if i != 'j':
        d2.append(i)
d1 = ''.join(d1)
d2 = ''.join(d2)
d1 = int(d1) * s
d2 = int(d2) * sg
r = (d1 ** 2 + d2 ** 2) ** 0.5
if d1 == 0:
    t = 1.57079632679
else:
    phi = math.atan(d2 / d1)
    t = math.degrees(phi)
    if t < 0:
        t = 180 + t
    t = math.radians(t)
print(f'{r}\n{t}')
