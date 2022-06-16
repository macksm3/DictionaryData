'''
Homework for the week of June 13th, 2022
by Michael Macks McCosh @MacksM3
Using dictionary data structures in Python

'''

# initlaize a startup dictionary called NamesDictionary

NamesDictionary = {'Zac': '27', 'Hal': '40', 'Max': 'older than dirt'}
MainMenuTitle = "Main menu"


def display_greeting():
    print("\n\nWelcome to the Names Dictionary\n"
          "program. This program stores some names\n"
          "and ages in a Dictionary type data structure.\n")
    return


def add_name_to_dict():
    temp_first_name = input("\nEnter a first name:").title()  # this is the key of key:value pair
    # temp_first_name = temp_first_name.title()

    temp_age = input("What is " + temp_first_name + "'s age?")  # this is the value of key:value pair

    NamesDictionary[temp_first_name] = temp_age
    return


def calculate_number():
    number_of_names = len(NamesDictionary)
    print(f"Number of names: {number_of_names}")


def delete_name_from_dict():
    name_to_search = input("Enter name to search: ")
    try:
        name_to_remove = NamesDictionary.pop(name_to_search)
        print(f"delete {name_to_remove}")
    except:
        print("Error: name not found")


def search_dictionary():
    name_to_search = input("Enter name to search: ")
    try:
        name_to_display = NamesDictionary.get(name_to_search)
        if name_to_display:
            print(f"found {name_to_search}, age {name_to_display}")
        else:
            print("search not found")

    except:
        print("Error: name not found")



def view_dictionary():
    print("\nHere is the entire contents"
          "of the dictionary:\n\n")

    print(NamesDictionary)
    print("\n")
    return


def do_menu():
    print("\n" + MainMenuTitle + "\n\n"
                                 "<A> to add a name to the dictionary,\n"
                                 "<C> to calculate the number of names in the dictionary.\n"
                                 "<D> to delete a name from the dictionary.\n"
                                 "<S> to search within the dictionary,\n"
                                 "<V> to view the entire dictionary.\n"
                                 "<Q> to quit the program.\n")

    temp = input("Your choice?")
    return temp


def do_main():
    display_greeting()

    while True:

        result = do_menu()
        result = result.upper()

        if result == "A":
            add_name_to_dict()

        elif result == "C":
            calculate_number()

        elif result == "D":
            delete_name_from_dict()

        elif result == "S":
            search_dictionary()

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
