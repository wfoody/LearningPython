#count = 1
"""
while (count < 18):
    print("*"), count + 2
    count = count + 2
"""
# For Loop (definite) vs While Loop (indefinite)
# Start with one star on first line, then add another two stars for each new line (9)

# Add the first 10 numbers starting from 0
"""
sum = 0
for i in range(10):
    sum += i
print(sum)
"""
star = "*"
# range(9) -> [0, 1, 2, 3, 4, 5, 6, 7, 8]
# range(0, 9, 1)
for line in range(9):
    # Print spaces
    # get the number of spaces we want to print
    # Cumulative sum: for loop to add something each time to some value, then do something with the sum
    output = ""
    # add spaces to output
    # range(start [inclusive], end [exclusive], step)
    for space in range(8 - line):
        output += " "

    # add stars to output
    output += star
    star += "**"

    # print output
    print(output)

# Lines | Spaces | Equation
# 0     | 8      | spaces = 8 - lines
# 1     | 7      |
# 2     | 6      |
# 3     | 5      |
# 4     | 4
# 5     | 3
# 6     | 2
# 7     | 1
# 8     | 0
# Lines | Stars
# 0     | 1
# 1     | 3
# 2     | 5
# 3     | 7
# 4     | 9
# 5     | 11
# 6     | 13
# 7     | 15
# 8     | 17