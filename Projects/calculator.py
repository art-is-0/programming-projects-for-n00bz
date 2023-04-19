
def prompt_menu(): 
    a = (float(input('Enter the first number: ')))
    b = (float(input('Enter the second number: ')))
    print("""
Choose an operation from the list:
1. Addition
2. Subtraction
3. Multiplication
4. Exponentiation
5. Division
6. Division with remainder
    """)
    op = int(input('Enter the choose number: '))
    return a, b, op

def calculate():
    a, b, op = prompt_menu()

    match op:
        case 1:
            print('Sum: {} + {} = {}'.format(a,b,a+b))
        case 2:
            print('Difference: {} - {} = {}'.format(a,b,a-b))
        case 3:
            print('Product: {} * {} = {}'.format(a,b,a*b))
        case 4:
            print('Exponent: {} ** {} = {}'.format(a,b,a**b))
        case 5:
            try:
                print("Quotient: {} / {} = {}".format(a,b,a/b))
            except:
                print("Division by 0 is not possible")
        case 6:
            try:
                print("Division with remainder: {} / {} = {} Remainder: {}".format(a,b,a//b,a%b))
            except:
                print('Division by 0 is not possible')
        case _:
            print('No such choice!')
    loop()

def loop():
    choice = str(input('Do you want to continue? (Y/N): '))
    print('')
    if choice.upper() == "Y":
        calculate()
    elif choice.upper() == "N":
        print('Goodbye!')
    else:
        print('Invalid input!')
        print('')
        loop()


def main():
    calculate()

# Check main
if __name__ == '__main__':
     # This code won't run if this file is imported.
     main()