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
