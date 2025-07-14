import tkinter as tk
from calculator import Calculator

calc = Calculator()


# Update the result display
def update_display():
    display_var.set(f"{calc.result}")


# Handle number and decimal input
def input_number(value):
    current = input_var.get()
    input_var.set(current + value)


# Clear input field
def clear_input():
    input_var.set("")


# Handle operator buttons (+, -, *, /, mod, exp)
def operate(operator):
    entry = input_var.get()
    try:
        number = float(entry)
    except ValueError:
        display_var.set("Invalid input")
        return
    if operator == "+":
        calc.add(number)
    elif operator == "-":
        calc.subtract(number)
    elif operator == "*":
        calc.multiply(number)
    elif operator == "/":
        calc.divide(number)
    elif operator == "%":
        calc.mod(number)
    elif operator == "exp":
        calc.exponent(number)
    clear_input()
    update_display()


# Handle special operations (sq, sqrt, factorial, undo, redo, clear)
def simple_operation(op):
    if op == "sq":
        calc.square()
    elif op == "sqrt":
        calc.square_root()
    elif op == "fact":
        calc.factorial()
    elif op == "undo":
        calc.undo()
    elif op == "redo":
        calc.redo()
    elif op == "AC":
        calc.clear()
    clear_input()
    update_display()


root = tk.Tk()
root.title("Simple Calculator")

# Display Frame
display_var = tk.StringVar()
display_label = tk.Label(root, textvariable=display_var, font=("Arial", 24),
                         bg="black", fg="white", width=15, anchor="e")
display_label.grid(row=0, column=0, columnspan=4)
update_display()

# Input Field (hidden but tracks input)
input_var = tk.StringVar()
input_entry = tk.Entry(root, textvariable=input_var, font=("Arial", 14),
                       width=15, justify="right")
input_entry.grid(row=1, column=0, columnspan=4)

# Button Layout
buttons = [
    ("AC", lambda: simple_operation("AC")),
    ("undo", lambda: simple_operation("undo")),
    ("redo", lambda: simple_operation("redo")),
    ("/", lambda: operate("/")),
    ("7", lambda: input_number("7")),
    ("8", lambda: input_number("8")),
    ("9", lambda: input_number("9")),
    ("*", lambda: operate("*")),
    ("4", lambda: input_number("4")),
    ("5", lambda: input_number("5")),
    ("6", lambda: input_number("6")),
    ("-", lambda: operate("-")),
    ("1", lambda: input_number("1")),
    ("2", lambda: input_number("2")),
    ("3", lambda: input_number("3")),
    ("+", lambda: operate("+")),
    ("0", lambda: input_number("0")),
    (".", lambda: input_number(".")),
    ("%", lambda: operate("%")),
    ("exp", lambda: operate("exp")),
    ("sq", lambda: simple_operation("sq")),
    ("sqrt", lambda: simple_operation("sqrt")),
    ("fact", lambda: simple_operation("fact"))
]

row_start = 2
col_start = 0
for idx, (text, cmd) in enumerate(buttons):
    row = row_start + idx // 4
    col = idx % 4
    tk.Button(root, text=text, width=6, height=2,
              font=("Arial", 14), command=cmd).grid(row=row, column=col)

root.mainloop()
