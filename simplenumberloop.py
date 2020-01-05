# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 19:42:12 2020

@author: Mustapha
"""

# List of integer numbers
numbers = [1, 2, 4, 6, 11, 20,25,30,40,]

# variable to store the square of each num temporary
sq = 0

# iterating over the given list
for val in numbers:
    # calculating square of each number
    sq = val * val
    # displaying the squares
    print(sq)