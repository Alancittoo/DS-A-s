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



# An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

# Example: (Input --> Output)

# "Dermatoglyphics" --> true "aba" --> false "moOse" --> false (ignore letter case)

# isIsogram "Dermatoglyphics" = true
# isIsogram "moose" = false
# isIsogram "aba" = false



def is_isogram(string):
    string = string.lower()
    letts = set()

    for x in string:
        if x.isalpha():
            if x in letts:
                return False
            letts.add(x)

    return True


# Something is wrong with our Warrior class. All variables should initialize properly and the attack method is not working as expected.

# If properly set, it should correctly calculate the damage after an attack (if the attacker position is == to the block position of the defender: no damage; otherwise, the defender gets 10 damage if hit "high" or 5 damage if hit "low". If no block is set, the defender takes 5 extra damage.

# For some reason, the health value is not being properly set. The following shows an example of this code being used:

# ninja = Warrior('Hanzo Hattori')
# samurai = Warrior('Ryōma Sakamoto')

# samurai.block = 'l'
# ninja.attack(samurai, 'h')
# # samurai.health should be 90 now
# The warrios must be able to fight to the bitter end, and good luck to the most skilled!

# Notice that health can't be below 0: once hit to 0 health, a warrior attribute deceased becomes true; if hit again, the zombie attribute becomes true too!

Position = {'high': 'h', 'low': 'l'}  #don't change this!

class Warrior():
    def __init__(self, name):
        # each warrior should be created with a name and 100 health points
        self.name = name
        self.health = 100
        # default guard is "", that is unguarded
        self.block = ""
        self.deceased = False
        self.zombie = True

    def attack(self, enemy, position):
        # attacking high deals 10 damage, low 5
        # 0 damage if the enemy blocks in the same position
        damage = 0
        if enemy.block!=position:
            damage+=10 if position =='h' else 5
        if enemy.block=="": damage+=5

        enemy.set_health(enemy.health-damage)

    def set_health(self, new_health):
    # health cannot have negative values
        self.health = max(0, new_health)
    # if a warrior is set to 0 health he is dead
        if self.health == 0:
            if not self.deceased:
                self.deceased = True
            else:
                self.zombie = True
    # he would be a zombie only if he was already dead


# Since there are lots of katas requiring you to round numbers to 2 decimal places, you decided to extract the method to ease out the process.

# And you can't even get this right!

# Quick, fix the bug before everyone in CodeWars notices that you can't even round a number correctly!


from decimal import Decimal, ROUND_HALF_UP

def round_by_2_decimal_places(n):
    return n.quantize(Decimal('0.01'),ROUND_HALF_UP)






