num_additions = int(input("How many numbers do you want to add? "))

total = 0

for _ in range(num_additions):
    num = float(input("Enter a number to add: "))
    total += num

print("The total sum is:", total)