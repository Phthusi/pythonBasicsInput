# name = input('Enter name: ')
# age = input('Enter age: ')
# location = input('Enter location: ')
# print(f'"Hello {name}, you are {age} years old and live in {location}."')

def add(num1,num2):
    return num1 + num2

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b==0:
        return 'b cannot be zero'
    return a / b 

def is_valid_operation():
    operations = ('+', '-', '*', '/')
    operation = input('Enter the operation: ')
    if operation in operations:
        return operation
    print(f'{operation} is not a valid operation, a valid should be -,+,* or /')
    return 0

def is_valid_num(num_name):
    num = input(f'Enter the {num_name} number: ')
    try:
        return float(num)
    except Exception:
        print(f'{num} is not a valid number')
        return ''

def run():
    first_number = ''
    second_number = ''
    operation = 0
    operations = { "+": add, "-": subtract, "*": multiply, "/": divide }
    
    while first_number=='' or second_number=='' or operation==0:
        first_number  = is_valid_num('first') if first_number==''  else first_number
        if first_number == '': continue
        second_number = is_valid_num('second') if second_number=='' else second_number
        if second_number=='': continue
        operation = is_valid_operation() if not(operation) else operation
    
    result = operations[operation](first_number, second_number)
    print("The result of", first_number, operation, second_number, "is", result)

if __name__ == '__main__':
    run()