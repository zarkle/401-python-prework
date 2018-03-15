# is_even
def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False


# is_int (is a number an integer (e.g. 7.0)?)
def is_int(x):
    if int(x) - x == 0:
        return True
    else:
        return False


# digit_sum (sum the digits of a number)
def digit_sum(n):
        total = 0
        for digit in str(n):
            total += int(digit)
        return total


# factorial (multiply all the integers from 1 through x)
def factorial(x):
    factorial = 1
    while x > 0:
        factorial *= x
        x -= 1
    return factorial


# is_prime (a positive integer greater than 1 that has no positive divisors other than 1 and itself)
# If there is a number between 1 and x that goes in evenly, then x is not prime. Reminder, all numbers less than 2 are not prime numbers
def is_prime(x):
    print x
    if x < 2:
        return False
    else:
        n = 2
        while n < x - 1:
        if x % n == 0:
            print False
            break
        n += 1
        else:
        print True


# reverse a string
# You may not use "reversed" or [::-1] to help you with this.
def reverse(text):
    reverse = ''
    n = len(text) - 1
    for i in range(len(text)):
        reverse += text[n]
        n -= 1
    return reverse


# anti-vowel (returns string with vowels removed)
def anti_vowel(text):
    no_vowel = ''
    for char in text:
        if char not in 'aeiouAEIOU':
        no_vowel += char
    return no_vowel


# scrabble_score
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}

def scrabble_score(word):
    total = 0
    for char in word.lower():
        total += score[char]
    return total


# censor (return "text" with "word" censored out)
def censor(text, word):
    censor = '*' * len(word)
    lst = text.split()
    for i in range(len(lst)):
        if lst[i] == word:
        lst[i] = censor
    return ' '.join(lst)


# count (count the number of times the "item" occurs in the "sequence" list)
# There is a list method in Python that you can use for this, but you should do it the long way for practice.
# The item you input may be an integer, string, float, or even another list!
def count(sequence, item):
    total = 0
    for each in sequence:
        if each == item:
        total += 1
    return total


# purify (remove all odd numbers from a list of numbers)
def purify(numbers):
    even = []
    for each in numbers:
        if each % 2 == 0:
        even.append(each)
    return even


# product (return the product of all elements in a list of integers)
def product(numbers):
    total = 1
    for each in numbers:
        total *= each
    return total


# remove_duplicates (remove elements of a list that are the same; keep a single occurrence; order of list does not matter)
def remove_duplicates(numbers):
    new = []
    for i in range(len(numbers)):
        if numbers[i] not in new:
        new.append(numbers[i])
    return new


# median (middle number in a sorted sequence of numbers; for an even number of elements, you must average the two elements surrounding the middle; can sort the sequence using the sorted() function)
def median(numbers):
    if len(numbers) < 2:
        return numbers[0]
    numbers = sorted(numbers)
    if len(numbers) % 2 != 0:
        return numbers[int(len(numbers) / 2)]
    else:
        return (numbers[len(numbers) / 2 - 1] + numbers[len(numbers) / 2]) / 2.0 
