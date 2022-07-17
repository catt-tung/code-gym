#Hangman
def hangman(word):
    wrong = 0
    stages = ["",
             "________        ",
             "|               ",
             "|        |      ",
             "|        0      ",
             "|       /|\     ",
             "|       / \     ",
             "|               "
              ]
    rletters = list(word)
    board = ["__"] * len(word)
    win = False
    print("Welcome to Hangman")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess a letter"
        char = input(msg)
        if char in rletters:
            cind = rletters \
                   .index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n"
              .join(stages[0: e]))
        if "__" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n"
              .join(stages[0: \
              wrong]))
        print("You lose! It was {}."
              .format(word))

hangman("cat")

# OOP intro - circle and triangle area
import math
class Circle:
    def __init__(self, r):
        self.radius = r
    def area(self):
        return math.pi * (self.radius ** 2)

cir1 = Circle(10)
print(cir1.area())

class Triangle:
    def __init__(self, w, h):
        self.width =  w
        self.height = h
    def area(self):
        return (self.width * self.height)/2

tri1 = Triangle(3, 4)
print(tri1.area())


#Class variables
class Rectangle():
    recs = []

    def __init__(self, w, l):
        self.width = w
        self.len = l
        self.recs.append((self.width, self.len))

    def print_size(self):
        print("""{} by {}
            """.format(self.width, self.len))

r1 = Rectangle(10, 24)
r2 = Rectangle(20, 40)
r3 = Rectangle(100,200)

print(Rectangle.recs)
#(result is [(10, 24), (20, 40), (100, 200)])

class Shape():
    def what_am_i(self):
        print("I am a shape.")

#https://github.com/calthoff/tstp/tree/master/part_II/more_object_oriented_programming/challenge
class Square(Shape):
    square_list = []

    def __init__(self, s1):
        self.s1 = s1
        self.square_list.append(self)

    def calculate_perimeter(self):
        return self.s1 * 4

    def what_am_i(self):
        super().what_am_i()
        print("I am a Square.")


a_square = Square(29)
print(Square.square_list)
another_square = Square(93)
print(Square.square_list)

#War
class Card:
    suits = ("spades", "hearts", "diamonds", "clubs")
    
    values = (None, None, "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace")
    #the 2 None values are so that the indices match up for the numbers 2-10

    def __init__(self, v, s):
        """suit + value are ints"""
        self.value = v
        self.suit = s

    def __lt__(self, c2):
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
        return False

    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        return False

#look up value of suit and card to print the card a Card object represents
    def __repr__(self):
        v = self.values[self.value]+\
            " of " + \
            self.suits[self.suit]
        return v

# define a class to represent a deck of cards
from random import shuffle
class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards\
                    .append(Card(i, j))
        shuffle(self.cards)

    def rm_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()

deck = Deck()
for card in deck.cards:
    print(card)

# define a player class
class Player:
    def __init__(self, name):
        self.wins = 0
        self.card = None
        self.name = name

# define a class to represent the game
class Game:
    def __init__(self):
        name1 = input("player 1 name ")
        name2 = input("player 2 name ")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    def wins(self, winner):
        w = "{} wins this round"
        w = w.format(winner)
        print(w)

    def draw(self, p1n, p1c, p2n, p2c):
        d = "{} drew {} {} drew {}"
        d = d.format(p1n,
                    p1c,
                    p2n,
                    p2c)
        print(d)

    def play_game(self):
        cards = self.deck.cards
        print("beginning War!")
        while len(cards) >= 2:
            m = "q to quit. Any " +\
                "key to play:"
            response = input(m)
            if response == 'q':
                break
            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            p1n = self.p1.name
            p2n = self.p2.name
            self.draw(p1n,
                    p1c,
                    p2n,
                    p2c)
            if p1c > p2c:
                self.p1.wins += 1
                self.wins(self.p1.name)
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)

        win = self.winner(self.p1,
                        self.p2)
        print("War is over. {} wins"
            .format(win))

        def winner(self, p1, p2):
            if p1.wins > p2.wins:
                return p1.name
            if p1.wins < p2.wins:
                return p2.name
            return "It was a tie!"