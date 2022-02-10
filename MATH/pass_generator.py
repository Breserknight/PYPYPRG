import random
import os
import zipfile


while True:
    while True:
        password = []

        tot_num = int(input('How many letters do you need in your password\n'))
        no_num = int(input('How many numbers do you need in your password\n'))
        sp_num = int(input('How many special characters do you need in your password\n'))

        letters = ('q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c',
                'v', 'b', 'n', 'm', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K',
                'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M')
        numbers = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
        special_char = ('~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '[', ']', '{', '}', '|', ';',
                        ':', ',', '.', '?')

        for i in range(tot_num):
            password.append(letters[random.randint(0, len(letters)-1)])

        for i in range(no_num):
            password.append(numbers[random.randint(0, len(numbers)-1)])

        for i in range(sp_num):
            password.append(special_char[random.randint(0, len(special_char)-1)])

        random.shuffle(password)

        print(f'Your Password is : {"".join(password)}')
        if(input("Do you wish to use this Password ?\nPress y/n : ")) in ['y', 'Y']:
            break


    while True:
        usr = input("Enter UserName : ")
        site = input("Enter Website : ")
        if(input("Do you wish to use this Username and Website?\nPress y/n : ")) in ['y', 'Y']:
            break

    with zipfile.ZipFile("pop.zip", "r") as zip:
        zip.extract("caliber.txt")

    with open("caliber.txt", "r") as f:
        line = f.read().splitlines()

    with open("caliber.txt", "a+") as file:
        SI = int(line[-1].split()[0]) + 1
        file.write(f"\n\n{SI}\t\t{usr}\t\t\t{''.join(password)}\t\t\t{site}")

    with zipfile.ZipFile("pop.zip", "w") as zip:
        zip.write("caliber.txt")

    os.remove("caliber.txt")

    print("PassWord SAvEd !")
    if input("Add Another Password?\npress y/n : ") not in ["y", "Y"]:
        break