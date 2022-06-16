'''
Homework for the week of June 13th, 2022
by Michael Macks McCosh @MacksM3
Using dictionary data structures in Python
Keeping operation similar to CLI starter code,
every menu item calls a popup page
'''

import tkinter as tk

# initlaize a startup dictionary called NamesDictionary

NamesDictionary = {'Zac': '27', 'Hal': '40', 'Max': '63', 'Bob': 'older than dirt'}


def display_greeting():         # included in starter code
    return ("\n\nWelcome to the Names Dictionary\n"
            "program. This program stores some names\n"
            "and ages in a Dictionary type data structure.\n")


def add_name_to_dict():
    def add_submit():
        temp_first_name = name_entry.get().title()  # this is the key of key:value pair
        temp_age = age_entry.get()  # this is the value of key:value pair
        NamesDictionary[temp_first_name] = temp_age
        add_name_label.config(text=f"Added {temp_first_name}, age {temp_age}")
        # tk.Label(add_window, text=f"Added {temp_first_name}, age {temp_age}").pack()
        name_entry.delete(0, "end")     # clear name entry
        age_entry.delete(0, "end")      # clear age entry

    add_window = tk.Toplevel()       # popup page
    add_window.geometry("400x200")
    tk.Label(add_window, text="\nAdd contents to the dictionary:").pack()

    # use frames to put label and entry box side by side without using grid
    name_frame = tk.Frame(add_window, width=380)
    name_frame.pack()
    name_entry = tk.Entry(name_frame)
    name_entry.pack(side="right")
    tk.Label(name_frame, text="Enter a first name: ").pack(side="right")

    age_frame = tk.Frame(add_window, width=380)
    age_frame.pack()
    age_entry = tk.Entry(age_frame)
    age_entry.pack(side="right")
    tk.Label(age_frame, text="What is their age? ").pack(side="right")

    tk.Button(add_window, text="Submit", command=add_submit).pack(pady=8)
    add_name_label = tk.Label(add_window, text=" ")
    add_name_label.pack()

    close_add_button = tk.Button(add_window, text='Close', command=add_window.destroy)
    close_add_button.pack(side="bottom", pady=8)

    return


def calculate_number():
    number_of_names = len(NamesDictionary)
    count_window = tk.Toplevel()       # popup page
    count_window.geometry("400x200")
    tk.Label(count_window, text=f"Number of names: {number_of_names}").pack(pady=30)
    # print(f"Number of names: {number_of_names}")
    close_count_button = tk.Button(count_window, text='Close', command=count_window.destroy)
    close_count_button.pack(side="bottom", pady=10)
    return


def delete_name_from_dict():
    # name_to_search = input("Enter name to search: ")
    def delete_submit():
        try:
            name_to_remove = NamesDictionary.pop(name_to_delete.get())
            result_label.config(text=f"deleted {name_to_delete.get()}: {name_to_remove}")
            # print(f"deleted {name_to_search.get()}: {name_to_remove}")
        except:
            result_label.config(text="Error: name not found")
            # print("Error: name not found")

        name_to_delete.delete(0, "end")     # clear search entry

    delete_window = tk.Toplevel()       # popup page
    delete_window.geometry("400x200")
    tk.Label(delete_window, text="\nEnter name to search for:").pack()
    name_to_delete = tk.Entry(delete_window)
    name_to_delete.pack()

    tk.Button(delete_window, text="Submit", command=delete_submit).pack(pady=10)
    result_label = tk.Label(delete_window, text=" ")
    result_label.pack()

    close_delete_button = tk.Button(delete_window, text='Close', command=delete_window.destroy)
    close_delete_button.pack(side="bottom", pady=10)

    return


def search_dictionary():
    # name_to_search = input("Enter name to search: ")
    def search_submit():
        try:
            name_to_display = NamesDictionary.get(name_to_search.get().title())
            if name_to_display:
                # print(f"found {name_to_search}, age {name_to_display}")
                response_label.config(text=f"found {name_to_search.get().title()}, age {name_to_display}")
            else:
                response_label.config(text="search not found")
                # print("search not found")

        except:
            tk.Label(search_window, text="Error: search failed").pack()
            # print("Error: name not found")

        name_to_search.delete(0, "end")     # clear search entry

    search_window = tk.Toplevel()       # popup page
    search_window.geometry("400x200")
    tk.Label(search_window, text="\nEnter name to search: ").pack()
    name_to_search = tk.Entry(search_window)
    name_to_search.pack()

    tk.Button(search_window, text="Submit", command=search_submit).pack(pady=10)
    response_label = tk.Label(search_window, text=" ")
    response_label.pack()

    close_search_button = tk.Button(search_window, text='Close', command=search_window.destroy)
    close_search_button.pack(side="bottom", pady=10)

    return


def view_dictionary():
    view_window = tk.Toplevel()       # popup page
    # view_window.geometry("400x200")
    # use padx to set window width and let height expand as list grows
    # a widget with scrolling would be next upgrade
    tk.Label(view_window, text="\nHere is the entire contents of the dictionary:\n").pack(padx=50)
    # for loop to show each item on its own line, or maybe use listbox
    for k, v in NamesDictionary.items():
        tk.Label(view_window, text=f"{k}, age; {v}").pack()
    # tk.Label(view_window, text=NamesDictionary).pack()

    close_view_button = tk.Button(view_window, text='Close', command=view_window.destroy)
    close_view_button.pack(side="bottom", pady=10)

    # print("\nHere is the entire contents of the dictionary:\n\n")
    # print(NamesDictionary)
    # print("\n")
    return


def main():
    window = tk.Tk()
    window.geometry("400x200")
    window.title("Dictionary Data GUI")
    window.config(background="yellow")
    icon = tk.PhotoImage(file='m3-blue-icon.png')
    window.iconphoto(True, icon)

    menubar = tk.Menu(window)
    window.config(menu=menubar)

    fileMenu = tk.Menu(menubar, tearoff=0, font=("Georgia", 13))
    menubar.add_cascade(label="File", menu=fileMenu, font=("Georgia", 13))
    fileMenu.add_command(label="Add", command=add_name_to_dict)
    fileMenu.add_command(label="Count", command=calculate_number)
    fileMenu.add_command(label="Delete", command=delete_name_from_dict)
    fileMenu.add_command(label="Search", command=search_dictionary)
    fileMenu.add_command(label="View", command=view_dictionary)
    fileMenu.add_separator()
    fileMenu.add_command(label="Quit", command=quit)

    tk.Label(window, text=display_greeting(), bg="yellow", font="none 12").pack()
    tk.Label(window, text="Use file menu above to choose actions", bg="yellow").pack()

    window.mainloop()


# Module/import check
if __name__ == "__main__":
    main()

print("\nProgram exiting...")
