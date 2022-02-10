import random

Decide = 1
types = ('Diamonds', 'Spades', 'Cloves', 'Hearts')
cards = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'King', 'Queen', 'Jack', 'Ace')
Key = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
       '9': 9, '10': 10, 'King': 13, 'Queen': 12, 'Jack': 11, 'Ace': 14}


class Keys:

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = Key[rank]

    def value(self):
        return self.value()

    def __str__(self):
        return f'{self.rank} of {self.suit}'


class Deck:
    def __init__(self):
        self.jumbled = []
        for i in types:
            for j in cards:
                self.jumbled.append(Keys(j, i))
        self.a = []
        self.b = []

    def shuffle(self):
        random.shuffle(self.jumbled)
        random.shuffle(self.jumbled)
        random.shuffle(self.jumbled)

    def split_deck(self):
        for _ in range(int(len(self.jumbled) / 2)):
            self.a.append(self.jumbled[0])
            self.jumbled.pop(0)
            self.b.append(self.jumbled[0])
            self.jumbled.pop(0)


class Logic:

    def __init__(self, cards1, cards2):
        self.P1 = cards1
        self.P2 = cards2
        self.place_holder = []

    def winner(self):
        global Decide
        if len(self.P1) == 0:
            print('Player 2 Wins!')
            Decide = 0
        else:
            print('player 1 Wins!')
            Decide = 0

    def equals(self):
        global Decide
        if len(self.P1) < 4 or len(self.P2) < 4:
            if len(self.P1) < 4:
                print('Player 2 Wins!')
                Decide = 0
            else:
                print('Player 1 Wins!')
                Decide = 0
        else:
            for _ in range(3):
                self.place_holder.append(self.P1.pop(0))
                self.place_holder.append(self.P2.pop(0))
            print('Equals = Len = {}'.format(len(self.place_holder)))
            self.checks()

    def checks(self):
        if len(self.P1) == 0 or len(self.P2) == 0:
            self.winner()
        else:
            print(f'Length of P1 = {len(self.P1)}  P2 = {len(self.P2)}')
            x, y = self.P1.pop(0), self.P2.pop(0)
            print(x, ' and ', y)
            print('-------------------')
            self.place_holder.append(x)
            self.place_holder.append(y)
            if x.value > y.value:
                for i in self.place_holder:
                    self.P1.append(i)
                self.place_holder = []
            elif x.value < y.value:
                for i in self.place_holder:
                    self.P2.append(i)
                self.place_holder = []

            else:
                self.equals()


New_Deck = Deck()
New_Deck.shuffle()
New_Deck.split_deck()
Player1 = New_Deck.a
Player2 = New_Deck.b
rounds = 1
while Decide:
    print(rounds)
    p = Logic(Player1, Player2)
    p.checks()
    rounds += 1
