'''
Homework for the week of June 13th, 2022

Using dictionary data structures in Python

'''

# initlaize an empty dictionary called NamesDictionary

NamesDictionary = {}
MainMenuTitle = "Main menu"


def display_greeting():
    print("\n\nWelcome to the Names Dictionary\n"
          "program. This program stores some names\n"
          "and ages in a Dictionary type data structure.\n")
    return


def add_name_to_dict():
    temp_first_name = \
        input("\nEnter a first name:")

    temp_age = \
        input("What is " + temp_first_name \
              + "'s age?")

    NamesDictionary[temp_first_name] = temp_age
    return


def view_dictionary():
    print("\nHere is the entire contents"
          "of the dictionary:\n\n")

    print(NamesDictionary)
    print("\n")
    return


def do_menu():
    print("\n" + MainMenuTitle + "\n\n"
                                 "<A> to add a name to the dictionary,\n"
                                 "<V> to view the entire dictionary.\n"
                                 "<Q> to quit the program.\n")

    temp = input("Your choice?")
    return (temp)


def do_main():
    display_greeting()

    while (True):

        result = do_menu()
        result = result.upper()

        if result == "A":
            add_name_to_dict()

        elif result == "V":
            view_dictionary()

        elif result == "Q":
            break

        else:
            print("\nMenu error!\n")


# Module/import check
if __name__ == "__main__":
    do_main()

print("\nProgram exiting...")
