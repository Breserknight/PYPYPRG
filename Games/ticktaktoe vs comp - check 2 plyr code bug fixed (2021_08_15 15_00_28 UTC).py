from random import randint


def display(row1, row2, row3):
    print(f'{row1}\n{row2}\n{row3}')


def inputs(num, var):
    lst.remove(num)
    if num <= 3:
        a[num-1] = var
    elif num <= 6:
        b[num-4] = var
    else:
        c[num-7] = var


def comp():
    # so that the function stops after u win
    if check() is True:
        if len(lst) == 0:
            return False
        q = randint(0, len(lst)-1)
        u = lst[q]
        inputs(u, 'O')


def check():
    if a[0] == b[0] == c[0] == 'X' or a[1] == b[1] == c[1] == 'X' or \
            a[2] == b[2] == c[2] == 'X' or a[0] == b[1] == c[2] == 'X' \
            or a[2] == b[1] == c[0] == 'X' or set(a) == {'X'} or set(b) == {'X'} or set(c) == {'X'}:
        print('You Win')
        return False
    elif a[0] == b[0] == c[0] == 'O' or a[1] == b[1] == c[1] == 'O' or\
            a[2] == b[2] == c[2] == 'O' or a[0] == b[1] == c[2] == 'O' \
            or a[2] == b[1] == c[0] == 'O' or set(a) == {'O'} or set(b) == {'O'} or set(c) == {'O'}:
        print('You Lose')
        return False
    else:
        return True


a = [' ', ' ', ' ']
b = [' ', ' ', ' ']
c = [' ', ' ', ' ']
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
display(a, b, c)

while check():
    y = input()
    if y.isdigit() is False:
        print('Please Enter a number')
        continue
    y = int(y)
    if y not in lst:
        if y > 9:
            print('Please enter values below 9')
            continue
        print('This place is already filled')
        continue
    inputs(y, 'X')
    if len(lst) == 0:
        display(a, b, c)
        if check() is True:
            print('Tie')
        elif check() is False:
            print('Win')
        break
    comp()
    display(a, b, c)
