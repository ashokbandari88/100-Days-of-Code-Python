# Coded by Ashok Bandari

print("Welcome to pyCalculator!")

n1 = float(input("What's the first number?: "))

def calculate(n1):
    continue_calculating = True
    while continue_calculating:
        final_total = 0
        operation = input("+\n-\n*\n/\nPick an operation: ")
        n2 = float(input("What's the next number?: "))
        if operation == "+":
            result = n1 + n2
            final_total += result
        elif operation == "-":
            result = n1 - n2
            final_total += result
        elif operation == "*":
            result = n1 * n2
            final_total += result
        elif operation == "/":
            result = n1 / n2
            final_total += result
        print(f"{n1} {operation} {n2} = {final_total}")
        should_continue = input(f"Type 'y' to continue calculating with {final_total}, or Type 'n' to start new calculation: ")
        if should_continue == "y":
            n1 = final_total
        elif should_continue == "n":
            continue_calculating = False

calculate(n1)