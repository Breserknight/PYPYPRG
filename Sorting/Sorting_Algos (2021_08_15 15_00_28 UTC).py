class Sort:

    def __init__(self, x):
        self.x = x

    def insertion_sort(self):
        for i in range(1, len(self.x)):
            temp = self.x[i]
            n = i - 1
            counter = i
            while n >= 0:
                if self.x[n] > self.x[counter]:
                    self.x[counter] = self.x[n]
                    self.x[n] = temp
                    n -= 1
                    counter -= 1
                else:
                    n -= 1
                    counter -= 1
        return self.x

    def regular_sort(self):
        new = []
        while len(self.x) > 0:
            temp = self.x[0]
            for i in range(len(self.x)):
                if temp > self.x[i]:
                    temp = self.x[i]
                else:
                    pass
            new.append(temp)
            self.x.remove(temp)
        return new


c = Sort(list(map(int, input('Enter Elements To Be Sorted\n').split())))
choice = int(input('Enter\n1 --> Insertion sort\n2 --> Regular sort\n'))
if choice == 1:
    print(c.insertion_sort())
elif choice == 2:
    print(c.regular_sort())
else:
    print('Fatal Error')
