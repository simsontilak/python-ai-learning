from math import exp

def calculate_amount_cont(loan_amount, yearly_rate, number_of_years):
    interest = yearly_rate / 100
    total_amount = loan_amount * exp(interest * number_of_years)
    return total_amount


def calculate_amount(loan_amount, yearly_rate, number_of_times, number_of_years):
    interest = yearly_rate / 100
    interest_per_period = interest / number_of_times
    period = number_of_times * number_of_years
    one_time_multiplier = 1 + interest_per_period
    compound_multiplier = one_time_multiplier ** period
    total_amount = loan_amount * compound_multiplier
    return total_amount

def main():
    loan_amount = float(input("Enter loan amount: "))
    yearly_rate = float(input("Interest percent rate per year: "))
    number_of_times = int(input("How many times a year interest is calculated: "))
    number_of_years = int(input("No of years: "))
    total_amount = calculate_amount(loan_amount, yearly_rate, number_of_times, number_of_years)
    total_amount_continuous = calculate_amount_cont(loan_amount, yearly_rate, number_of_years)
    
    print(f"Amount after {number_of_years} years is ${round(total_amount,6)}")
    print(f"Amount after {number_of_years} years after continuous compounding is ${round(total_amount_continuous,6)}")
    

if __name__ == "__main__":
    main()
