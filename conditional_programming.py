
# THE BOOLEAN DATATYPE
True
# or
False


# Conditions

age = 21

# print(age != 18) # EQUATES TO True
# print(age == 18) # EQUATES TO False


# IF ELSE STATEMENT (Nested)
if age >= 18:
    print("You qualify as an adult")
else:
    if age > 10:
        print("You are above 10 but not an adult")
    else:
        print("Sorry, you are under 10")

# IF ELSE STATEMENT (ELIF)
if age >= 18:
    print("You qualify as an adult")
elif age > 10:
    print("You are above 10 but not an adult")
else:
    print("Sorry, you are under 10")

# A program that asks a person's information (name, age), And then checks if the person was born in the 90s, or the 80s
