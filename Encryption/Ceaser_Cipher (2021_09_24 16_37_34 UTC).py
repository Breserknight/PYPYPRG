ans = ['encode', 'decode']

while True:
    x = input("Enter 'encode' to encrypt and 'decode' to decrypt : ").strip()
    if x.lower() in ans:
        break
    else:
        print('Invalid Input!!')


def cf(choice, string, shift):
    new_string = ""
    cpy = string
    string = string.lower()
    if shift > 26:
        shift = shift - round(shift/26) * 26
    if choice == ans[1]:
        shift *= -1
    for i in range(len(string)):
        if string[i] == ' ':
            new_string += ' '
            continue
        ascii_val_new = ord(string[i]) + shift
        if ascii_val_new > 122 or ascii_val_new < 97:
            if ascii_val_new > 122:
                ascii_val_new -= 25
            elif ascii_val_new < 97:
                ascii_val_new += 25
        if cpy[i].upper() == cpy[i]:
            new_string += chr(ascii_val_new).upper()
        else:
            new_string += chr(ascii_val_new)
    return new_string


string1 = input('Enter your string : ')
shift1 = int(input('Enter Key Value : '))
print(cf(x.lower(), string1, shift1))