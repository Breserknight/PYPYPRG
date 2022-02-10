def func(a):
    lst = ["(", "[", "{"]
    store = []
    for i in a:
        if i in lst:
            store.append(i)
        else:
            if i == ")" and store[-1] == "(":
                store.pop()
            if i == "]" and store[-1] == "[":
                store.pop()
            if i == "}" and store[-1] == "{":
                store.pop()
    if len(store) == 0:
        return 'YES'
    return 'NO'


y = input()
print(func(y))
