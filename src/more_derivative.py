from sympy import *

def derivative(at_var):
    # "x" and step size "s"
    x, s = symbols('x s')
    
    # declare function
    f = x ** 2
    
    # slope between two points with gap "s"
    # substitute into rise-over-run formula
    slope_f = (f.subs(x, x + s) - f) / ((x+s) - x)
    
    # substitute 2 for x
    slope_2 = slope_f.subs(x, at_var)
    
    # calculate slope at x = 2
    # infinitely approach step size _s_ to 0
    result = limit(slope_2, s, 0)
    
    return (slope_2, result)

def var_derivative():
    # "x" and step size "s"
    x, s = symbols('x s')
    # declare function
    f = x**2
    # slope between two points with gap "s"
    # substitute into rise-over-run formula
    slope_f = (f.subs(x, x + s) - f) / ((x+s) - x)
    # calculate derivative function
    # infinitely approach step size +s+ to 0
    result = limit(slope_f, s, 0)
    return (f, result)

def main():
    x = int(input("Value of x: "))
    
    (slope_f, result) = derivative(x)
    
    print(f"Derivative slope function = {slope_f} and derivative =  {result}")

    (f, result) = var_derivative()
    
    print(f"Derivative of {f} is {result}")
    
if __name__ == "__main__":
    main()