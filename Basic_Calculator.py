while True:
    print()
    print("This is a Basic Calculator, can only do +, -, *, / with two numbers, and it returns a rounded integer number, more info refers to README")
    print()
    num_1 = int(input(" number1: "))  # Taking the variable from the user
    operator = input("  [+ - * /]: ")  # Taking the operator from the user
    # Taking the Second variable from the user
    num_2 = int(input(" number2: "))
    operator_dict = {  # Crate a dict of the calculations

        '+': num_1 + num_2,
        '-': num_1 - num_2,
        '*': num_1 * num_2,
        '/': num_1 / num_2
    }
    # Search the dict and do the calculations
    result = operator_dict.get(operator, "Type in operator and compute")
    print("  Result is %d, the decimal is rounded" % result)
    print()
    Continue = input("Have other numbers needs to be calculate? Y/N:")
    if Continue == 'Y':
        print()
        continue
    elif Continue == 'N':
        print("The program has shuted down")
        break
    else:
        print("Please press Y or N on your keyboard")
