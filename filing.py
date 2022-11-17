print("Choose an option: ")
print("1:Read")
print("2: Append")
choice = int(input("Your choice: "))

if choice == 1:
    file1 = open("testfile.txt", "r")
    while True:
        name = file1.readline().strip()
        if name == "":
            break
        age = file1.readline().strip()
        subject = file1.readline().strip()
        print(f"The name is {name}, age is {age} and subject is {subject}.")
    file1.close()
elif choice == 2:
    file1 = open("testfile.txt", "a")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    subject = input("Enter Subjecr: ")
    file1.writelines(name+"\n")
    file1.writelines(age+"\n")
    file1.writelines(subject+"\n")
    file1.close()



