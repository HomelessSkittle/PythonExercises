# PYTHON EXERCISES
# ---------------------
def run_python_programs():
  # Make a Python program that prints your name.
  print("Conor Sosh")

  # Make a program that displays the lyrics of a song.
  print("""What if I say I'm not like the others?
What if I say I'm not just another one of your plays?
You're the pretender.
What if I say I will never surrender?""")

def variables():
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

def strings():
  # Make a program that displays your favourite actor/actress.
  print("Edward Bosco")

  # Try to print the word „lucky‟ inside s.
  s = "My lucky number is 7, what is yours?"
  print(s[3:8])

  # Try to print the day, month, year in the form “Today is 2/2/2016”.
  date = "3/15/2021"
  print(f"Today is {date}")

def string_replace():
  # Try the replace program
  string = "Hello world!"
  newString = string.replace("Hello", "Howdy")
  print(string)
  print(newString)

  # Can a string be replaced twice?
  # Yes and No. Strings are immutable, so to if you replace the same string twice, you won't have the the intermediate changes. To do that, you would need to save the result of the first string replace as a variable, then do another string replace on that.

  # Does replace only work with words or also phrases?
  # You can replace any substring with a new substring

def string_find():
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

def string_join():
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

def string_split():
  # Can a string be split on multiple characters?
  string = "Here is a pretty long string, should be good for testing; I have no idea how to use semicolons, maybe I should look that up."
  print(string.split(", "))
  # You can split on multiple characters, but they have to be in a sequence. For example ", "

  # Can you split a string this string?: World,Earth,America,Canada
  string = "World,Earth,America,Canada"
  print(string.split(","))

  # Given an article, can you split it based on phrases?
  # Yes

def random_numbers():
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

def keyboard_input():
  # Make a program that asks a phone number.
  input("Please enter your phone number:\n> ")

  # Make a program that asks the users preferred programming language.
  input("Please enter your preferred programming language:\n> ")

def if_statements():
  # Make a program that asks the number between 1 and 10. If the number is out of range, the program should display invalid number
  answer = int(input("Please give a number between 1 and 10\n> "))

  if (answer < 0 or answer > 10):
    print("Invalid number")
  else:
    print("Good choice!")

  # Make a program that asks a password
  password = input("What's the password? Hint: It's password123\n> ")

  if password == "password123":
    print("Correct!")
  else:
    print("Incorrect.")

def for_loops():
  # Make a program that lists the countries in the set clist = ['Canada','USA','Mexico','Australia']
  clist = ['Canada','USA','Mexico','Australia']
  for country in clist:
    print(country)

  # Create a loop that counts from 0 to 100
  x = range(101)
  for i in x:
    print(i)

  # Make a multiplication table using a loop 
  x = range(13)
  for i in x:
    print(str(i) + " times 12 is: " + str((i * 12)))

  # Output the numbers 1 to 10 backwards using a loop
  x = range(10, 0, -1)
  for i in x:
    print(i)

  # Create a loop that counts all even numbers to 10
  x = range(11)
  for i in x:
    if i % 2 == 0:
      print(i)

  x = range(100, 201)
  sum = 0
  for i in x:
    sum += i
  print(sum)

def while_loops():
  # Make a program that lists the countries in the set using a while loop  
  clist = ["Canada", "USA", "Mexico"]
  index = 0
  while index < len(clist):
    print(clist[index])
    index += 1
  
  # What's the difference between a while loop and a for loop?
  # A for loop has predefined conditions for beginning and ending when you create it.
  # A while loop will continuously go through the loop body until some loop condition is satisfied. Note: It is possible to make an infinite loop if the condition is not well defined.

  # Can you sum numbers in a while loop?
  # Yes
  nlist = [2, 5, 2, 9, 10, 28, 4]
  index = 0
  sum = 0
  while index < len(nlist):
    sum += nlist[index]
    index += 1
  print(sum)

  # Can a for loop be used in a while loop?
  # Yes
  example_string = "*"
  while_control = 0
  while while_control < 5:
    print("While Loop Iteration #" + str(while_control))
    for_control = range(while_control + 1)
    for i in for_control:
      print(example_string * i)
    while_control += 1

# These are just some helper functions used as examples for the functions section below
def functions_example_two():
  print("Hello from functions_example_two!")

def functions_example():
  functions_example_two()
  print("Howdy from functions_example!")

def factorial(input_num):
  if input_num == 1:
    return input_num
  elif input_num < 1:
    return(1)
  else:
    return (input_num * factorial(input_num - 1))

