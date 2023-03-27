import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")

        # Create display
        self.display = tk.Entry(self.master, width=30, borderwidth=5, justify=tk.RIGHT)
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Define buttons
        button_list = ["7", "8", "9", "/", "4", "5", "6", "*", "1", "2", "3", "-", "0", ".", "C", "+"]

        # Create buttons
        row = 1
        col = 0
        for button in button_list:
            command = lambda x=button: self.button_click(x)
            tk.Button(self.master, text=button, padx=20, pady=10, command=command).grid(row=row, column=col)
            col += 1
            if col > 3:
                row += 1
                col = 0

        # Create equals button
        tk.Button(self.master, text="=", padx=50, pady=10, command=self.calculate).grid(row=row, column=0, columnspan=4)

    def button_click(self, button):
        if button == "C":
            self.display.delete(0, tk.END)
        else:
            self.display.insert(tk.END, button)

    def calculate(self):
        try:
            result = eval(self.display.get())
            self.display.delete(0, tk.END)
            self.display.insert(0, result)
        except:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error")

# Create window
root = tk.Tk()

# Create calculator
calculator = Calculator(root)

# Run window
root.mainloop()
