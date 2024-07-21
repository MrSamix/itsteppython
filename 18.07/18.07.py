#task1
from tkinter import *

def show_name():
    name = entryname.get()
    surname = entrysurname.get()
    label.config(text=f"Full name: {name} {surname}")

root = Tk()
root.title("Form")
root.geometry("200x200")

label_name = Label(root, text="Name:")
label_name.pack()
entryname = Entry(root)
entryname.pack()

label_surname = Label(root, text="Surname:")
label_surname.pack()
entrysurname = Entry(root)
entrysurname.pack()

button = Button(root, text="Show", command=show_name)
button.pack()

label = Label(root, text="")
label.pack()

root.mainloop()


#task 2

root = Tk()
root.title("Calculator")
root.geometry("550x600")

def plus():
    first = int(first_num.get())
    second = int(second_num.get())
    resoult_num = first + second
    result.config(text=f"Result: {resoult_num}")


def minus():
    first = int(first_num.get())
    second = int(second_num.get())
    resoult_num = first - second
    result.config(text=f"Result: {resoult_num}")

def multiply():
    first = int(first_num.get())
    second = int(second_num.get())
    resoult_num = first * second
    result.config(text=f"Result: {resoult_num}")

def share():
    first = int(first_num.get())
    second = int(second_num.get())
    resoult_num = first / second
    result.config(text=f"Result: {resoult_num}")


first_num_l = Label(text="First Number", font=("Arial", 10))
first_num_l.pack()
first_num = Entry(width=10, justify="left")
first_num.pack()

second_num_l = Label(text="Second Number", font=("Arial", 10))
second_num_l.pack()
second_num = Entry(width=10, justify="left")
second_num.pack()

plus_button = Button(text="+", width=7, command=plus)
plus_button.pack(pady=10)

minus_button = Button(text="-", width=7, command=minus)
minus_button.pack(pady=10)

multiply_button = Button(text="*", width=7, command=multiply)
multiply_button.pack(pady=10)

share_button = Button(text="/", width=7, command=share)
share_button.pack(pady=10)

result = Label(width=10, anchor="center", font=("Arial", 20))
result.pack()

root.mainloop()