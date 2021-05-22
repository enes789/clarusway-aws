text = """
1. Find phone number \n
2. Insert a phone number \n
3. Delete a person from the phonebook \n
4. Terminate \n
Select operation on Phonebook App (1/2/3) : """
num = input("Welcome to the phonebook application \n" + text)

db_dict = {}


while num != "4":
    if num.isdecimal():
        number = int(num)
        if number == 1:
            name = input("Find the phone number of :")
            print(db_dict[name])

        elif number == 2:
            name = input("Insert name of the person :")
            tel = int(input("Insert phone number of the person :"))
            db_dict[name] = tel
            print(f"Phone number of {name} is inserted into the phonebook")

        elif number == 3:
            name = input("Whom to delete from phonebook :")
            db_dict.pop(name)
            print(f"{name} is deleted from the phonebook")

        print(db_dict)
    num = input(text)
    if num == "4":
        print("\nExiting Phonebook... Good Bye")
        
        

