# a simple calculator with basic arithmetic operations.

def sum(first_num, second_num):
    """This is used to add the inputed values"""
    return first_num + second_num

def sub(first_num, second_num):
    """This is to subtract the inputted values"""
    return first_num - second_num

def mul(first_num, second_num):
    """This is used to multply the inputted values"""
    return first_num * second_num

def div(first_num,second_num):
    """This is used to divide the inputted values"""
    return first_num/second_num
contt = True 
while contt:
    operations = {
        "+": sum,
        "-": sub, 
        "/": div, 
        "*": mul
        }
    first_num = float(input("What is the first number?  \n"))
    for op in operations:
        print(op)

    ops = input("Choose an operation?  \n")
    if ops in operations:
        second_num = float(input("What is the second number?  \n"))

        calculation = operations[ops]
        ans = calculation(first_num, second_num)
        print(f"{first_num} {ops} {second_num} = {ans}")
    else:
        print("Invalid operations")


    cont = input("Type Y to continue and N to continue ").lower()
    if cont == "y".lower():
        contt = True 
    else:
        contt = False 


