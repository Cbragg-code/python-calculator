from calculator import Calculator
from file_manager import save_variables, load_variables


def main():
    calc = Calculator()

    print("Python CLI Calculator (Type 'exit' to quit)")

    while True:
        command = input("> ").strip()

        if command.lower() == "exit":
            print("Exiting Calculator...")
            break

        elif command.lower() == "clear":
            calc.clear()
            print("Result cleared.")

        elif command.lower() == "undo":
            calc.undo()
            print(f"Result: {calc.result}")

        elif command.lower() == "redo":
            calc.redo()
            print(f"Result: {calc.result}")

        elif command.lower() == "sqrt":
            calc.square_root()
            print(f"Result: {calc.result}")

        elif command.lower() == "sq":
            calc.square()
            print(f"Result: {calc.result}")

        elif command.lower() == "fact":
            calc.factorial()
            print(f"Result: {calc.result}")

        else:
            tokens = command.split()

            if len(tokens) == 1:
                try:
                    calc.result = float(tokens[0])
                    print(f"Result set to: {calc.result}")
                except ValueError:
                    print("Invalid input. Type a number or a valid command.")