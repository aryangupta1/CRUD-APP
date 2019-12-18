from tkinter import *
from tkinter import messagebox
from db import Database

db = Database('users.db')


# Functions for add, remove, update, delete and populate list

def populate_list():
    list_box.delete(0, END)
    for row in db.fetch():
        list_box.insert(END, row)


def add_item():
    if firstName_text.get() == '' or lastName_text.get() == '' or age_text.get() == '' or occupation_text.get() == '':
        messagebox.showerror('Required Fields', 'Please include all fields')
        return
    db.insert(firstName_text.get(), lastName_text.get(), age_text.get()
              , occupation_text.get())
    list_box.delete(0, END)
    list_box.insert(END, (firstName_text.get(), lastName_text.get(), age_text.get()
                          , occupation_text.get()))
    clear_text()
    populate_list()


def select_item(event):
    try:
        global selected_item
        index = list_box.curselection()[0]
        selected_item = list_box.get(index)

        firstName_entry.delete(0, END)
        firstName_entry.insert(END, selected_item[1])

        lastName_entry.delete(0, END)
        lastName_entry.insert(END, selected_item[2])

        age_entry.delete(0, END)
        age_entry.insert(END, selected_item[3])

        occupation_entry.delete(0, END)
        occupation_entry.insert(END, selected_item[4])
    except IndexError:
        pass


def remove_item():
    db.remove(selected_item[0])
    clear_text()
    populate_list()


def update_item():
    db.update(selected_item[0], firstName_text.get(), lastName_text.get(), age_text.get()
              , occupation_text.get())
    populate_list()


def clear_text():
    firstName_entry.delete(0, END)
    lastName_entry.delete(0, END)
    age_entry.delete(0, END)
    occupation_entry.delete(0, END)


# Creating root window
root = Tk()

root.title('CRUD APP')
root.geometry('700x350')

# First name

firstName_text = StringVar()
firstName_label = Label(root, text='First Name', font=('bold', 14), pady=20)
firstName_label.grid(row=0, column=0, sticky=W)
firstName_entry = Entry(root, textvariable=firstName_text)
firstName_entry.grid(row=0, column=1)

# last Name
lastName_text = StringVar()
lastName_label = Label(root, text='Last Name', font=('bold', 14))
lastName_label.grid(row=0, column=2, sticky=W)
lastName_entry = Entry(root, textvariable=lastName_text)
lastName_entry.grid(row=0, column=3)

# Age

age_text = StringVar()
age_label = Label(root, text='Age', font=('bold', 14))
age_label.grid(row=1, column=0, sticky=W)
age_entry = Entry(root, textvariable=age_text)
age_entry.grid(row=1, column=1)

# Occupation

occupation_text = StringVar()
occupation_label = Label(root, text='Occupation', font=('bold', 14))
occupation_label.grid(row=1, column=2, sticky=W)
occupation_entry = Entry(root, textvariable=occupation_text)
occupation_entry.grid(row=1, column=3)

# List Box
list_box = Listbox(root, height=8, width=50, border=0)
list_box.grid(row=3, column=0, columnspan=3, rowspan=6, pady=20, padx=20)

# Bind select to listbox
list_box.bind('<<ListboxSelect>>', select_item)

# Scrollbar
scrollbar = Scrollbar(root)
scrollbar.grid(row=3, column=3)

# Connect scrollbar to listbox
list_box.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=list_box.yview)

# CRUD Buttons
add_button = Button(root, text='ADD', width=12, command=add_item)
add_button.grid(row=2, column=0, pady=20)

remove_button = Button(root, text='REMOVE', width=12, command=remove_item)
remove_button.grid(row=2, column=1)

update_button = Button(root, text='UPDATE', width=12, command=update_item)
update_button.grid(row=2, column=2)

delete_button = Button(root, text='CLEAR', width=12, command=clear_text)
delete_button.grid(row=2, column=3)

# Populate data
populate_list()
# Starts root window
root.mainloop()
