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


# You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.

# Implement the function which takes an array containing the names of people that like an item. It must return the display text as shown in the examples:

# []                                -->  "no one likes this"
# ["Peter"]                         -->  "Peter likes this"
# ["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
# ["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
# ["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"

def likes(names):
    res = len(names)

    if res == 0:
        return "no one likes this"
    elif res == 1:
        return f"{names[0]} likes this"
    elif res == 2:
        return f"{names[0]} and {names[1]} like this"
    elif res == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        return f"{names[0]}, {names[1]} and {res - 2} others like this"




#Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

#Examples:

#* 'abc' =>  ['ab', 'c_']
#* 'abcdef' => ['ab', 'cd', 'ef']
def solution(s):
    res = [s[i:i+2] for i in range(0, len(s), 2)]
    if len(res) > 0 and len(res[-1]) == 1:
        res[-1] += '_'
    return res


#This time we want to write calculations using functions and get the results. Let's have a look at some examples:

#seven(times(five())) # must return 35
#four(plus(nine())) # must return 13
#eight(minus(three())) # must return 5
#six(divided_by(two())) # must return 3
#Requirements:

#There must be a function for each number from 0 ("zero") to 9 ("nine")
#There must be a function for each of the following mathematical operations: plus, minus, times, divided_by
#Each calculation consist of exactly one operation and two numbers
#The most outer function represents the left operand, the most inner function represents the right operand
#Division should be integer division. For example, this should return 2, not 2.666666...:
#eight(divided_by(three()))

def zero(operation=None):
    return 0 if operation is None else operation(0)

def one(operation=None):
    return 1 if operation is None else operation(1)

def two(operation=None):
    return 2 if operation is None else operation(2)

def three(operation=None):
    return 3 if operation is None else operation(3)

def four(operation=None):
    return 4 if operation is None else operation(4)

def five(operation=None):
    return 5 if operation is None else operation(5)

def six(operation=None):
    return 6 if operation is None else operation(6)

def seven(operation=None):
    return 7 if operation is None else operation(7)

def eight(operation=None):
    return 8 if operation is None else operation(8)

def nine(operation=None):
    return 9 if operation is None else operation(9)

def plus(num):
    return lambda x: x + num

def minus(num):
    return lambda x: x - num

def times(num):
    return lambda x: x * num

def divided_by(num):
    return lambda x: x // num

#Write a function named first_non_repeating_letter that takes a string input, and returns the first character that is not repeated anywhere in the string.

#For example, if given the input 'stress', the function should return 't', since the letter t only occurs once in the string, and occurs first in the string.

#As an added challenge, upper- and lowercase letters are considered the same character, but the function should return the correct case for the initial letter. For example, the input 'sTreSS' should return 'T'.

#If a string contains all repeating characters, it should return an empty string ("") or None -- see sample tests.

def first_non_repeating_letter(s):
    lower = s.lower()
    res = {}

    for letter in lower:
        res[letter] = res.get(letter, 0) + 1

    for letter in s:
        if res[lower[s.index(letter)]] == 1:
            return letter

    return ""



# Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

# * url = "http://github.com/carbonfive/raygun" -> domain name = "github"
# * url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
# * url = "https://www.cnet.com"                -> domain name = cnet"

def domain_name(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]



# Complete the solution so that it reverses the string passed into it.

# 'world'  =>  'dlrow'
# 'word'   =>  'drow'


def solution(string):
    return string[ :: -1]

# Note: This kata is inspired by Convert a Number to a String!. Try that one too.

# Description
# We need a function that can transform a string into a number. What ways of achieving this do you know?

# Note: Don't worry, all inputs will be strings, and every string is a perfectly valid representation of an integral number.

# Examples
# "1234" --> 1234
# "605"  --> 605
# "1405" --> 1405
# "-7" --> -7


def string_to_number(s):
    return int(s)

# Make a function that will return a greeting statement that uses an input; your program should return, "Hello, <name> how are you doing today?".

# [Make sure you type the exact thing I wrote or the program may not execute properly]

def greet(name):
    return f"Hello, {name} how are you doing today?"


# You are given a node that is the beginning of a linked list. This list contains a dangling piece and a loop. Your objective is to determine the length of the loop.

# For example in the following picture the size of the dangling piece is 3 and the loop size is 12:

def loop_size(node):
    x = node
    xn = node

    while xn is not None and xn.next is not None:
        x = x.next
        xn = xn.next.next

        if x == xn:
            # Count the length of the loop
            length = 1
            x = x.next
            while x != xn:
                x = x.next
                length += 1
            return length

    return 0



# In this kata, your task is to create all permutations of a non-empty input string and remove duplicates, if present.

# Create as many "shufflings" as you can!

# Examples:

# With input 'a':
# Your function should return: ['a']

# With input 'ab':
# Your function should return ['ab', 'ba']

# With input 'abc':
# Your function should return ['abc','acb','bac','bca','cab','cba']

# With input 'aabb':
# Your function should return ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
# Note: The order of the permutations doesn't matter.

# Good luck!


def permutations(s):
    def test(curr, remain):
        if not remain:
            solo.add(curr)
        else:
            for i in range(len(remain)):
                new_curr = curr + remain[i]
                new_remain = remain[:i] + remain[i + 1:]
                test(new_curr, new_remain)

    solo = set()
    test('', s)
    return list(solo)


# Given an array of integers your solution should find the smallest integer.

# For example:

# Given [34, 15, 88, 2] your solution will return 2
# Given [34, -345, -1, 100] your solution will return -345
# You can assume, for the purpose of this kata, that the supplied array will not be empty.


def find_smallest_int(arr):
    #needs to be first
    small = arr[0]
    #anything after first
    for i in arr[1:]:
        if i < small:
            small = i
    return small

# def findSmallestInt(arr):
#     return min(arr)



# Grade book
# Complete the function so that it finds the average of the three scores passed to it and returns the letter value associated with that grade.

# Numerical Score	Letter Grade
# 90 <= score <= 100	'A'
# 80 <= score < 90	'B'
# 70 <= score < 80	'C'
# 60 <= score < 70	'D'
# 0 <= score < 60	'F'
# Tested values are all between 0 and 100. Theres is no need to check for negative values or values greater than 100.


def get_grade(s1, s2, s3):
    avg = (s1 + s2 + s3) / 3

    if 90 <= avg <= 100:
        return 'A'
    elif 80 <= avg < 90:
        return 'B'
    elif 70 <= avg < 80:
        return 'C'
    elif 60 <= avg < 70:
        return 'D'
    else:
        return 'F'
