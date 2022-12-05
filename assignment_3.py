n = int(input("How many flour bags weights do you want to enter? "))
totalWeight = 0

for i in range(n):
    weight = float(input("Enter weight: "))
    totalWeight = totalWeight + weight
    if weight < 4.5:
        print("Underweight!")
    elif weight > 5.5:
        print("Overweight!")
    elif weight >= 4.5 and weight <= 5.5:
        print("Optimal weight")

average = totalWeight/n
print(f"The Average weight of the flour bags is {average}.")
