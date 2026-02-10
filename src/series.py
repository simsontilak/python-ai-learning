from functools import reduce
from sympy import *

def multi(a, b):
    return a * b

def factorial(end_range):
    return reduce(multi, range(1, end_range+1))

def calc_sum(multiplier,end_range):
    return sum(i * multiplier for i in range(1,end_range+1))

def calc_sum_lazy(multiplier, end_range):
    i, n = symbols('i n')
    summation = Sum(multiplier * i,(i, 1, n))
    work = summation.subs(n, end_range)
    return work.doit()

def main():
    print(f"Sum = {calc_sum(1,6)}")
    print(f"Sum = {calc_sum_lazy(1,6)}")
    print(f"Factorial = {factorial(5)}")

if __name__ == "__main__":
    main()