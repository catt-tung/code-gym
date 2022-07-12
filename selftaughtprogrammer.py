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
