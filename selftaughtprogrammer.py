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

# Intersection of two lists, list comprehension
list1 = [2, 43, 48, 62, 64, 28, 3]
list2 = [1, 28, 42, 70, 2, 10, 62, 31, 4, 14]

def return_intersection(list1, list2):
    list3 = [v for v in list1 if v in list2]
    return list3

print(return_intersection(list1, list2))

# Intersection of two lists using sets
list1 = [2, 43, 48, 62, 64, 28, 3]
list2 = [1, 28, 42, 70, 2, 10, 62, 31, 4, 14]

def return_intersection(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return print(list(set1.intersection(set2)))
return_intersection(list1, list2)
