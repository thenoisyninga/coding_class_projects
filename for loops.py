# FOR LOOPS

evenCounter = 0
oddCounter = 0

for i in range(10):
    num = int(input("Enter an integer: "))
    if (num % 2) == 0:
        evenCounter += 1
    else:
        oddCounter += 1

print(f"There were {evenCounter} even values, and {oddCounter} odd values.")

# FOR EACH LOOPS

namesList = ["saRiM", "aYeSha", "SHafaq", "moosA", "baTool"]

for name in namesList:
    print(name.upper()[0] + name.lower()[1:])
