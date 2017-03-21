# Question : list and print all the vowels in a given word.
#
# Answer   : 1. Create a loop to run through each letter of the word
#            2. Check if each letter is a vowel or not. If it is add it to
#            the list.





















word = 'MATHEMATICS'
vowels = ['A','E','I','O','U']
vowelsInWord = [x for x in word if x in vowels]
print(vowelsInWord)  ## ['A', 'E', 'A', 'I']

# Question : Calculate the prime numbers between 1 and 100 using the sieve
#            of Eratosthenes:
#
# Answer   : 1. Create a list of all multiples of 2....8 that are less
#            than 100.
#            2. Create a list of all values that are in between 2....100
#            and not in the list above.


















noprimes = [j for i in range(2, 8) for j in range(i*2, 100, i)]
primes = [x for x in range(2, 100) if x not in noprimes]
print (primes)  ## [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
