print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")

    age = int(input("What is your age: "))
    if age <= 16:
        print("YOU PAY 10")

    elif age <= 12:
        print("you pay 8")
    elif age <= 10:
        print("you pay 5")

    else:
        print("your too young")
else:
    print("Sorry you have to grow taller before you can ride.")


"""
Nested if else

if condition:
    if another condition:
        do this
    else:
        do this
else:
    do this


"""