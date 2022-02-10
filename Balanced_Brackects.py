def check(a):
    d = {'(':')', '[':']', '{':'}'}
    hold = []
    for i in a:
        if i in d.keys():
            hold.append(i)
        else:
            if hold:
                if d[hold[-1]] == i:
                    hold.pop()
            else:
                return 'Un-Balanced'
    return 'Balaned' if len(hold) == 0 else 'Unbalanced'

x = input('Bracket sets : ')
print(check(x))
