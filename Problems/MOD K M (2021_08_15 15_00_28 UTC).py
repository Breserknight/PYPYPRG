from itertools import product

k, m = map(int, input().split())
y = (list(map(int, input().split()))[1:] for _ in range(k))
z = list(map(lambda a:sum(i**2 for i in a)%m,product(*y)))
print(max(z))