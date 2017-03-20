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
me = ["Shantanu Kamath", "Computer Science", 21, 1000000]
print(me[3])    ## 1000000
print(len(me))  ## 4
```

## List Methods

Besides simple accessing of values, lists have a large variety of methods that are used to performed different useful manipulations on them.  
Some of them are:  
- **list.append(element):** adds a single element to the end of the list. Common error: does not return the new list, just modifies the original.
- **list.insert(index, element):** inserts the element at the given index, shifting elements to the right.
list.extend(list2) adds the elements in list2 to the end of the list. Using + or += on a list is similar to using extend().
- **list.index(element):** searches for the given element from the start of the list and returns its index. Throws a ValueError if the element does not appear (use "in" to check without a ValueError).
- **list.remove(element):** searches for the first instance of the given element and removes it (throws ValueError if not present)
- **list.sort():** sorts the list in place (does not return it). (The sorted() function shown below is preferred.)
- **list.reverse():** reverses the list in place (does not return it)
- **list.pop(index):** removes and returns the element at the given index. Returns the rightmost element if index is omitted (roughly the opposite of append()).

## List Comprehensions
In Python, List comprehensions provide a concise way to create lists.  
Common applications are to make new lists where each element is the result of some operations applied to each member of another sequence or iterable, or to create a subsequence of those elements that satisfy a certain condition.
