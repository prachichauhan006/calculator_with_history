HISTORY_FILE = "History.txt"

def show_history():
    try:
        with open(HISTORY_FILE, 'r') as file:
            lines = file.readlines()
            if len(lines) == 0:
                print("NO HISTORY FOUND!")
            else:
                for line in reversed(lines):
                    print(line.strip())
    except FileNotFoundError:
        print("NO HISTORY FOUND!")

def clear_history():
    with open(HISTORY_FILE, 'w') as file:
        pass
    print("HISTORY CLEARED")

def save_to_history(equation, result):
    with open(HISTORY_FILE, 'a') as file:
        file.write(equation + " = " + str(result) + "\n")

def calculate(user_input):
    operators = ['+', '-', '*', '/', '%', '**']
    for op in operators:
        if op in user_input:
            try:
                num1, num2 = user_input.split(op)
                num1 = float(num1.strip())
                num2 = float(num2.strip())
                
                if op == '+':
                    result = num1 + num2
                elif op == '-':
                    result = num1 - num2
                elif op == '*':
                    result = num1 * num2
                elif op == '/':
                    if num2 == 0:
                        print("CANNOT DIVIDE BY ZERO")
                        return
                    result = num1 / num2
                elif op == '%':
                    result = num1 % num2
                elif op == '**':
                    result = num1 ** num2

                # Clean result (int if no decimal)
                if result == int(result):
                    result = int(result)

                print("Result:", result)
                save_to_history(user_input, result)
                return
            except:
                print("Invalid numbers. Try again.")
                return

    print("INVALID OPERATOR. USE ONLY +, -, *, /, %, **")

def main():
    print('-- SIMPLE CALCULATOR --')
    print("Type expressions like 2+3 or commands like 'history', 'clear', 'exit'")
    while True:
        user_input = input("Enter: ").strip().lower()
        if user_input == 'exit':
            print("GOODBYE!")
            break
        elif user_input == 'history':
            show_history()
        elif user_input == 'clear':
            clear_history()
        else:
            calculate(user_input)

main()
