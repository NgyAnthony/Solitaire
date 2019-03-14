import random


class Card:
    def __init__(self, suits, number):
        self.suits = suits
        self.number = number

    def __repr__(self):
        return "Card('{}', '{}')".format(self.suits, self.number)


class Dealer:
    def __init__(self):
        self.number = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13")
        self.suits = ("Clover", "Diamond", "Heart", "Spade")

        self.initialize_deck()



    def initialize_deck(self):
        for suits in self.suits:
            for number in self.number:
                card = Card(suits, number)
                a_board.deck.append(card)

    def make_readable(self):
        self.readable_path = "{}/{}".format(self.suits, self.number)

    def get_card(self):
        return a_board.deck.pop(random.randint(0, len(a_board.deck) -1))

class Board:
    def __init__(self):
        self.stack = [[None, None, None, None, None, None, None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None, None, None, None, None, None, None]]

        self.grid = [[None, None, None, None, None, None, None],
                     [None, None, None, None, None, None, None],
                     [None, None, None, None, None, None, None],
                     [None, None, None, None, None, None, None],
                     [None, None, None, None, None, None, None],
                     [None, None, None, None, None, None, None],
                     [None, None, None, None, None, None, None]]

        self.deck = []

    def __str__(self):
        return "\n{}\n{}\n{}\n{}\n{}\n{}\n{}".format(self.grid[0], self.grid[1], self.grid[2],
                                                                self.grid[3], self.grid[4], self.grid[5],
                                                                self.grid[6])

    def initial_distribution(self):
        row = 7
        for col in range(len(self.grid)):
            for x in range(0, row):
                random_card = a_dealer.get_card()
                self.grid[x][col] = random_card
            row -= 1

a_board = Board()
a_dealer = Dealer()
a_board.initial_distribution()
print(a_board)