def functions():
  # Make a function that sums the list my_list = [1,2,3,4,5]
  sum = 0
  my_list = [1,2,3,4,5]
  for num in my_list:
    sum += num
  print(sum)

  # Can functions be called inside a function?
  # Yes
  functions_example()

  # Can a function call itself?
  # Yes
  print (factorial(5))

  # Can variables defined in a function be used in another function?
  # No, because they were defined in one function, they cannot be used in another, unless you are passing them as parameters, but that is not quite the same thing.

def lists():
  # Make a program that displays the states in the US
  state_list = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]

  for state in state_list:
    print(state)

  print()
  # Display all states starting with the letter M
  for state in state_list:
    if state[0] == "M":
      print(state)

def list_operations():
  # Given the list y = [6,4,2] add the items 12, 8 and 4
  y = [6, 4, 2]
  y.append(12)
  y.append(8)
  y.append(4)

  for num in y:
    print(num)
  
  # Change the 2nd item of the list to 3
  y[1] = 3

  for num in y:
    print(num)

# Below are a couple of helper functions for sorting a list of pairs
def selectFirst(item):
  return (item[0])

def selectSecond(item):
  return (item[1])

def sorting_list():
  # Given a list with pairs sort on the first element
  x = [(3,6), (4,7), (5,9), (8,4), (3,1)]
  x.sort(key=selectFirst)
  print(x)

  # Given a list of pairs, sort on the second element
  x.sort(key=selectSecond)
  print(x)

def range_function():
  import random
  # Create a list of one thousand numbers
  list = []
  for i in range(1000):
    list.append(random.randint(0, 100000))

  # Get the largest and smallest number from that list
  largest = -999
  smallest = 999
  for num in list:
    if num > largest:
      largest = num
    if num < smallest:
      smallest = num

  print("The largest number is: " + str(largest))
  print("The smallest number is: " + str(smallest))

  # Create two lists, an even and an odd open
  even_list = []
  odd_list = []
  for i in range(30):
    if i % 2 == 0:
      even_list.append(i)
    else:
      odd_list.append(i)
  
  print("Even list:")
  print(even_list)
  print("Odd list:")
  print(odd_list)

def dictionary():
  country_dictionary = {
    "USA": "United States",
    "GER": "Germany",
    "CAN": "Canada",
    "MEX": "Mexico",
    "ITA": "Italy"
  }

  print(country_dictionary)

def read_file():
  # Read a file and number every line
  file = open("testopen.txt", "r")
  lines = file.readlines()

  line_number = 0
  for line in lines:
    line_number += 1
    print("Line{}: {}".format(line_number, line.strip()))

  # Find out what happens if the file doesn't exist.
  # You get a FileNotFoundError

  # What happens if you create a file with another user and try to open it?
  # Depending on your permissions, you may or may not be able to open the file.

def write_file():
  # Write the text "Take it easy" to a file.
  file = open("testwrite.txt", "w")
  file.write("Take it easy")

  # Write the line open("text.txt") to a file
  file = open("newfile.txt", "w")
  file.write("""open("text.txt")""")

def nested_loops():
  # Given a tic-tac-toe board of 3x3, print every position
  for i in range(3):
    for j in range(3):
      print(i, j, end = " ")
      print("|", end = " ")
    print("")
    print("-----------------")

  # Create a program where every person meets the other
  persons = ["John", "Marissa", "Pete", "Dayton"]
  i = 0
  while i < len(persons):
    j = i + 1
    while j < len(persons):
      print (persons[i] + " met " + persons[j])
      j += 1
    i += 1

  # If a normal for loop finishes in n steps, it has O(n) complexity. How many steps does a nested loop have?
  # It would have n^2 steps.

def slices():
  # Take a slice of the list below
  pizzas = ["Hawaii", "Pepperoni", "Fromaggi", "Napolitani", "Diavoli"]
  print(pizzas[1:2])

  # Given the text "Hello World", take the slice "World"
  text = "Hello World"
  print(text[6:11])

def multi_return_example():
  a = 12
  b = 8
  return a, b, a+b

def multi_return_example_two():
  one = 1
  two = 2
  three = 3
  four = 4
  five = 5
  return one, two, three, four, five

def multiple_return():
  # Create a function that returns a, b, and a+b
  c, d, e = multi_return_example()
  print(c)
  print(d)
  print(e)

  # Create a function that returns five variables
  six, seven, eight, nine, ten = multi_return_example_two()
  print(six, seven, eight, nine, ten)

