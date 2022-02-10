bits = [0 for _ in range(12)]
with open("./AdventOfCode/text.txt", "r") as file:
    for line in file:
        c = 0
        for i in line.strip():
            if int(i):
                bits[c] += 1
            c += 1

print(bits)

bit1 = [1 if i > 500 else 0 for i in bits]
bit2 = [0 if i else 1 for i in bit1]
print(bit1)
print(bit2)
def convert(bit):
    num = 0
    deg = 11
    for i in bit:
        num += 2 ** deg * i
        deg -= 1
    return num

print(convert(bit1) * convert(bit2))