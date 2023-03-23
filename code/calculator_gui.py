import tkinter as tk

# Function to perform addition
def add():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        result = num1 + num2
        label_result.config(text="Result: " + str(result))
    except ValueError:
        label_result.config(text="Invalid input")

# Function to perform subtraction
def subtract():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        result = num1 - num2
        label_result.config(text="Result: " + str(result))
    except ValueError:
        label_result.config(text="Invalid input")

# Function to perform multiplication
def multiply():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        result = num1 * num2
        label_result.config(text="Result: " + str(result))
    except ValueError:
        label_result.config(text="Invalid input")

# Function to perform division
def divide():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        result = num1 / num2
        label_result.config(text="Result: " + str(result))
    except ValueError:
        label_result.config(text="Invalid input")
    except ZeroDivisionError:
        label_result.config(text="Cannot divide by zero")

# Create the main window
window = tk.Tk()
window.title("Simple Calculator")

# Create the number input fields
label_num1 = tk.Label(window, text="Number 1:")
label_num1.pack()
entry_num1 = tk.Entry(window)
entry_num1.pack()

label_num2 = tk.Label(window, text="Number 2:")
label_num2.pack()
entry_num2 = tk.Entry(window)
entry_num2.pack()

# Create the operation buttons
button_add = tk.Button(window, text="+", width=10, command=add)
button_add.pack()

button_subtract = tk.Button(window, text="-", width=10, command=subtract)
button_subtract.pack()

button_multiply = tk.Button(window, text="*", width=10, command=multiply)
button_multiply.pack()

button_divide = tk.Button(window, text="/", width=10, command=divide)
button_divide.pack()

# Create the result label
label_result = tk.Label(window, text="Result: ")
label_result.pack()

# Run the main loop
window.mainloop()
