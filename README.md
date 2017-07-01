# Python Advanced

*by Shantanu Kamath for IEEE NTU Student Branch*

***Disclaimer*** *-* *This document is only meant to serve as a reference for the attendees of the workshop. It does not cover all the concepts or implementation details discussed during the actual workshop.*
### To do
- [x] Make Notebook for Python Basics
- [x] Make Notebook for Python Advanced
- [ ] Add Generators
- [ ] Add Implementations for Algorithms
- [ ] Move Search and Sort Algorithms from the Advanced ReadMe to Algorithm Implementations
- [ ] Add Implementations for Data Structures
- [ ] Add Solutions to Project Euler
- [ ] Update ReadMe to define and table of contents for different workshops.
### Getting Started

- **Python Basics:** This document is meant to go deeper into concepts of programming in Python. It expects the attendees to have basic knowledge of the language that was explained in the introductory workshop - [Python Basics - IEEE NTU](https://github.com/SuyashLakhotia/IEEENTU-PythonBasics/blob/master/README.md).

- **Development Environment:** The workshop will be conducted using IDLE development environment on MacOS running the latest Python version 3.6.0 . It is recommended that the attendees use the same. Attendees are welcome to use an environment they are comfortable with. [Download Environment](https://www.python.org/downloads/)

## List Basics

In Python, it is possible to create a list of values. Each item in the list is called an *element* and can be accessed individually using a zero-based index. Hence avoiding the need to create multiple variables to store individual values.

```python
# list of numbers of type Integer
numbers = [1, 2, 3, 4, 5]
print("List :", numbers)
print("Second element :", numbers[1])    ## 2
print("Length of list :",len(numbers))   ## 5
print() # Empty line

# list of strings
colors = ['red', 'blue', 'green']
print("List :", colors)
print ("First color :", colors[0])      ## red
print ("Third color :", colors[2])      ## green
print ("Length of list :",len(colors))  ## 3
print() # Empty line

# list with multiple variable types
me = ['Shantanu Kamath', 'Computer Science', 20, 1000000]
print("List :", me)
print("Fourth element :", me[3])        ## 1000000
print("Length of list :", len(me))      ## 4
```

## List Methods

Besides simple accessing of values, lists have a large variety of methods that are used to performed different useful manipulations on them.  
Some of them are:  

- **list.append(element):** adds a single element to the end of the list. Common error: does not return the new list, just modifies the original.

```python
# list.append example
names = ['Hermione Granger', 'Ronald Weasley']
names.append('Harry Potter')
print(names)  ## ['Hermione Granger', 'Ronald Weasley', 'Harry Potter']
```

- **list.insert(index, element):** inserts the element at the given index, shifting elements to the right.

```python
# list.insert example
names = ['Ronald Weasley', 'Hermione Granger']
names.insert(1, 'Harry Potter')
print(names)  ## ['Ronald Weasley', 'Harry Potter', 'Hermione Granger']
```

- **list.extend(list2):** adds the elements in list2 to the end of the list. Using + or += on a list is similar to using extend().

```python
# list.extend example
MainChar = ['Ronald Weasley', 'Harry Potter', 'Hermione Granger']
SupChar = ['Neville Longbottom', 'Luna Lovegood']
MainChar.extend(SupChar)
print(MainChar)  ## ['Ronald Weasley', 'Harry Potter', 'Hermione Granger', 'Neville Longbottom', 'Luna Lovegood']
```

- **list.index(element):** searches for the given element from the start of the list and returns its index. Throws a ValueError if the element does not appear (use 'in' to check without a ValueError).

```python
# list.index example
names = ['Ronald Weasley', 'Harry Potter', 'Hermione Granger']
index = names.index('Harry Potter')  
print(index)  ## 1

# Throws a ValueError
index = names.index('Albus Dumbledore')
```

- **list.remove(element):** searches for the first instance of the given element and removes it (throws ValueError if not present)

```python
names = ['Ronald Weasley', 'Harry Potter', 'Hermione Granger']
index = names.remove('Harry Potter')  ## ['Ronald Weasley', 'Hermione Granger']
print(names)
```

- **list.pop(index):** removes and returns the element at the given index. Returns the rightmost element if index is omitted (roughly the opposite of append()).

```python
names = ['Ronald Weasley', 'Harry Potter', 'Hermione Granger']
index = names.pop(1)
print(names)  ## ['Ronald Weasley', 'Hermione Granger']
```

- **list.sort():** sorts the list in place (does not return it). (The sorted() function shown below is preferred.)

```python
alphabets = ['a', 'f','c', 'e','b', 'd']
alphabets.sort();
print (alphabets) ## ['a', 'b', 'c', 'd', 'e', 'f']
```

- **list.reverse():** reverses the list in place (does not return it).

```python
alphabets = ['a', 'b', 'c', 'd', 'e', 'f']
alphabets.reverse()
print(alphabets)  ## ['f', 'e', 'd', 'c', 'b', 'a']
```

## List Comprehensions
In Python, List comprehensions provide a concise way to create lists. Common applications are to make new lists where each element is the result of some operations applied to each member of another sequence, or to create a subsequence of those elements that satisfy a certain condition.

It can be used to construct lists in a very natural, easy way, like a mathematician is used to do.
This is how we can explain sets in maths:
- Squares = {x² : x in {0 ... 9}}
- Exponents = (1, 2, 4, 8, ..., 2¹²)
- EvenSquares = {x | x in S and x even}

Lets try to do this in Python using normal loops and list methods:

```python
# Using loops and list methods

squares = []
for x in range(10):
  squares.append(x**2)
print(squares)      ## [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

exponents = []
for i in range(13):
  exponents.append(2**i)
print(exponents)    ## [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]

evenSquares = []
for x in squares:
  if x % 2 == 0:
    evenSquares.append(x)
print(evenSquares)  ## [0, 4, 16, 36, 64]
```

These extend to more than one line. But by using list comprehensions you can bring it down to just one line.

```python
# Using list comprehensions

squares = [x**2 for x in range(10)]
exponents = [2**i for i in range(13)]
evenSquares = [x for x in squares if x % 2 == 0]
print(squares)      ## [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(exponents)    ## [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]
print(evenSquares)  ## [0, 4, 16, 36, 64]

```

## Searching
Searching is the process of finding a particular item in a collections of items. It is one of the most common problems that arise in computer programming. A search typically answers either True or False as to whether the item is present.

In Python, there is a very easy way to ask whether an item is in a list of items. We use the ***in*** operator.

```python
# Using in to check if number is present in the list.

>>> 15 in [3,5,2,4,1]
False
>>> 'Work' in 'Python Advanced Workshop'
True
```
Sometimes it can be important to get the position of the searched value. In that case, we can use ***index*** method for lists and the ***find*** method for strings.

```python
# Using index to get position of the number if present in list.
# In case of lists, its important to remember that the index function will throw an error if the value isn't present in the list.

values = [3,5,2,4,1]
if 5 in values:
  print("Value present at",values.index(5))  ## 1
else:
  print("Value not present in list")

# Using find to get the index of the first occurrence of the word in a sentence.

sentence = "This be a string"
index = sentence.find("is")
if index == -1:
  print("There is no 'is' here!")
else:
  print("Found 'is' in the sentence at position "+str(index))

# Using index to find words in a list of words
sentence = "This be a string"
words = sentence.split(' ')
if 'is' in words:
  print("Found 'is' in the list at position "+str(words.index('is')))
else:
  print("There is no 'is' here!")
```

#### Sequential Search Algorithm
When data items are stored in a collection such as a list, we say that they have a linear or sequential relationship. Each data item is stored in a position relative to the others.   
In Python lists, these relative positions are the index values of the individual items. Since these index values are ordered, it is possible for us to visit them in sequence.

```python
# Sequential search algorithm

def sequentialSearch(alist, item):
  pos = 0
  found = False
  while pos < len(alist) and not found:
    if alist[pos] == item:
      found = True;
    else:
      pos = pos + 1
  if pos == len(alist):
     return -1
  return pos

testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
print(sequentialSearch(testlist, 3))
print(sequentialSearch(testlist, 13))
```

#### Binary Search Algorithm *(Optional)*
***Binary search requires the list to be in a sorted order.***    
Instead of searching the list in sequence, a binary search will start by examining the middle item. If that item is the one we are searching for, we are done.   
If it is not the correct item, we can use the ordered nature of the list to eliminate half of the remaining items.   
If the item we are searching for is greater than the middle item, we know that the entire lower half of the list as well as the middle item can be eliminated from further consideration. The item, if it is in the list, must be in the upper half.   
We can then repeat the process with the upper half. Start at the middle item and compare it against what we are looking for. Again, we either find it or split the list in half, therefore eliminating another large part of our possible search space.

```python
# Binary search algorithm

def binarySearch(alist, item):
  first = 0
  last = len(alist)-1
  found = False

  while first<=last and not found:
      midpoint = (first + last)//2
      if alist[midpoint] == item:
          found = True
          return midpoint
      else:
          if item < alist[midpoint]:
              last = midpoint-1
          else:
              first = midpoint+1
  return -1

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(binarySearch(testlist, 3))
print(binarySearch(testlist, 13))
```


For more on searching algorithms (Hashing) you can refer to [InteractivePython Tutorials](http://interactivepython.org/runestone/static/pythonds/SortSearch/toctree.html)

## Sorting
Sorting is the process of placing elements from a collection in some kind of order.   
For example, a list of words could be sorted alphabetically or by length.    
A list of cities could be sorted by population, by area, or by zip code.


Python lists have a ***built-in sort()*** method that modifies the *list in-place* and a ***sorted() built-in*** function that builds a *new* sorted list from an iterable.

- ***list.sort():***  Modifies existing list and can be used only with lists.
- ***sorted(list):*** Creates a new list when called and can be used with other iterables.

##### Basic sorting functions
The most basic use of the sorted function can be seen below :  

```python
# Using sort() with a list.

values = [7, 4, 3, 6, 1, 2, 5]
print("Unsorted list :", values)     ## [7, 4, 3, 6, 1, 2, 5]
newValues = values.sort()
print("New list :", newValues)       ## None
print("Old list :", values)          ## [1, 2, 3, 4, 5, 6, 7]
print()
# Using sorted() with a list.

values = [7, 4, 3, 6, 1, 2, 5]
print("Unsorted list :", values)     ## [7, 4, 3, 6, 1, 2, 5]
newValues = sorted(values)
print("New list :", newValues)       ## [1, 2, 3, 4, 5, 6, 7]
print("Old list :", values)          ## [7, 4, 3, 6, 1, 2, 5]
```

##### Sorting using additional key
For more complex custom sorting, sorted() takes an optional "key=" specifying a "key" function that transforms each element before comparison.    
The key function takes in 1 value and returns 1 value, and the returned "proxy" value is used for the comparisons within the sort.
```python
# Using key in sorted

values = ['ccc', 'aaaa', 'd', 'bb']
print (sorted(values, key=len))            ## ['d', 'bb', 'ccc', 'aaaa']

# Remember case sensitivity :  All upper case characters come before lower case character in an ascending sequence.
sentence = "This is a test string from Andrew"
sorted(sentence.split(), key=str.lower)    ## ['a', 'Andrew', 'from', 'is', 'string', 'test', 'This']

# Using reverse for ascending and descending
strs = ['aa', 'BB', 'zz', 'CC']
print sorted(strs)                         ## ['BB', 'CC', 'aa', 'zz'] (case sensitive)
print sorted(strs, reverse=True)           ## ['zz', 'aa', 'CC', 'BB']

```

For more on sorting algorithms and its implementation you can refer to [InteractivePython Tutorials](http://interactivepython.org/runestone/static/pythonds/SortSearch/toctree.html)

## Basics on Class and OOP

This section is built around the fundamental of *Object Oriented Programming (OOP)*.
It aims strengthening basics but doesn't justify the broad topic itself. As OOP is a very important programming concept you should read further to better get a grip on python as well as go deep in understanding how it is useful and essential to programming.
Below are some essential resources :
- [Improve Your Python: Python Classes and Object Oriented Programming](https://jeffknupp.com/blog/2014/06/18/improve-your-python-python-classes-and-object-oriented-programming/)
- [Learn Python The Hard Way](https://learnpythonthehardway.org/book/ex40.html)
- [Python For Beginners](http://www.pythonforbeginners.com)
- [A Byte Of Python](https://python.swaroopch.com/oop.html)

### OOP
In all the code we wrote till now, we have designed our program around functions i.e. blocks of statements which manipulate data. This is called the procedure-oriented way of programming.

There is another way of organizing your program which is to combine data and functionality and wrap it inside something called an object. This is called the object oriented programming paradigm.   

Most of the time you can use procedural programming, but when writing large programs or have a problem that is better suited to this method, you can use object oriented programming techniques.

### Classes and Objects
Classes and objects are the two main aspects of object oriented programming. A ***class*** creates a new type where ***objects*** are ***instances*** of the class.   

Objects can store data using ordinary variables that belong to the object. Variables that belong to an object or class are referred to as ***fields*** or ***attributes***.

Objects can also have functionality by using functions that belong to a class. Such functions are called ***methods*** of the class.

The simplest class possible is shown in the following example :

```python
class Person:
    pass  # An empty block

p = Person()
print(p)

```
### Methods

Class methods have only one specific difference from ordinary functions - they must have an extra first name that has to be added to the beginning of the parameter list, but you do not give a value for this parameter when you call the method, Python will provide it. This particular variable refers to the object itself, and by convention, it is given the name self.

```python
class Person:
    def say_hi(self):
        print('Hello, how are you?')

p = Person()
p.say_hi()
```

#### The __init__
There are many method names which have special significance in Python classes. We will see the significance of the __init__ method now.   

The __init__ method is run as soon as an object of a class is instantiated. The method is useful to do any initialization you want to do with your object. Notice the double underscores both at the beginning and at the end of the name.

```python
class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('Hello, my name is', self.name)

p = Person('Swaroop')
p.say_hi()
```

#### Object variables
Now let us learn about the data part. The data part, i.e. fields, are nothing but ordinary variables that are bound to the namespaces of the classes and objects. This means that these names are valid within the context of these classes and objects only. That's why they are called name spaces.   

There are two types of fields - class variables and object variables which are classified depending on whether the class or the object owns the variables respectively.   

***Class variables*** are shared - they can be accessed by all instances of that class. There is only one copy of the class variable and when any one object makes a change to a class variable, that change will be seen by all the other instances.   

***Object variables*** are owned by each individual object/instance of the class. In this case, each object has its own copy of the field i.e. they are not shared and are not related in any way to the field by the same name in a different instance.

 An example will make this easy to understand.

```python
class Robot:
    ##   Represents a robot, with a name.

    # A class variable, counting the number of robots
    population = 0

    def __init__(self, name):
        ##   Initializes the data.
        self.name = name
        print("(Initializing {})".format(self.name))

        # When this person is created, the robot
        # adds to the population
        Robot.population += 1

    def die(self):
        ##   I am dying.
        print("{} is being destroyed!".format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print("{} was the last one.".format(self.name))
        else:
            print("There are still {:d} robots working.".format(
                Robot.population))

    def say_hi(self):
        ##   Greeting by the robot. Yeah, they can do that.
        print("Greetings, my masters call me {}.".format(self.name))

    @classmethod
    def how_many(cls):
        ##   Prints the current population.
        print("We have {:d} robots.".format(cls.population))


droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()

droid2 = Robot("C-3PO")
droid2.say_hi()
Robot.how_many()

print("\nRobots can do some work here.\n")

print("Robots have finished their work. So let's destroy them.")
droid1.die()
droid2.die()

Robot.how_many()
```

#### How It Works
This is a long example but helps demonstrate the nature of class and object variables. Here, population belongs to the Robot class and hence is a class variable. The name variable belongs to the object (it is assigned using self) and hence is an object variable.  

Thus, we refer to the population class variable as Robot.population and not as self.population. We refer to the object variable name using self.name notation in the methods of that object. Remember this simple difference between class and object variables. Also note that an object variable with the same name as a class variable will hide the class variable!   

Instead of Robot.population, we could have also used self.__class__.population because every object refers to its class via the self.__class__ attribute.   

The how_many is actually a method that belongs to the class and not to the object. This means we can define it as either a classmethod or a staticmethod depending on whether we need to know which class we are part of. Since we refer to a class variable, let's use classmethod.


We have marked the how_many method as a class method using a decorator.
Decorators can be imagined to be a shortcut to calling a wrapper function, so applying the @classmethod decorator is same as calling:
how_many = classmethod(how_many)

Observe that the __init__ method is used to initialize the Robot instance with a name. In this method, we increase the population count by 1 since we have one more robot being added. Also observe that the values of self.name is specific to each object which indicates the nature of object variables.
Remember, that you must refer to the variables and methods of the same object using the self only. This is called an attribute reference.

All class members are public. One exception: If you use data members with names using the double underscore prefix such as ***__privatevar*** , Python uses name-mangling to effectively make it a private variable.

Thus, the convention followed is that any variable that is to be used only within the class or object should begin with an underscore and all other names are public and can be used by other classes/objects. Remember that this is only a convention and is not enforced by Python (except for the double underscore prefix).


*There are more concepts in OOP such as Inheritance, Abstraction and Polymorphism, which would require a lot more time to cover. You may refer to reference material for explanation on these topics.*
## File I/O
File handling is super simplified in Python compared to other programming languages.
The first thing you’ll need to know is Python’s built-in ***open*** function to get a ***file object***.   
The ***open*** function opens a ***file***. When you use the ***open*** function, it returns something called a ***file object***. File objects contain ***methods*** and ***attributes*** that can be used to collect information about the file you opened. They can also be used to manipulate said file.

For example, the ***mode*** attribute of a file object tells you which mode a ***file*** was opened in. And the ***name*** attribute tells you the name of the file that the ***file object*** has opened.

#### File Types
In Python, a file is categorized as either ***text*** or ***binary***, and the difference between the two file types is important.

***Text files*** are structured as a sequence of lines, where each line includes a sequence of characters. This is what you know as code or syntax.

Each line is terminated with a special character, called the ***EOL*** or ***End of Line*** character. There are several types, but the most common is the ***comma*** {,} or ***newline*** character. It ends the current line and tells the interpreter a new one has begun.

A ***backslash*** character can also be used, and it tells the interpreter that the next character – following the slash – should be treated as a new line. This character is useful when you don’t want to start a new line in the text itself but in the code.

A ***binary file*** is any type of file that is not a text file. Because of their nature, binary files can only be processed by an application that know or understand the file’s structure. In other words, they must be applications that can ***read and interpret*** binary.

#### Open ( ) Function
The syntax to open a file object in Python is:

```python
file_object  = open("filename", "mode") ## where file_object is the variable to add the file object.
```
The second argument you see – mode – tells the interpreter and developer which way the file will be used.

#### Mode
Including a mode argument is optional because a default value of ***r*** will be assumed if it is omitted.

The modes are:

- ***r*** – Read mode which is used when the file is only being read
- ***w*** – Write mode which is used to edit and write new information to the file (any existing files with the same name will be erased when this mode is activated)
- ***a*** – Appending mode, which is used to add new data to the end of the file; that is new information is automatically amended to the end
- ***r+*** – Special read and write mode, which is used to handle both actions when working with a file

#### Create a text file
Using a simple text editor, let’s create a file. You can name it anything you like, and it’s better to use something you’ll identify with.
For the purpose of this workshop, however, we are going to call it "testfile.txt".
Just create the file and leave it blank.

To manipulate the file :
```python
file = open("testfile.txt","w")

file.write("Hello World")
file.write("This is our new text file")
file.write("and this is another line.")
file.write("Why? Because we can.")

file.close()
```

#### Reading a text file
Following methods allow reading a file :
- ***file.read():*** extract a string that contains all characters in the file.
```python
file = open("testfile.text", "r")
print file.read()
```
- ***file.read(numberOfCharacters):*** extract only a certain number of characters.  
```python
file = open("testfile.txt", "r")

print file.read(5)
```
- ***file.readline():*** read a file line by line – as opposed to pulling the content of the entire file at once.
```python
file = open("testfile.txt", "r")
print file.readline()
```
- ***file.readline(lineNumber):*** return a specific line
```python
file = open("testfile.txt", "r")
print file.readline(3):
```
- ***file.readlines():*** return every line in the file, properly separated in a list
```python
file = open("testfile.txt", "r")
print file.readlines():
```

#### Looping over file
When you want to read – or return – all the lines from a file in a more memory efficient, and fast manner, you can use the loop over method. The advantage to using this method is that the related code is both simple and easy to read.

```python
file = open("testfile.txt", "r")
for line in file:
print line
```

#### Using the File Write Method
This method is used to add information or content to an existing file. To start a new line after you write data to the file, you can add an ***EOL*** ("\n")) character.
```python
file = open("testfile.txt", "w")

file.write("This is a test")
file.write("To add more lines.")

file.close()
```
#### Closing a file
When you’re done working, you can use the fh.close() command to end things. What this does is close the file completely, terminating resources in use, in turn freeing them up for the system to deploy elsewhere.

It’s important to understand that when you use the fh.close() method, any further attempts to use the file object will fail.
```python
file.close()
```
## Importing Modules
So far we haven't explained what a Python module is. To put it in a nutshell: every file, which has the file extension .py and consists of proper Python code, can be seen or is a module.   
There is no special syntax required to make such a file a module. A module can contain arbitrary objects, for example files, classes or attributes.   
All those objects can be accessed after an import. There are different ways to import a modules.   

Import one module:
```python
>>> import math
>>> math.pi
3.141592653589793
>>> math.sin(math.pi/2)
1.0
>>> math.cos(math.pi/2)
6.123031769111886e-17
>>> math.cos(math.pi)
-1.0
```

Import more than one module in one import statement:
```python
import math, random
```
If only certain objects of a module are needed, we can import only those:
```python
from math import sin, pi
```
Instead of explicitly importing certain objects from a module, it's also possible to import everything in the namespace of the importing module:
```python
>>> from math import *
>>> sin(3.01) + tan(cos(2.1)) + e
2.2968833711382604
>>> e
2.718281828459045
```

## Scripting
This topic is a little more complex than you would have expected it to be.
Probably practice more python before you venture into this topic.
But just to get you to understand what this topic consists of and also appreciate the powerful nature of python,
Here are a few video clips to showing the result of various python scripts.  
[Articles showcasing python scripts](https://www.quora.com/What-are-the-best-Python-scripts-youve-ever-written)   
[Movie subtitle downloader](https://youtu.be/Q5YWEqgw9X8)   
[Python Script to download course content from Blackboard learn](https://github.com/NasaGeek/blackboard-export)   
