
totalWeight = 0
weight = 0
counter = 0
while weight >= 0:
    weight = float(input("Enter weight: "))
    if weight >= 0:
        totalWeight = totalWeight + weight
        counter = counter + 1
        if weight < 4.5:
            print("Underweight!")
        elif weight > 5.5:
            print("Overweight!")
        elif weight >= 4.5 and weight <= 5.5:
            print("Optimal weight")
    else:
        print("No longer taking inputs")

print(counter)
print(totalWeight)
average = totalWeight / counter
print(f"The Average weight of the flour bags is {average}.")
