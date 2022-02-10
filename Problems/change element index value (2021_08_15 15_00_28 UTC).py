def usr(a):
    while True:
        pos1, val1 = input('Enter int this format\n(index) (value)   #brackets are not to br included\n').split()
        if pos1.isdigit() is False:
            print('Enter Numbers\n')

        if int(pos1) not in range(len(a)):
            print('Index out of bounds')
        if val1.isdigit() is True:
            val1 = int(val1)
        break
    return int(pos1), val1


def replacing(lst, pos1, val1):
    lst[pos1] = val1


def timer(a):
    while True:
        print(a)
        ask = input('Do you wish to change the terms in the list\nYes-[Y] or No-[N]\n').lower().strip()
        if ask == 'y':
            c, d = usr(a)
            replacing(a, c, d)
        elif ask == 'n':
            print('Your list is :',a)
            break
        else:
            print('Enter Y or N')


x = [1, 2, 3, 4, 5]
timer(x)
