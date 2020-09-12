# Finding the largest element

numbers = [384, 84, 489, 2347, 47, 94]

numbers.sort()

print(numbers[-1])

#alternative


arg1 = max(numbers)

print(arg1)

print(max(numbers))


#2nd_alternative

def find_largest(numbers):
    
    largestSeen = numbers[0] 

    for x in numbers:
        if x > largestSeen:
            largestSeen = x

    return largestSeen
        
       
largestSeen = find_largest(numbers)
print(largestSeen)