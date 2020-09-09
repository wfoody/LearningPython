#first_number = input("Enter first number: ")
#second_number = input("Enter second number: ")

#esult = float(first_number) + float(second_number)
#(second_number)
#print(result)

def calculate_tip(total_cost, percentage):
    return total_cost * (percentage/100)

tip = calculate_tip(100, 2)

if tip >= 10:
    print("You are very generous")
elif tip < 10 and tip >= 5:
    print("You are a bad tipper")
else:
    print("you suck")
print(tip)

def greet(name):
    print(f"Hello {name}")


greet("Will")

print(20)