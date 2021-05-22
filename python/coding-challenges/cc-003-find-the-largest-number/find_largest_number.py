listA = []

for i in range(5):
    number = int(input("Enter a number: "))
    listA.append(number)

result = sorted(listA, reverse = True)
print(f"The largest number : {result[0]}")