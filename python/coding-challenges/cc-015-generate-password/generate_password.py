import random

name = input("Please enter your full name: ").lower()
number = "0123456789"
first_3 = random.sample(name, k=3)
a, b = "", ""
for i in first_3:
    a += i
last_4 = random.sample(number, k=4)
for i in last_4:
    b += i
print(a + b)