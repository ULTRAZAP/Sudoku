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

from tabulate import tabulate as ta
import random as r

# we take random inputs from the range of 1-9 and not repeat the no. while keeping the space between them

# we will mark the space as 0

# we will randomize where the zero will go to

# l = []

# while len(l) <= 4:  # we will fill only 5 out of the 9 spaces in the line
#     a = r.randint(1, 9)  # both the no. are included
#     if a not in l:
#         l.append(a)

# while len(l) <= 8:  # to fill the remaining spaces with zero
#     a = r.randint(0, 9)  # both the no. are included
#     if len(l) > a:
#         if l[a] != 0:
#             l.insert(a, 0)

# print(l)

# TODO: You have to find out a way to make the randomizing thing consistent for both the zero and inputting the no (Solved It using while loop)
# The no. are changing everytime and thats good but same no. of no. are needed for consistency and for the length of the list to be 10
# TODO: solve the index error (Solved)

# TODO: Add more lines like in a actual sudoku game and to check that no no. is being repeated

# Okay, I have realized the existence of 2-Dimensional Lists
# and this is a test

# l = [1, 2]
# a = [0]
# a.append(l)
# l.append(4)
# a[0] = 1
# print(a)

# We can use the above code for more efficient and faster program

# TODO: Use the 2D List Logic to create 9 lists in side the list where each list is one line on a sudoku

# ! Input of the no. from the user should be done after printing of the sudoku is done

# * sudo = [[0,0,0,0,0,0,0,0,0],
# * [0,0,0,0,0,0,0,0,0],
# * [0,0,0,0,0,0,0,0,0],
# * [0,0,0,0,0,0,0,0,0],
# * [0,0,0,0,0,0,0,0,0],
# * [0,0,0,0,0,0,0,0,0],
# * [0,0,0,0,0,0,0,0,0],
# * [0,0,0,0,0,0,0,0,0],
# * [0,0,0,0,0,0,0,0,0]]

# For better visualization I have made the above code
# A better way would be to use for loop like this

# * this is a much better way and represents the same code as above
sudo = [[] for j in range(9)]

# for i in sudo:
#     print(i)
# TODO for tomorrow: randomize the no. inside them(Done)

# lets add the random algorithm
for i in range(9):
    while len(sudo[i]) <= 4:  # This will add 5 no. in the
        a = r.randint(1, 9)
        if a not in sudo[i]:
            sudo[i].append(a)

    while len(sudo[i]) <= 8:  # this will add 4 0's in the left over space
        a = r.randint(1, 9)
        if len(sudo[i]) > a:
            if sudo[i][a] != 0:
                sudo[i].insert(a, 0)

# TODO Make the above code work as it is not printing anything just solve that problem (Solved)

# * for printing them without brackets we can use this

# for i in range(len(sudo)):
#     for j in range(len(sudo[i])):
#         print(sudo[i][j], end=' ')
#     print()

# * Or what we can use it tabulate module for better looking box

#print(ta(sudo, tablefmt="grid"))

# TODO Remove repeating no. in one line for now

# Let's take each box and line in a list and check if there are no no. repeating

# TODO to make the above function better also make the writing of the code better (Done)

for i in range(9):
    l1 = sudo[i]  # for example
    for j in range(len(l1)):
        if l1[j] != 0:
            if l1.count(l1[j]) > 1:
                l1[j] = 0
    sudo[i] = l1

# * Let's work on the no. not repeating in one vertical line

# l1 = []
# i = 0
# for k in range(9):
#     l1.append(sudo[i][k])
#     for j in range(len(l1)):
#         if l1[j] != 0:
#             if l1.count(l1[j]) > 1:
#                 l1[j] = 0
#     sudo[i][k] = l1[i]
#     i += 1

# print(ta(sudo, tablefmt="grid"))

# * Above works only for one line

# TODO Make the above code work for all the lines

# Okay, It's too hard get each no. in the first index and change them so let's create another list which will contain all the elements in the vertical line

# And let's shorten the for loop code

# vl = []
# for j in range(9):
#     for i in range(9):
#         vl.append(sudo[i][j])

#     # TODO Work on the above code tomorrow (Done)

#     for i in range(len(vl)):
#         if vl.count(vl[i]) > 1:
#             vl[i] = 0

#     for i in range(9):
#         sudo[i][j] = vl[i]

print(ta(sudo, tablefmt="grid"))


# * The above code works properly and now to do this for all the vertical lines I have to implement this

# TODO Implement the above algo to all vertical lines(Done)

# ! The above code is not perfect so fix that
