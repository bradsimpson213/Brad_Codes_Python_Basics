# The INPUT built in function
# DOCS URL:  https://docs.python.org/3.9/library/functions.html?highlight=built

bad_input = True

while bad_input:
    try:
        user_input = int(input("Please enter some text: "))
        print(user_input)
        print("STR check", type(user_input) == str)
        print("INT check", type(user_input) == int)

    except ValueError:
        print("We need to enter number characters only, try again!")


    else: 
        bad_input = False