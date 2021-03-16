# PYTHON EXERCISES - Day One (Variables - Keyboard Input)
# ---------------------
# Make a Python program that prints your name.
print("Conor Sosh")

# Make a program that displays the lyrics of a song.
print("What if I say I'm not like the others?")
print("What if I say I'm not just another one of your plays?")
print("You're the pretender.")
print("What if I say I will never surrender?")

# Variables
# Make a program that displays several numbers.
print(9)
print(74)
print(45, 86, 24, 25)

# Make a program that solves and shows the summation of 64 + 32.
print(64 + 32)

# Do the same as in 2, but make it sum x + y.
x = 64
y = 32
print(x + y)

# Strings
# Make a program that displays your favourite actor/actress.
print("Edward Bosco")

# Try to print the word „lucky‟ inside s.
s = "My lucky number is 7, what is yours?"
print(s[3:8])

# Try to print the day, month, year in the form “Today is 2/2/2016”.
date = "3/15/2021"
print(f"Today is {date}")

# String replace
# Try the replace program
string = "Hello world!"
newString = string.replace("Hello", "Howdy")
print(string)
print(newString)

# Can a string be replaced twice?
# Yes

# Does replace only work with words or also phrases?
# You can replace any substring with a new substring

# String find
# Find out if string find is case sensitive
# string.find IS case sensitive
string = "Hello world!"
print(string.find("h"))
# Returns -1, which means "h" was not found

# What if a query string appears twice in the string?
# It returns the first occurance of the string/substring
string = "Hello world!"
print(string.find("l"))
# Returns 2, the first location of the first "l"

# Write a program that asks console input and searches for a query.
string = "Hello world!"
userInput = input("What substring are you searching for?\n> ")
print(string.find(userInput))

# String join
# Create a list of words and join them, like the example above.
stringOne = "Here is a"
stringTwo = "couple of strings"
sequence = (stringOne, stringTwo)
print(" ".join(sequence))

# Try changing the separator string from a space to an underscore.
stringOne = "Here is a"
stringTwo = "couple of strings"
sequence = (stringOne, stringTwo)
print("_".join(sequence))

# String split
# Can a string be split on multiple characters?
string = "Here is a pretty long string, should be good for testing; I have no idea how to use semicolons, maybe I should look that up."
print(string.split(", "))
# You can split on multiple characters, but they have to be in a sequence. For example ", "

# Can you split a string this string?: World,Earth,America,Canada
string = "World,Earth,America,Canada"
print(string.split(","))

# Given an article, can you split it based on phrases?
# Yes

# Random numbers
# Make a program that creates a random number and stores it into x.
import random
x = random.randint(0, 100)
print(x)

# Make a program that prints 3 random numbers.
print(random.randint(0, 100))
print(random.randint(0, 100))
print(random.randint(0, 100))

# Create a program that generates 100 random numbers and find the frequency of each number.
import collections
i = 0
size = 100
randomList = []
for i in range(size):
    randomList.append(random.randint(0, 100))

count = collections.Counter(randomList)

print(count)

# Keyboard input
# Make a program that asks a phone number.
input("Please enter your phone number:\n > ")

# Make a program that asks the users preferred programming language.
input("Please enter your preferred programming language:\n > ")
