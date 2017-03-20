# Python Advanced

*by Shantanu Kamath for IEEE NTU Student Branch*

***Disclaimer*** *-* *This document is only meant to serve as a reference for the attendees of the workshop. It does not cover all the concepts or implementation details discussed during the actual workshop.*

### Getting Started

- **Python Basics:** This document is meant to go deeper into concepts of programming in Python. It expects the attendees to have basic knowledge of the language that was explained in the introductory workshop - [Python Basics - IEEE NTU](https://github.com/SuyashLakhotia/IEEENTU-PythonBasics/blob/master/README.md).

- **Development Environment:** The workshop will be conducted using IDLE development environment on MacOS running the latest Python version 3.6.0 . It is recommended that the attendees use the same. Attendees are welcome to use an environment they are comfortable with. [Download Environment](https://www.python.org/downloads/)

## List Basics

In Python, it is possible to create a list of values. Each item in the list is called an *element* and can be accessed individually using a zero-based index. Hence avoiding the need to create multiple variables to store individual values.

```python
# list of numbers of type Integer
numbers = [1, 2, 3, 4, 5]
print(numbers)       ## [1, 2, 3, 4, 5]
print(numbers[1])    ## 2
print(len(numbers))  ## 5

# list of strings
colors = ['red', 'blue', 'green']
print colors[0]    ## red
print colors[2]    ## green
print len(colors)  ## 3

# list with multiple variable types
me = ['Shantanu Kamath', 'Computer Science', 21, 1000000]
print(me[3])    ## 1000000
print(len(me))  ## 4
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
# list.append example
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
  print(values.index(5))  ## 1
else:
  print("Value not present in list")

# Using find to get the index of the first occurrence of the word in a sentence.

sentence = "This be a string"
index = sentence.find("is")
if index == -1:
  print ("There is no 'is' here!")
else:
  print ("Found 'is' in the sentence at position "+str(index))

# Using index to find words in a list of words
sentence = "This be a string"
words = sentence.split(' ')
if 'is' in words:
  print ("Found 'is' in the list at position "+str(words.index('is'))) ## 1
else:
  print ("There is no 'is' here!")
```

### Sequential Search Algorithm *(OPTIONAL)*

## Sorting
