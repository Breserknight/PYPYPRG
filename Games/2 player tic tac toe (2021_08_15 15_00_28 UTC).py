def display(a1, b1, c1):
    print(f' {a1[0]} | {a1[1]} | {a1[2]} ',
          f'\n------------\n {b1[0]} | {b1[1]} | {b1[2]}',
          f'\n------------\n {c1[0]} | {c1[1]} | {c1[2]} ')


def inputs(var):
    while True:
        i = input(f'Player {p} Enter a position\n')
        if i.isdigit() is False:
            print('Enter numbers (0-9)')
            continue
        if int(i) not in lst:
            if int(i) in range(0, 10):
                print('Space already taken \n')
                continue
            else:
                print('Number out of range, Enter values from (0-9)')
                continue
        break
    i = int(i)
    lst.remove(i)
    if i <= 3:
        a[i - 1] = var
    elif i <= 6:
        b[i - 4] = var
    else:
        c[i - 7] = var


def check():
    if a[0] == b[0] == c[0] == 'X' or a[1] == b[1] == c[1] == 'X' or \
            a[2] == b[2] == c[2] == 'X' or a[0] == b[1] == c[2] == 'X' or \
            a[2] == b[1] == c[0] == 'X' or set(a) == {'X'} or set(b) == {'X'} or set(c) == {'X'}:
        display(a, b, c)
        print('Player 1 Wins')
        return False
    elif a[0] == b[0] == c[0] == 'O' or a[1] == b[1] == c[1] == 'O' or \
            a[2] == b[2] == c[2] == 'O' or a[0] == b[1] == c[2] == 'O' or \
            a[2] == b[1] == c[0] == 'O' or set(a) == {'O'} or set(b) == {'O'} or set(c) == {'O'}:
        display(a, b, c)
        print('Player 2 Wins')
        return False
    elif len(lst) == 0:
        display(a, b, c)
        print('Tie\n')
        return False
    else:
        return True


def game_time():
    global p, counter
    while True:
        var1 = input('Enter X or O\n').upper().strip()
        if var1 not in ['O', 'X']:
            print('Enter X or O not anything else \n')
            continue
        if var1 == 'X':
            var2 = 'O'
            break
        elif var1 == 'O':
            var2 = 'X'
            break
    while check():
        display(a, b, c)
        if counter % 2 == 0:
            p = 1
            inputs(var1)
            counter += 1
        else:
            p = 2
            inputs(var2)
            counter += 1


def again():
    global a, b, c, lst, p, counter
    while True:
        z = input('Another Round?\nYes-[Y] or No-[N]\n').lower().strip()
        if z == 'y':
            a = [' ', ' ', ' ']
            b = [' ', ' ', ' ']
            c = [' ', ' ', ' ']
            lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            p = 1
            counter = 0
            return True
        elif z == 'n':
            return False
        else:
            print('Enter Yes(Y) or No(N)\n')


a = [' ', ' ', ' ']
b = [' ', ' ', ' ']
c = [' ', ' ', ' ']
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
p = 1
counter = 0
game_time()
while again():
    game_time()
