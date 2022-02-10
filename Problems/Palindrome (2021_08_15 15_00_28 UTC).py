def printing(q):
    print(int(''.join(q)))


x = int(input())
counter = 1
while True:
    lst = []
    for i in range(1,counter+1):
        lst.append(i)
    for i in lst[::-1][1:]:
        lst.append(i)
    lst = [str(i) for i in lst]
    printing(lst)
    counter += 1
    if counter == x+1:
        break
