import operations
from operations import Math_functions
import random
import os
# Add a check to make sure the user input is a number.
points = 0
signs = ("+", "-", "*", "/")
answer = None
num_pool = 10
counter = None
def difficulty(counter):
    while True:
        try:
            counter = int(input("Enter difficulty(Number): "))
            if counter >= 0:
                break
            else: 
                print("Difficulty cannot be negative.")
        except ValueError:
            print("This is not a number.")
    return counter
operators_file = "operations.py"
if os.path.exists(operators_file):
    print(f"{operators_file} is visible")
while True:
    counter = difficulty(counter)
    running = True
    points = 0
    num_pool = 10
    while running:
        print("----------------")
        print()
        print(f"Points: {points}")
        print()
        print("----------------")
        # when I get better at mathematics, change it to uniform
        first_number = round(random.randint(1, num_pool), 2)
        second_number = round(random.randint(1,num_pool), 2)
        number = Math_functions()
        sign = random.choice(signs)
        if sign == "+":
            answer = round(number.plus(first_number, second_number), 2)
        elif sign == "-":
            answer = round(number.minus(first_number, second_number), 2)
        elif sign == "*":
            answer = round(number.multi(first_number, second_number), 2)
        elif sign == "/":
            answer = round(number.divide(first_number, second_number), 2)
        print()
        guess = float(input(f" {first_number} {sign} {second_number} = "))
        print()
        print("----------------")
        print()
        if guess == answer:
            points += 10
            num_pool += counter
        else:
            print("YOU LOSE")
            running = False
    print()
    print("----------------")
    print()
    print(f"Final Score: {points}")
    print()
    print("----------------")
    print()
    restart = input("Restart(Y/N): ").upper()
    if restart == "N":
        break