# Two Sum problem // EAsY kinda

# Write a function that takes an array of numbers (integers for the tests) and a target number. It should find two different items in the array that, when added together, give the target value. The indices of these items should then be returned in a tuple / list (depending on your language) like so: (index1, index2).

# For the purposes of this kata, some tests may have multiple answers; any valid solutions will be accepted.

# The input will always be valid (numbers will be an array of length 2 or greater, and all of the items will be numbers; target will always be the sum of two different items from that array).

# Based on: http://oj.leetcode.com/problems/two-sum/
numbers = [ 11, 2,  7, 15]
target = 9

def two_sum(numbers, target):
    #     keep track of numbers we go through
    nums_left = {}

    for i in range(len(numbers)):
        num = numbers[i]
#         number in array - target number
        left = target - num
#         if left is within the numbs left, return it
        if left in nums_left:
            return [nums_left[left], i]

        nums_left[num] = i

test = two_sum(numbers, target)


print(test) # [ 1 , 2 ]







# String ends with ? problem            /// EASY

# Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

# Examples:

# solution('abc', 'bc') # returns true
# solution('abc', 'd') # returns false


def solution(text, ending):
    # your code here...
    return text.endswith(ending)




#  // List filtering Problem ,         EASY but had difficulty remembering different python methods to get it going

# In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.

# Example
# filter_list([1,2,'a','b']) == [1,2]
# filter_list([1,'a','b',0,15]) == [1,0,15]
# filter_list([1,2,'aasf','1','123',123]) == [1,2,123]


def filter_list(l):
    #makes sure test is a integer, filtering out the other components in the array
    return [test for test in l if type(test) == int]



# A square of squares Problem, Medium forgot for the longest to import math and had trouble remembering it and just tried doing it a longer way until I figured out I had to import math

# You like building blocks. You especially like building blocks that are squares. And what you even like more, is to arrange them into a square of square building blocks!
# However, sometimes, you can't arrange them into a square. Instead, you end up with an ordinary rectangle! Those blasted things! If you just had a way to know, whether you're currently working in vain… Wait! That's it! You just have to check if your number of building blocks is a perfect square.

# Task
# Given an integral number, determine if it's a square number:
# In mathematics, a square number or perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself.
# The tests will always use some integral number, so don't worry about that in dynamic typed languages.

# Examples
# -1  =>  false
#  0  =>  true
#  3  =>  false
#  4  =>  true
# 25  =>  true
# 26  =>  false


import math

# def is_square(n):
#     num = math.sqrt(n)
#     if type(num) is float:
#         return False;
#     else:
#         return True


def is_square(n):
    if n < 0:
        return False;
    num = math.sqrt(n)
    return num.is_integer()
