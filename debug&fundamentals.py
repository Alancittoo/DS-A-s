# This code does not execute properly. Try to figure out why.
# def multiply(a, b):
#     a * b

# ANSWER
def multiply(a, b):
    return a * b



# Return the number (count) of vowels in the given string.

# We will consider a, e, i, o, u as vowels for this Kata (but not y).

# The input string will only consist of lower case letters and/or spaces.

def get_count(sentence):
    vowels = 'aieou'
    start = 0

    for let in sentence:
        if let in vowels:
            start += 1
    return start




# You might know some pretty large perfect squares. But what about the NEXT one?

# Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter. Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.

# If the parameter is itself not a perfect square then -1 should be returned. You may assume the parameter is non-negative.

# Examples:(Input --> Output)

# 121 --> 144
# 625 --> 676
# 114 --> -1 since 114 is not a perfect square


import math
def find_next_square(sq):
    if math.sqrt(sq).is_integer():
        num = math.sqrt(sq)
        num += 1
        return num * num
    else:
        return -1


# Complete the square sum function so that it squares each number passed into it and then sums the results together.

# For example, for [1, 2, 2] it should return 9


def square_sum(numbers):
    sum = 0

    for num in numbers:
        sum += num * num
    return sum


# Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.


def bool_to_word(boolean):
    if boolean == True:
        return "Yes"
    else:
        return "No"



# Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the "instructions" for the development and functioning of living organisms.

# If you want to know more: http://en.wikipedia.org/wiki/DNA

# In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". Your function receives one side of the DNA (string, except for Haskell); you need to return the other complementary side. DNA strand is never empty or there is no DNA at all (again, except for Haskell).

# More similar exercise are found here: http://rosalind.info/problems/list-view/ (source)

# Example: (input --> output)

# "ATTGC" --> "TAACG"
# "GTAT" --> "CATA"


def DNA_strand(dna):
    dna_pal = {'A': 'T', 'T': 'A', 'G' : 'C', 'C' : 'G'}
    res = [dna_pal[x] for x in dna]
    return ''.join(res)


# Code as fast as you can! You need to double the integer and return it.



def double_integer(i):
    return i * 2


# Timmy & Sarah think they are in love, but around where they live, they will only know once they pick a flower each. If one of the flowers has an even number of petals and the other has an odd number of petals it means they are in love.

# Write a function that will take the number of petals of each flower and return true if they are in love and false if they aren't.

# import codewars_test as test
# from solution import lovefunc

# @test.describe("Fixed Tests")
# def fixed_tests():
#     @test.it('Basic Test Cases')
#     def basic_test_cases():
#         test.assert_equals(lovefunc(1,4), True)
#         test.assert_equals(lovefunc(2,2), False)
#         test.assert_equals(lovefunc(0,1), True)
#         test.assert_equals(lovefunc(0,0), False)

def lovefunc( flower1, flower2 ):
    if flower1 % 2 == 0 and flower2 % 2 != 0 :
            return True
    if flower1 % 2 != 0 and flower2 % 2 == 0 :
            return True
    else:
        return False


#Write a function that takes an array of numbers and returns the sum of the numbers. The numbers can be negative or non-integer. If the array does not contain any numbers then you should return 0.

#Examples
#Input: [1, 5.2, 4, 0, -1]
#Output: 9.2

#Input: []
#utput: 0

#Input: [-2.398]
#Output: -2.398

#Assumptions
#You can assume that you are only given numbers.
#You cannot assume the size of the array.
#You can assume that you do get an array and if the array is empty, return 0.
#What We're Testing
#We're testing basic loops and math operations. This is for beginners who are just learning loops and math operations.
#Advanced users may find this extremely easy and can easily write this in one line.

def sum_array(a):
    total = 0
    for num in a:
        total += num
    return total
