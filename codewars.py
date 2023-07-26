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


# You live in the city of Cartesia where all roads are laid out in a perfect grid. You arrived ten minutes too early to an appointment, so you decided to take the opportunity to go for a short walk.
# The city provides its citizens with a Walk Generating App on their phones -- everytime you press the button it sends you an array of one-letter strings representing directions to walk (eg. ['n', 's', 'w', 'e']).
# You always walk only a single block for each letter (direction) and you know it takes you one minute to traverse one city block, so create a function that will return true if the walk the app gives you will take you exactly ten minutes,
# (you don't want to be early or late!) and will, of course, return you to your starting point. Return false otherwise.

# Note: you will always receive a valid array containing a random assortment of direction letters ('n', 's', 'e', or 'w' only). It will never give you an empty array (that's not a walk, that's standing still!).

# import codewars_test as test

# @test.describe('Walk Validator - fixed tests')
# def sample_tests():
#     @test.it ("should return true for a valid walk")
#     def _():
#         test.assert_equals(is_valid_walk(['n','s','n','s','n','s','n','s','n','s']), True, 'should return True');
#     @test.it ("should return false if walk is too long")
#     def _():
#         test.assert_equals(is_valid_walk(['w','e','w','e','w','e','w','e','w','e','w','e']), False, 'should return False');
#     @test.it ("should return false if walk is too short")
#     def _():
#         test.assert_equals(is_valid_walk(['w']), False, 'should return False');
#     @test.it ("should return false if walk does not bring you back to start")
#     def _():
#         test.assert_equals(is_valid_walk(['n','n','n','s','n','s','n','s','n','s']), False, 'should return False');


def is_valid_walk(walk):
    # set coords
    coords = {'n': 0, 's': 0, 'e': 0, 'w': 0}

    #to short or long
    if len(walk) != 10:
        return False

    # update coords
    for x in walk:
        coords[x] += 1

    return coords['n'] == coords['s'] and coords['e'] == coords['w']


# The marketing team is spending way too much time typing in hashtags.
# Let's help them with our own Hashtag Generator!

# Here's the deal:

# It must start with a hashtag (#).
# All words must have their first letter capitalized.
# If the final result is longer than 140 chars it must return false.
# If the input or the result is an empty string it must return false.
# Examples
# " Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
# "    Hello     World   "                  =>  "#HelloWorld"
# ""                                        =>  false

def generate_hashtag(s):
    if not s:
        return False

    words = s.split()
    hashtag = '#'

    for word in words:
        capitalized_word = word.capitalize()
        hashtag += capitalized_word

    if len(hashtag) > 140:
        return False

    return hashtag


# Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is non-negative.

# Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case



def count_bits(n):

    bin_num = bin(n)[2:]
    # removes the prefix issue

    ones = bin_num.count('1') #count 1s
    return ones
