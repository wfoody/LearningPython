
star = "*"
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

