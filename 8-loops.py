#note, print function is in py2 and py3 syntax

# while loop
while count < 5:
    print "Hello, I am a while and count is", count
    count += 1


# condition
while loop_condition:
    print "I am a loop"
    loop_condition = False


# break
count = 0

while True:
    print count
    count += 1
    if count >= 10:
        break


# while/else
import random

print "Lucky Numbers! 3 numbers will be generated."
print "If one of them is a '5', you lose!"

count = 0
while count < 3:
    num = random.randint(1, 6)
    print num
    if num == 5:
        print "Sorry, you lose!"
        break
    count += 1
else:
    print "You win!"


# while/else
from random import randint

random_number = randint(1, 10) # Generates a number from 1 through 10 inclusive

guesses_left = 3

while guesses_left > 0:
    guess = int(raw_input('Your guess: '))
    if guess == random_number:
        print('You win!')
        break
    guesses_left -= 1
else:
    print('You lose.')


# for loop
for i in range(10):
    print i


# for loop to append to list
hobbies = []

for i in range(3):
    hobby = raw_input('Your hobby: ')
    hobbies.append(hobby)
print(hobbies)


# for loop with strings
phrase = "A bird in the hand..."


# Add your for loop
for char in phrase:
    if char == 'A' or char == 'a':
        print('X'),
  else:
     print(char),

print


# for loop to iterate through a list
numbers  = [7, 9, 12, 54, 99]

for num in numbers:
    print num


# for loop over a dictionary
d = {'x': 9, 'y': 10, 'z': 20}
for key in d:
    if d[key] == 10:
        print "This dictionary has the value 10!"


# for loop over a dictionary
d = {'a': 'apple', 'b': 'berry', 'c': 'cherry'}

for key in d:
    print(key, d[key])


# enumerate (gives an index to each element in a list)
choices = ['pizza', 'pasta', 'salad', 'nachos']

print 'Your choices are:'
for index, item in enumerate(choices):
    print((index + 1), item)


# zip (iterate over multiple lists)
list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

for a, b in zip(list_a, list_b):
    print(max(a, b))


# for/else
fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

print 'You have...'
for f in fruits:
    if f == 'tomato':
        print 'A tomato is not a fruit!' # (It actually is.)
        break
    print 'A', f
else:
    print 'A fine selection of fruits!'