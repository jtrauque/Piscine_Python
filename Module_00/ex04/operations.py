import sys

if len(sys.argv) == 3:
    if not sys.argv[1].isdigit() or not sys.argv[2].isdigit():
        print("InputError: only numbers\n\nUsage: python operations.py <number1> <number2>\nExample:\n      python operations.py 10 3")
    else:
        try: 
            x = int(sys.argv[1])
            y = int(sys.argv[2])
            print('{0: <12}'.format("Sum:"), x + y)
            print('{0: <12}'.format("Difference:"), x - y)
            print('{0: <12}'.format("Product:"), x * y)
            print('{0: <12}'.format("Quotient:"), x / y)
            print('{0: <12}'.format("Reminder:"), x % y)
        except ValueError:
            print("InputError: only numbers\n\nUsage: python operations.py <number1> <number2>\nExample:\n      python operations.py 10 3")
        except ZeroDivisionError:
            print('{0: <12}'.format("Quotient:"), "ERROR (div by zero)")
            print('{0: <12}'.format("Reminder:"), "ERROR (modulo by zero)")
elif len(sys.argv) > 3:
    print("InputError: too many arguments\n\nUsage: python operations.py <number1> <number2>\nExample:\n        python operations.py 10 3")
else: 
    print("Usage: python operations.py <number1> <number2>\nExample:\n        python operations.py 10 3")

