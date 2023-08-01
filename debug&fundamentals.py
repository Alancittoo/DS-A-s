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
