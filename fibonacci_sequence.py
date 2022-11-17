# Asked for the amount of numbers to generate
sequenceLength = int(input("How many numbers do you want?"))
sequence = [0, 1]

# for the amount of numbers to be generated, we added to the sequence,the sum of the last two numbers in the sequence
for i in range(sequenceLength - 2):
    sequence.append(sequence[-1] + sequence[-2])
    
print(f"[+] These are {sequenceLength} fibonacci numbers:")

for number in sequence:
    print(number)