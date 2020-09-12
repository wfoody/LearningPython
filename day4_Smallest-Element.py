numbers = [384, 84, 489, 2347, 47, 94]

#print(min(numbers))

#alternative

def finding_smallest(numbers):

    smallestSeen = numbers[0]

    for i in numbers:
        if i < smallestSeen:
            smallestSeen = i
    return smallestSeen

smallestSeen = finding_smallest(numbers)
print(smallestSeen)




