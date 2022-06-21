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