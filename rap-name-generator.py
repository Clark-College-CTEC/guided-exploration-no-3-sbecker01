# Guided Exploration No. 3
# Stewart Becker

import random  # imports that random library

possible_names = []  # creates an empty list

outputFile = open('rap-names-output.txt', 'w')  # creates a new file

# sets open('rap-names.txt', 'r') as the variable dataFile(?)
with open('rap-names.txt', 'r') as dataFile:
    for name in dataFile:  # per line in dataFile
        # appends to the empty list, strips spaces from the right side
        possible_names.append(name.rstrip())

# asks for a whole number input, sets as variable count
count = int(input('How many rap names would you like to create? '))
# asks for a whole number input, sets as variable parts
parts = int(input('How many parts should the name contain? '))


for i in range(count):  # repeats indented code for number of times requested by user
    name_parts = []  # set empty list

    for j in range(parts):  # nested loop, repeats indented code for the amount equal to parts
        # appends a possible rap name randomly via randit function (randit is limited from 0-end of the list)
        name_parts.append(
            possible_names[random.randint(0, len(possible_names)-1)])
        # writes to file, joins the randomly generated rap name with a space
    outputFile.write(f"{' '.join(name_parts)}\n")
    print(f"{' '.join(name_parts)}")  # prints
outputFile.close()  # closes file
