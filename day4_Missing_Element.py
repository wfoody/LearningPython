# Missing Element

numbers = [0, 1, 3, 4, 5, 6, 7, 8, 9]

def find_missing(numbers):

    for i in range(len(numbers)):
        if i not in numbers:
            return i

print(find_missing(numbers))