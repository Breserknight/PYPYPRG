import random


def pt(a):
    if a == 6:
        return ' +---------+\n "         |\n           |\n           |\n           |\n           |\n ============'  
    elif a == 5:
        return ' +---------+\n "         |\n O         |\n           |\n           |\n           |\n ============'  
    elif a == 4:
        return ' +---------+\n "         |\n O         |\n |         |\n           |\n           |\n ============'  
    elif a == 3:
        return ' +---------+\n "         |\n O         |\n/|         |\n           |\n           |\n ============'  
    elif a == 2:
        return ' +---------+\n "         |\n O         |\n/|\        |\n           |\n           |\n ============'  
    elif a == 1:
        return ' +---------+\n "         |\n O         |\n/|\        |\n/          |\n           |\n ============'  
    elif a == 0:
        return ' +---------+\n "         |\n O         |\n/|\        |\n/ \        |\n           |\n ============'  


count = 0
dictionary = ['Apple', 'Mango', 'Banana', 'Kawasaki', 'Hyundai']
while True:
    if count == 0:
        past_guesses = []
        life = 6
        y = dictionary[random.randint(0, len(dictionary)-1)]
        x = [i for i in y]
        s = ['_ ' for _ in range(len(x))]
        p = x[0]
        for i in range(len(x)):
            if x[i] == p:
                s[i] = x[i]
                x[i] = '0'
        past_guesses.append(p.lower())
        count = 1
    print('\n'*5)
    print(''.join(s), '\n HANGMAN')
    print(pt(life))

    if life <= 0:
        print('You Lost')
        print(f'Your Answer was {y}')
        i = input('Continue ?\n1 - Yes\n2 - No\n')
        if i == '1':
            count = 0
            continue
        else:
            print('Thank You For Playing!')
            break
    print('past guesses', past_guesses, '\n-----------------------------------')
    choice = input('Enter Your Letter\n')
    if choice.lower() in past_guesses:
        print('Already Guessed\n')
        continue
    if choice not in x:
        past_guesses.append(choice.lower())
        life -= 1
        print('Not There')
        continue
    past_guesses.append(choice.lower())
    for i in range(len(x)):
        if x[i].lower() == choice.lower():
            s[i] = choice.lower()
            x[i] = '0'
    if len(set(x)) == 1:
        print("You've Won!")
        print(f"Answer was \n--------------------------\n{y}\n--------------------------\nAnd you've guessed it")
        i = input('Continue ?\n1 - Yes\n2 - No\n')
        if i == '1':
            count = 0
            continue
        else:
            print('Thank You For Playing!')
            break
