# saving my equations from studying self-taught computer scientist

# Ch4 Sorting Algorithms
# insertion sort
def insertion_sort(a_list):
    for i in range(1, len(a_list)):
        value = a_list[i]
        while i>0 and a_list[i-1] > value:
            a_list[i] = a_list[i-1]
            i = i-1
        a_list[i] = value
    return print(a_list)
insertion_sort([3, 5, 1, 7, 6, 9, 0])

# merge sort
def merge_sort(a_list):
    if len(a_list) > 1:
        mid = len(a_list) // 2
        left_half = a_list[:mid]
        right_half = a_list[mid:]
        merge_sort(left_half)
        merge_sort(right_half)

        left_ind = 0
        right_ind = 0
        alist_ind = 0
        while left_ind < len(left_half) and right_ind < len(right_half):
            if left_half[left_ind] <= right_half[right_ind]:
                a_list[alist_ind] = left_half[left_ind]
                left_ind += 1
            else:
                a_list[alist_ind] = right_half[right_ind]
                right_ind += 1
            alist_ind += 1

        while left_ind < len(left_half):
            a_list[alist_ind] = left_half[left_ind]
            left_ind += 1
            alist_ind += 1

        while right_ind < len(right_half):
            a_list[alist_ind]= right_half[right_ind]
            right_ind += 1
            alist_ind += 1
    return a_list

#Anagram
def is_anagram(str1, str2):
    str1 = str1.replace(' ','').lower()
    str2 = str2.replace(' ','').lower()
    if sorted(str1) == sorted(str2):
        return True
    else:
        return False

print(is_anagram('Tom Marvolo Riddle', 'I am Lord Voldemort'))

#Palindrome
def is_palindrome(str):
    if str[::-1] == str:
        return True
    else: return False

#Last Digit
def last_digit(str):
    nums = [c for c in str if c.isdigit()]
    return nums[-1]

print(last_digit("Buy 1 get 2 free"))

import string
#Caeser Cipher
def caeser_cipher(str, key):
    encrypted_message = ""
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    for c in str:
        if c in uppercase:
            new = (uppercase.index(c) + key) % 26
            encrypted_message += uppercase[new]
        elif c in lowercase:
            new = (lowercase.index(c) + key) % 26
            encrypted_message += lowercase[new]
        else:
            encrypted_message += c
    return encrypted_message

print(caeser_cipher("Come before six oclock", 4))

# Function to evaluate if a number is even or odd:
def is_even(n):
    return not n & 1

# Fizzbuzz
def fizzbuzz():
    for i in range (1, 100):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

#Greatest Common Factor
def gcf(int1, int2):
    if int1 < 0 or int2 < 0:
        raise ValueError("Numbers must be positive")
    gcf = None
    if int1 == 0:
        gcf = int2
    if int2 == 0:
        gcf = int2

    if int1 > int2:
        smaller = int2
    else:
        smaller = int1
    for i in range (1, smaller + 1):
        if int1 % i == 0 and int2 % i == 0:
            gcf = i
    return print(gcf)

#Greatest Common Factor Euclid's Algorithm
def gcf_euclid(x, y):
    if y == 0:
        x, y = y, x
    while y != 0:
        x, y, = y, x % y
    return print(x)

#Prime numbers - linear
def is_prime(n):
    for i in range (2, n):
        if n % i == 0:
            return print(False)
        return print(True)

#Prime numbers - logarithmic, find primes
import math

def is_prime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return print(False)
    return print(True)

def find_primes(n):
    return [is_prime(i) for i in range(2,n)]

#Ch 9 Arrays
#Move zeros
def move_zeroes(the_list):
    zero_index = 0
    for index, n in enumerate(the_list):
        if n != 0:
            the_list[zero_index] = n
            if zero_index != index:
                the_list[index] = 0
            zero_index += 1
    return(the_list)

the_list = [8, 0, 3, 0, 12]
move_zeroes(the_list)
print(the_list)

#Combining lists
def combine_lists(list_one, list_two):
    new_list = list(zip(list_one, list_two))
    return print(new_list)

list_one = ["one", "two", "three"]
list_two = [1, 2, 3]
combine_lists(list_one, list_two)

# Finding duplicates - making use of Python sets
def find_duplicates(any_iterable):
    duplicates = []
    a_set = set()

    for item in any_iterable:
        l1 = len(a_set)
        a_set.add(item)
        l2 = len(a_set)
        if l1 == l2:
            duplicates.append(item)
    return print(duplicates)

a_list = ["joe", "jimmy", "joe", "john", "jack", "jeremy", "john"]
find_duplicates(a_list)

#Intersection of lists methods
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

#Sorting an array, evens first, odds in the end
import array
an_array = array.array('i', [1, 28, 42, 70, 2, 10, 62, 31, 4, 14])

def return_sorted_nums(an_array):
    new_array = []
    for num in an_array:
        if num % 2 == 0:
            new_array.insert(0, num)
        else:
            new_array.append(num)
    return(print(array.array('i', new_array)))

return_sorted_nums(an_array)

#Creating a linked list
class Node:
    def__init__(self, data, next=None):
        self.data = data
        self.next = next
