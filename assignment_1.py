# A program that asks a person's information (name, age), And then checks if the person was born in the 90s, or the 80s
#
name = input("Enter your name: ")
age = int(input("Enter your age: "))

year = 2022 - age

if str(year)[-2] == "8":
    print("You were born in 80's")
if str(year)[-2] == "9":
    print("You were born in 90's")

