x = []
with open('testcase.txt', 'r') as file:
    for line in file:
        x.append(list(map(int, line.split())))
max1 = 0
for i in range(len(x)):
    for o in range(len(x[0]) - 3):
        max1 = max(max1, x[i][o]*x[i][o+1]*x[i][o+2]*x[i][o+3])
for i in range(len(x) - 3):
    for o in range(len(x[0]) - 3):
        max1 = max(max1, x[o][i]*x[o+1][i]*x[o+2][i]*x[o+3][i])
for i in range(len(x) - 3):
    for o in range(len(x[0]) - 3):
        max1 = max(max1, x[i][o]*x[i+1][o+1]*x[i+2][o+2]*x[i+3][o+3])
print(max1)