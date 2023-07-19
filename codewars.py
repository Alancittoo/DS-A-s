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
