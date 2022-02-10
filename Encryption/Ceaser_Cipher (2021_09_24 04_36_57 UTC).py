ans = ['encode', 'decode']

while True:
    x = input("Enter 'encode' to encrypt and 'decode' to decrypt : ").strip()
    if x.lower() in ans:
        break
    else:
        print('Invalid Input!!')

def condf(choice, string, shift):
    new_string = ""
    if shift > 26:
        shift = shift - round(shift/26) * 26
    sig = -1
    if choice == ans[1]:
        sig = +1
        shift *= -1
    for i in string:
        ascii_val_new = ord(i) + shift 
        if ascii_val_new > 122:
            ascii_val_new += sig * 26
        new_string += chr(ascii_val_new)

print(condf(x, input('Enter the string : '), int(input('Shift Key Value :'))))