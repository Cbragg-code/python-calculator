from calculator import Calculator
from file_manager import save_variables, load_variables

calc = Calculator()


def display_menu():
    print("""
Available Commands:
+ [number/variable]
- [number/variable]
* [number/variable]
/ [number/variable]
mod [number/variable]
exp [number/variable]
sq, sqrt, ! (factorial)
var [name]  -> save current result
set [name]  -> set result to variable
read [file], write [file]
undo, redo, clear, vars, result, exit
""")


menu_actions = {
    '+': lambda val: calc.add(val),
    '-': lambda val: calc.subtract(val),
    '*': lambda val: calc.multiply(val),
    '/': lambda val: calc.divide(val),
    'mod': lambda val: calc.mod(val),
    'exp': lambda val: calc.exponent(val),
    'sq': lambda: calc.square(),
    'sqrt': lambda: calc.square_root(),
    '!': lambda: calc.factorial(),
    'undo': lambda: calc.undo(),
    'redo': lambda: calc.redo(),
    'clear': lambda: calc.clear(),
}


def create_variable(name):
    if name.islower() and name.isalpha():
        calc.create_variable(name)
        print(f"Saved {calc.result} as variable '{name}'")
    else:
        print("Error: Variable names must be lowercase letters only.")


def set_variable(name):
    if name in calc.variables:
        calc.result = calc.variables[name]
        print(f"Result set to value of '{name}': {calc.result}")
    else:
        print(f"Error: Unknown variable '{name}'.")


def get_value(val):
    if val in calc.variables:
        return calc.variables[val]
    try:
        return float(val)
    except ValueError:
        print(f"Error: '{val}' is not a valid number or variable.")
        return None


def main_loop():
    display_menu()
    while True:
        command = input("> ").strip().split()
        if not command:
            continue

        cmd = command[0].lower()

        if cmd == "exit":
            print("Exiting calculator.")
            break

        elif cmd == "result":
            print(f"Result: {calc.result}")

        elif cmd == "vars":
            if calc.variables:
                print("Stored Variables:")
                for k, v in calc.variables.items():
                    print(f"  {k}: {v}")
            else:
                print("No variables stored.")

        elif cmd == "var" and len(command) == 2:
            create_variable(command[1])

        elif cmd == "set" and len(command) == 2:
            set_variable(command[1])

        elif cmd == "read" and len(command) == 2 and command[1] == "vars":
            calc.variables = load_variables()
            print("Variables loaded from variables.json")

        elif cmd == "write" and len(command) == 2 and command[1] == "vars":
            save_variables(calc.variables)
            print("Variables saved to variables.json")

        elif cmd in menu_actions:
            if len(command) == 2:
                val = get_value(command[1])
                if val is not None:
                    menu_actions[cmd](val)
                    print(f"Result: {calc.result}")
            elif len(command) == 1:
                if cmd in ['sq', 'sqrt', '!', 'undo', 'redo', 'clear']:
                    menu_actions[cmd]()
                    if cmd != "clear":
                        print(f"Result: {calc.result}")
                else:
                    print("Error: Missing operand.")
            else:
                print("Error: Invalid input format.")

        elif len(command) == 3:
            # Format: number/operator/number OR var/operator/var
            left, operator, right = command
            if operator not in menu_actions:
                print("Error: Unknown operator.")
                continue
            left_val = get_value(left)
            right_val = get_value(right)
            if left_val is None or right_val is None:
                continue
            calc.result = left_val
            menu_actions[operator](right_val)
            print(f"Result: {calc.result}")

        else:
            print("Error: Invalid command or usage.")


if __name__ == "__main__":
    main_loop()
