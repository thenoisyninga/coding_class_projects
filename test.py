marksObt = float(input("Enter your Marks: "))
marksTot = int(input("Total Marks: "))


percentage = (marksObt/marksTot) * 100

if percentage >= 90:
    print("Your grade is A")
elif percentage >= 80:
    print("Your grade is B.")
elif percentage >= 70:
    print("Your grade is C")
elif percentage >= 60:
    print("Your grade is D")
elif percentage >= 50:
    print("Your grade is E")
else:
    print("U")


