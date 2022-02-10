class SORT:

    def __init__(self, var):
        self.x = var

    def sort1(self):
        b = self.x
        s = []
        while True:
            d = b[0]
            for i in b:
                if d < i:
                    continue
                else:
                    d = i
            s.append(d)
            b.remove(d)
            if len(b) == 0:
                break
        return s


x = list(map(int,input().split()))
x = SORT(x)
x = x.sort1()
print(x)