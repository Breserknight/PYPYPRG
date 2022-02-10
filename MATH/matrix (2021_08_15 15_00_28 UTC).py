def deter(i):
    d = i[0][0]*(i[1][1]*i[2][2]-i[1][2]*i[2][1])-i[0][1]*(i[1][0]*i[2][2]-i[1][2]*i[2][0])+i[0][2]*(i[1][0]*i[2][1]-i[1][1]*i[2][0])
    return d


def multi(i,j):

    return


prompt = input('Commands\nDeterminant->D ,Multiplication->M\n')
a,b = [list(map(int,input(f'enter dimensions of matrix {i+1}\n').split())) for i in range(2)]
while a[0] != a[1] or b[0] != b[1] or a[0] != 3 or b[0] !=3:
    print('This Prg can only do computations for 3x3 matrices')
    a, b = [list(map(int, input(f'enter dimensions of matrix {i + 1}\n').split())) for i in range(2)]

if prompt == 'D' or prompt == 'd':
    x = [(list(map(int, input().split()))) for _ in range(3)]
    result = deter(x)
    for i in result:
        print(i)
elif prompt == 'M' or prompt == 'm':
    x = [(list(map(int, input().split()))) for _ in range(3)]
    o = [[],[],[]]
    for _ in range(3):
        ip = list(map(int, input().split()))
        o[0].append(ip[0])
        o[1].append(ip[1])
        o[2].append(ip[2])
    print(o)
