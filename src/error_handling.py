import traceback

def demo_error_handling():
    errored = False
    try:
        number1 = int(input("Enter a number: "))
        number2 = int(input("Enter another number: "))
        result = number1 // number2
        if result == 0:
            raise ArithmeticError("Second number should be smaller than first number")
    except ValueError:
        print("You got to enter a number!")
        errored = True
    except ZeroDivisionError:
        print("Second number cannot be zero")
        errored = True
    else:
        print("Here is your result: ", result)
    finally:
        if errored:
            print("Sorry Try again")
        else:
            print("Great job!!")

def main():
    try:
        demo_error_handling()
    except ArithmeticError as ae:
        print(ae)
        traceback.print_exc()


if __name__ == "__main__":
    main()
            
