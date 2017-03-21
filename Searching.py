# Question : Given a list of unsorted integers, find and print all the
#            positions of numbers that are divisible by given number
#
# Answer   : 1. Modify sequential search to loop through each value in
#            the list
#            2. Check if each value is divisible by given number and
#            print its position.

















def sequentialSearch(alist, item):
    pos = 0
    while pos < len(alist):
        if alist[pos] % item == 0:
            print(pos)
        pos = pos + 1

testlist = [1, 2, 32, 8, 17, 19, 42, 13]
print(sequentialSearch(testlist, 3))
print(sequentialSearch(testlist, 2))

# Question : Given a list of unsorted integers, find a particular number.
#            If number is present display its position else add it to the
#            list and print an alert.
#
# Answer   : 1. Modify sequential search.






















def sequentialSearch(alist, item):
  pos = 0
  found = False
  while pos < len(alist) and not found:
    if alist[pos] == item:
      found = True;
    else:
      pos = pos + 1
  if pos == len(alist):
     alist.append(item)
     return alist
  return pos

testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
print(sequentialSearch(testlist, 3))
print(sequentialSearch(testlist, 13))
print(testlist)
