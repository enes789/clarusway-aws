number = input(""" ###  This program converts milliseconds into hours, minutes, and seconds ###
(To exit the program, please type "exit")
Please enter the milliseconds (should be greater than zero) :  """)

while number.lower() != "exit":
    if number.isdecimal():
        num = int(number)

        if num < 1000:
            print(f"just {num} millisecond/s")
        else:
            a = num // 1000

            if a < 60:
                print(f"{a} second/s")
            else:
                b = a // 60
                if b < 60:
                    x = a % 60
                    if x > 0:
                        print(f"{b} minute/s {x} second/s")
                    else:
                        print(f"{b} minute/s")
                else:
                    c = b // 60
                    d = a % 60
                    y = b % 60
                      
                    if d == 0 and y == 0:
                        print(f"{c} hour/s")
                    elif y == 0:
                        print(f"{c} hour/s {d} second/s")
                    elif d == 0:
                            print(f"{c} hour/s {y} minute/s")
                    else:
                         print(f"{c} hour/s {y} minute/s {d} second/s")

    else:
        print("Not Valid Input !!!")

    number = input(""" ###  This program converts milliseconds into hours, minutes, and seconds ###
(To exit the program, please type "exit")
Please enter the milliseconds (should be greater than zero) :  """)
    if number.lower() == exit:
        print("Exiting the program... Good Bye")
        break
        

print("Exiting the program... Good Bye")