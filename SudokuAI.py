# SudokuAI

# As I am a Ametuer, I will first learn how to input no. in just one line of a sudoku table

# We do this by taking a sample list which will contain the no. from 1 to 9

# The no. will be randomized in the list and we have to input the missing no. in the places it should be / we want it to be

# I am using numpy to reduce the no. of lines and steps needed

# import numpy as np

# # here we have to find the missing no. and add it here to let's say at the index of 5
# l = [9, 7, 8, 6, 4, 3, 2, 1]

# a = list(range(1, 10))

# if np.mean(l) != 45:  # i am using mean as the mean of 1-9 is 45 and easier to write
#     l.sort()

#     for i in range(len(l)):
#         if l[i] != a[i]:
#             l.insert(5, a[i])
#             break

# print(l)
# # to change the commit message

# Now to make it better

# lets randomize the no. in a line of a Sudoku while keeping a place in between
# we intend to increase the spaces hence the difficulty

import random as r

# we take random inputs from the range of 1-9 and not repeat the no. while keeping the space between them

# we will mark the space as 0

# we will randomize where the zero will go to

l = []

for i in range(5):  # we will fill only 5 out of the 9 spaces in the line
    a = r.randint(1, 10)
    if a not in l:
        l.append(a)
print(l)
for i in range(11):
    a = r.randint(0, 11)
    if len(l) > a:
        if l[a] != 0:  # solve the index error occuring here
            l.insert(a, 0)

print(l)

# TODO: You have to find out a way to make the randomizing thing consistent for both the zero and inputting the no
# The no. are changing everytime and thats good but same no. of no. are needed for consistency and for the length of the list to be 10
# TODO solve the index error
