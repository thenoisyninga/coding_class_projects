
marksSheet = {}

Max = -1
highestname = ""


z = int(input("Enter total marks:"))
for i in range(5):
    x = float(input("Enter Marks:"))
    y = str(input("Enter Name:"))
    perc = (x/z)*100
    marksSheet[y] = perc
    if perc > Max:
        Max = perc
        highestname= y
    if perc >= 90:
        print("A")
    elif perc >=80:
        print("B")
    elif perc >=70:
        print("C")
    elif perc >=60:
        print("D")
    elif perc >=50:
        print("E")
    else:
        print("U")
print(f"The highest marks are: {Max}")
print(f"The student with highest marks:{highestname}")
print("\nHere are all the marks")


for name in marksSheet:
    print(f"{name} : {marksSheet[name]}%")