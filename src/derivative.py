from sympy import *

#pass any function and the x value and delta x
def derivative_x(f, x, delta_x):
    m = (f(x + delta_x) - f(x)) / ((x + delta_x) - x)
    return m

def derivative(x):
    # Declare 'x' to SymPy
    x = symbols('x')
    # Now just use Python syntax to declare function
    f = x**2
    # Calculate the derivative of the function
    dx_f = diff(f)
    return dx_f


def square(x):
    return x**2


def main():
    x = int(input("Value of x: "))
    delta_x = float(input("Value of delta x: "))
    print(f"Derivative: {derivative_x(square,x,delta_x)}")
    print(f"Derivative (with sympy): {derivative(x)}")
    
if __name__ == "__main__":
    main()