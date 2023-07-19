# Week 1 - Part 1 - Exercise
# name = input("Please enter your name. ")
# start_city = input("Which city would you like to start in? ")
# destination_city = input("Which city would you like to end in? ")
# transport = input("How would you like to get there? ")

# print(name, "would like to travel from", start_city, "to", destination_city, f"by way of {transport}!")

# Week 1 - Bonus
# discriminant = b^2 - 4ac
value_a = int(input("Please enter the value of a: "))
value_b = int(input("Please enter the value of b: "))
value_c = int(input("Please enter the value of c: "))

solution = (value_b**2) - 4*(value_a * value_c)

if solution == 0:
    print("The quadratic equation has 1 real solution.")
elif solution > 0:
    print("The quadratic equation has 2 real solutions.")
elif solution < 0:
    print("The quadratic equation has 2 complex solutions.")
else:
    print("Impossible.")