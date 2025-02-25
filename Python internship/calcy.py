from tkinter import *

def add_numbers():
    first_num = float(first_number_entry.get())
    second_num = float(second_number_entry.get())
    result_label.config(text=f"{int(first_num + second_num)}")

def subtract_numbers():
    first_num = float(first_number_entry.get())
    second_num = float(second_number_entry.get())
    result_label.config(text=f"{int(first_num - second_num)}")

def multiply_numbers():
    first_num = float(first_number_entry.get())
    second_num = float(second_number_entry.get())
    result_label.config(text=f"{int(first_num * second_num)}")

def divide_numbers():
    first_num = float(first_number_entry.get())
    second_num = float(second_number_entry.get())
    if second_num == 0:
        result_label.config(text="Division by Zero not possible")
    else:
        result_label.config(text=f"{int(first_num // second_num)}")

# Main window setup
calculator_window = Tk()
calculator_window.title("Calculator")
calculator_window.config(padx=30, pady=30)

# Title label
title_label = Label(text="CALCULATOR")
title_label.grid(column=1, row=0)

# Input labels and entries
first_number_label = Label(text="Enter the first number")
first_number_label.grid(column=0, row=1)

second_number_label = Label(text="Enter the second number")
second_number_label.grid(column=0, row=2)

first_number_entry = Entry(width=15)
first_number_entry.grid(column=1, row=1)

second_number_entry = Entry(width=15)
second_number_entry.grid(column=1, row=2)

# Operation buttons
add_button = Button(text="ADD", command=add_numbers)
add_button.grid(column=0, row=4)

subtract_button = Button(text="SUBTRACT", command=subtract_numbers)
subtract_button.grid(column=1, row=4)

multiply_button = Button(text="MULTIPLY", command=multiply_numbers)
multiply_button.grid(column=0, row=5)

divide_button = Button(text="DIVIDE", command=divide_numbers)
divide_button.grid(column=1, row=5)

# Result display
result_text_label = Label(text="RESULT")
result_text_label.grid(column=0, row=3)

result_label = Label(text="")
result_label.grid(column=1, row=3)

# Run the application
calculator_window.mainloop()
