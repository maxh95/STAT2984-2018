import numpy as np


# Question 1: (2 points)
# count the number of elements in a list
countries = ['Cananda', 'United States', 'Spain', 'Germany', 'Brazil', 'China']
len(countries)
# there are 6 elements in the country list

# Question 2: (2 points)
# Compute the sum of a list of numbers
number = [3, 4, 5, 2, 3, 8, 7, 6, 4, 5, 1, 2, 3]
print sum(number)
#53

# Question 3: (2 points)
# given a number 'num', print if
# the number is odd or even
num = 4
if num % 2 == 0:
    print 'even'
else:
    print 'odd'
# even

# Question 4: (3 points)
# compute the mean of a list of numbers
#import numpy as np, I installed the numpy package so that I could use some new functions
np.mean(number)
#mean of numbers[] = 4.0769230769230766


# Question 5: (3 points)
# compute the standard deviation of a list of numbers
np.std(number)
#stdev of numbers[] = 1.9791815892720934

# Question 6: (3 points)
# create a list containing all elements
# from a list of numbers less than 'n'
# print the list
# n = 4  , n=4 is hashtagged out because earlier I created n to be something different and in pycharm it was easier to
# click on the variable and change its value to 4

list_less_four = [n for n in number if n < 4]
print list_less_four
# [3, 2, 3, 1, 2, 3]

# Question 7: (5 points)
# determine the median of a list of numbers
# hint: what do you do if there are an even
# number of elements in the list?
np.median(number)
# the median of numbers is 4.0


# Question 8: (5 points)
# create a dictionary 'counts' where the keys
# are the elements of a list and the values are
# the frequency of each element in the list

colors = ['red','blue','green','black','red','pink','blue','green','red','pink']
counts = {'RED':[3],'BLUE':[2],'GREEN':[2],'BLACK':[1], 'PINK':[2]}

# Question 9: (5 points)
# create a stem and leaf plot of a list of number
# hint: you can reuse some of the code from the previous question
number.sort()
stem_leaf = {'Leaf': number, 'Stem':0}
print stem_leaf
# {'Leaf': [1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 6, 7, 8], 'Stem': 0}

# Question 10: (10 points)
# create a list containing the first 'N'
# elements of the Fibinachi sequence.


def f(N):
    if N == 0:
        return [0]
    elif N == 1:
        return [0, 1]
    else:
        fib = f(N-1)
        fib.append(fib[-1] + fib[-2])  #the list.append method adds a single element to the end of a list, in this case
                                        # it is adding the -1 + -2 index of the n-1th iteration of the fibonacci
                                        #sequence, for n=10 the -1 index is34 and the -2 index is 21, 34+21=55 for f(10)
        return fib

first_ten_fib_num = f(10)
print first_ten_fib_num
# The first n=10 numbers of the Fibonacci sequence [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]