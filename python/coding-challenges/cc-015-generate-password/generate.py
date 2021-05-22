import random

def generate_password(name):
    first_3 = random.sample(name, k=3)
    last_4 = random.sample(range(10), k=4)
    a, b = "", ""
    for i in first_3:
        a += i
    for i in last_4:
        b += str(i)
    return a + b

name = input("Please enter your full name: ").lower()
print(generate_password(name))