def reduce_amount(withdrawl):
  balance = 10000
  balance = balance - withdrawl
  print(balance)

def scope():
  #Add a function reduce amount that changes the variable balance
  reduce_amount(5000)
  reduce_amount(300)

  # Create a function with a local variable
  # We just did that up above

def time_and_date():
  import time
  # Print the date in format year-month-day

  curr_time = time.localtime(time.time())
  year, month, day = curr_time[0:3]

  print(str(year) + "/" + str(month) + "/" + str(day))

def try_except():
  # Can try-except be used to catch invalid keyboard input?
  # Yes
  try:
    x = int(input("Enter a number: "))
    x = x + 1
    print(x)
  except:
    print("Invalid input.")

  # Can try-except catch the error if a file can't be opened?
  # Yes
  try:
    file = open("trytest.txt", "r")
    print("Opened the file!")
  except FileNotFoundError:
    print("The file doesn't exist.")

  # When would you not use try-except?
  # When writing a complex program, where an error might pop up at several points. Try except blocks can mask otherwise helpful error messages. Or if we don't raise any particular excpetion, we won't be getting any useful report from our except statement.
class Website:
  def __init__(self, title):
    self.title = title
    self.location = "the internet"
  
  def showTitle(self):
    print(self.title)

  def showLocation(self):
    print(self.location)

  def updateLocation(self, new_location):
    self.location = new_location

def class_example():
  # Can you have more than one class in a file?
  # Yes you can, but depending on the project, it might be a bad idea, and make things confusing to read

  # Can multiple objects be created from the same class?
  # Yes, you can create as many objects as you want from a single class

  # Can objects create classes?
  # No, objects are derived from classes, not the other way around.

  # Using the code above create another object
  obj_one = Website('pythonbasics.org')
  obj_one.showTitle()

  #Add a method to the class: location()
  obj_one.showLocation
  obj_one.updateLocation("the world wide web")
  obj_one.showLocation

class Person:
  def __init__(self):
    self.name = "Conor"
    self.age = "21"

  def getName(self):
    return self.name
  
  def getAge(self):
    return self.age
  
  def setName(self, new_name):
    self.name = new_name
  
  def setAge(self, new_age):
    self.age = new_age

def getter_and_setter():
  # Add a variable age and create a getter and setter
  # original code:
  """
  class Person:
  def __init__(self):
    self.name = "Conor"
  """

  # Why would you use getter and setter methods?
  # It allows us to validate and control user input for our objects

def modules():
  # import the math module and call the sin function
  import math 
  print (math.sin(10))

  # Create your own module with the function snake()
  import animal
  animal.snake()

class Fruit:
  def __init__(self, color, taste):
    self.color = color
    self.taste = taste

  def printDescription(self):
    print(self.color, self.taste)

  # Create a new class that inherits from the class Fruit
class Berry(Fruit):
  def printFact():
    print("Fun fact: pumpkins are a berry.")

  # Create a class that inherits from two super classes
class Multi(Fruit, Berry):
  pass

# Static Methods
  # Can a method inside a class be called without creating an object?
  # Yes you can, if you have a static method in a class, you can call the method without making an object
  
  # Why does not everybody like static methods?
  # They break the typical structure of OOP principles. Static methods can be called from anywhere, by anyone, and it will all share same value. Say you have some static "Open file method". If two processes use it and begin writing to files, the result will be a tangled garbage of output.

# Iterable
  # What is an iterable?
  # An iterable is a python object that can be used as a sequence. You can loop over an iteralbe, but you can't access individual elements directly

  # Which types of data can be used with an iterable?
  # An iterable is just a container, and could hold any type of data. For example lists, tupels, dictionaries, and sets are all iterable objects.

# Class Method
  # What is a classmethod?
  # A class method is a method that is shared among all objects. They can be called from instances of the class, as well as in the class itself.

  # How does a classmethod differ from a static method?
  # A static method knows nothing about the class or instance. A class method gets the class when the method is called - it knows about the classes atributes and methods.

# Multiple Inheritance
  # Do all programming langauges support multiple inheritance?
  # No. Multiple inheritance can greatly increase the complexity of the language, making it very difficult to create compilers and developing the language.

  # Why would you not use multiple inheritance?
  # If you have two classes that have the same method name, but different functionality. It might not be defined what method you actually inherit from

  # Is there a limit to the number of classes you can inherit from?
  # Not in python.
