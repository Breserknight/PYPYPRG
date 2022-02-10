import random

suits = ('Diamonds', 'Spades', 'Cloves', 'Hearts')
ranks = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'King', 'Queen', 'Jack', 'Ace')
keys = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
        '9': 9, '10': 10, 'King': 10, 'Queen': 10, 'Jack': 10, 'Ace': 11}


# To use value to compare cards
class Identify:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = keys[rank]

    def __str__(self):
        return f'{self.rank} of {self.suit}'


# creates deck and selecting a card method
class Deck:
    def __init__(self):
        self.deck = []
        for i in suits:
            for o in ranks:
                self.deck.append(Identify(i, o))

    def deal_one(self):
        return self.deck.pop(0)

    def shuffle(self):
        random.shuffle(self.deck)
        random.shuffle(self.deck)
        random.shuffle(self.deck)


# creates player account and money handling methods
class Player:

    def __init__(self):
        self.bank = 500

    def bet(self, amount):
        self.bank -= amount

    def add_money(self, amount):
        self.bank += amount


# game logic
class Logic:

    def __init__(self, player, dealer):
        self.player = player
        self.dealer = dealer
        self.bet_val = 0
        # val1 = sum(player) , val2 = sum(dealer)
        self.val1 = 0
        self.val2 = 0
        # eval is used when value of Ace has to be changed to 1
        self.eval = 0
        # change_check for reducing only one Ace value to 1
        self.change_check = 0

    def check(self):
        if self.val1 >= 21 or self.val2 >= 21:
            if self.val1 == 21 and self.val2 == 21:
                p1.add_money(self.bet_val)
                print(f'-----------------------------\nTie!\nBal = {p1.bank} chips')
                self.bet_val = 0
            elif self.val1 == 21:
                p1.add_money(2*self.bet_val)
                print(f'-----------------------------\nYou Win!\nBal = {p1.bank} chips')
                self.bet_val = 0
            elif self.val2 == 21:
                self.bet_val = 0
                print(f'-----------------------------\nYou Lose!\nBal = {p1.bank} chips')
            elif self.val1 > 21:
                self.bet_val = 0
                print(f'-----------------------------\nYou Lose!\nBal = {p1.bank} chips')
            elif self.val2 > 21:
                p1.add_money(2*self.bet_val)
                self.bet_val = 0
                print(f'-----------------------------\nYou Win!\nBal = {p1.bank} chips')
        else:
            if self.val1 > self.val2:
                p1.add_money(2*self.bet_val)
                self.bet_val = 0
                print(f'-----------------------------\nYou Win!\nBal = {p1.bank} chips')
            elif self.val2 > self.val1:
                self.bet_val = 0
                print(f'-----------------------------\nYou Lose!\nBal = {p1.bank} chips')
            elif self.val2 == self.val1:
                p1.add_money(2*self.bet_val)
                self.bet_val = 0
                print(f'-----------------------------\nTie!\nBal = {p1.bank} chips')

    def comp(self):
        self.eval = 0
        while self.val2 < self.val1:
            if self.val2 >= 21:
                break
            self.dealer.append(new.deal_one())
            sum2 = 0
            for i in self.dealer:
                sum2 += i.value
            self.val2 = sum2
            if self.val2 > 21 and self.change_check != 2:
                for i in self.dealer:
                    if i.rank == 'Ace':
                        self.eval = -10
                        break
                self.change_check = 2
            self.val2 += self.eval
            print(f'-----------------------------\nYour Hand : [below] , Val = {self.val1}')
            for i in self.player:
                print(i)
            print(f'-----------------------------\nDealers : [below], Val = {self.val2}')
            for i in self.dealer:
                print(i)
        self.check()

    def play(self):
        
        x = int(input('1-Hit\n2-Check\n3-Bet\n'))
        if x == 1:
            self.player.append(new.deal_one())
            self.initialize()
        elif x == 2:
            self.comp()
        elif x == 3:
            while True:
                y = int(input(f'Balance = {p1.bank}\nEnter Chips -- '))
                if y > p1.bank:
                    print('Exceeds limit!!')
                    continue
                break
            p1.bet(y)
            self.bet_val += y
            self.player.append(new.deal_one())
            self.initialize()
        else:
            print('Enter 1 / 2 / 3 ONLY')
            self.play()

    def initialize(self):

        sum1 = 0
        for i in self.player:
            sum1 += i.value
        self.val1 = sum1
        if self.val1 > 21:
            if self.change_check == 0:
                for i in self.player:
                    if i.rank == 'Ace':
                        self.eval = -10
                        self.change_check = 1
                        break
        self.val1 += self.eval
        print(f'-----------------------------\nYour Hand : [below] , Val = {self.val1}')
        for i in self.player:
            print(i)
        print(f'-----------------------------\nDealers : [{self.dealer[0]},Hidden],'
              f' Val = Hidden')
        if self.val1 > 21:
            self.check()
        elif self.val1 == 21:
            self.comp()
        else:
            self.play()


# crete deck and start the game
new = Deck()
new.shuffle()
p1 = Player()
while True:
    a = []
    b = []
    # bet = initial_bet
    while True:
        bet = int(input(f'-----------------------------\nBalance          = {p1.bank} Chips\nEnter Bet Amount = '))
        if bet > p1.bank:
            print('Exceeds limit!!')
            continue
        break
    p1.bet(bet)
    for _ in range(2):
        a.append(new.deal_one())
        b.append(new.deal_one())
    game = Logic(a, b)
    game.bet_val += bet
    game.initialize()
    # next 2 lines reset the Ace value to 11 [technically]
    game.change_check = 0
    game.eval = 0
    choice = int(input('-----------------------------\nKeep Playing?\n1 - Yes , 2 - No\n'))
    if choice == 1:
        continue
    else:
        break
