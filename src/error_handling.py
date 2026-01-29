def demo_error_handling():
    errored = False
    try:
        number1 = int(input("Enter a number: "))
        number2 = int(input("Enter another number: "))
        result = number1 // number2
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
    demo_error_handling()


if __name__ == "__main__":
    main()
            
