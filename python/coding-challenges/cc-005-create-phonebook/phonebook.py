db_dict = {}
def phonebook(number):
    
    if number == 1:
        name = input("Find the phone number of :")
        if db_dict == {}:
            return f"You haven't entered number of {name} yet"
        return db_dict[name]

    elif number == 2:
        name = input("Insert name of the person :")
        tel = int(input("Insert phone number of the person :"))
        db_dict[name] = tel
        return f"Phone number of {name} is inserted into the phonebook"

    elif number == 3:
        name = input("Whom to delete from phonebook :")
        db_dict.pop(name)
        return f"{name} is deleted from the phonebook"


# flag to show warning to the user, default is False.
is_invalid = False

# start endless loop to get user input continuously
print("Welcome to the phonebook application")
while True:
    # info text to be shown to the user
    info = """
    1. Find phone number \n
    2. Insert a phone number \n
    3. Delete a person from the phonebook \n
    4. Terminate \n
    Select operation on Phonebook App (1/2/3) : """

    # get the user input after showing info text.
    # if is_invalid set to True then show additional warning to the user
    # pass the input the alphanum variable after stripping white space characters
    alphanum = input('\nInvalid input format, cancelling operation ...\n'*is_invalid + info).strip()
    # if the input is not decimal number
    if not alphanum.isdecimal():
        is_invalid = True
        continue
    # convert the given string to the integer
    number = int(alphanum)
    # if the number is between 1 and 3999, inclusively
    if 0 < number < 4:
        # then convert to roman numerals and print out the user
        print(phonebook(number))
        # and set invalid flag to the False, it might be set the True in previous cycle
        is_invalid = False
    # Exiting the program
    elif number == 4:
        print("\nExiting Phonebook... Good Bye")
        break

    else:
        # then set to invalid flag to True to show warning
        is_invalid = True

    print(db_dict)


    
        
        

