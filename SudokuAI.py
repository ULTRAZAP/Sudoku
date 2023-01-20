# SudokuAI

# As I am a Ametuer, I will first learn how to input no. in just one line of a sudoku table

# We do this by taking a sample list which will contain the no. from 1 to 9

# The no. will be randomized in the list and we have to input the missing no. in the places it should be / we want it to be

# I am using numpy to reduce the no. of lines and steps needed

import numpy as np

# here we have to find the missing no. and add it here to let's say at the index of 5
l = [9, 7, 8, 6, 4, 3, 2, 1]

a = list(range(1, 10))

if np.mean(l) != 45:  # i am using mean as the mean of 1-9 is 45 and easier to write
    l.sort()

    for i in range(len(l)):
        if l[i] != a[i]:
            l.insert(5, a[i])
            break

print(l)
