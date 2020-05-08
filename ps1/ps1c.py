#This program finds the best rate of savings to achieve a down payment (+- $100) on a $1M house in 36 months

#Down payment fraction is 25%, semi-annual salary raise is 7% and the annual rate of return on savings is 4%

#Other required info: cost of house, raise, return, down payment, current savings
semi_annual_raise=0.07
r=0.04
portion_down_payment=0.25
total_cost=1000000
down_payment=total_cost*portion_down_payment#250,000
current_savings=0


#Helper function that calculates how much is saved in 36 months given salary, savings rate, and semi annual raise
def save36m(guess,salary,sar):
    savings=0
    months=0
    while months<36:
        if months%6==0 and months!=0:
            salary=salary*(1+sar)
        savings=savings+(salary/12)*(guess/10000)+savings*semi_annual_raise/12
        months+=1
    return savings

#The actual function that calculates the best savings rate as a decimal fraction of monthly salary
def find_savings_rate(salary):
    if save36m(10000, starting_salary, semi_annual_raise)<down_payment:
        print("It is not possible to pay the down payment in three years")
    else:
        low=0
        high=10000
        guess=(high+low)/2.0
        num_guesses=0
        epsilon=100
        while abs(save36m(guess, starting_salary, semi_annual_raise)-down_payment)>epsilon:
            if save36m(guess,starting_salary,semi_annual_raise)>down_payment:
                high=guess
            else:
                low=guess
            guess=(high+low)/2.0
            num_guesses+=1
        print("Best savings rate:", str(guess/10000))
        print("Steps in bisection search:", str(num_guesses))

#INPUT from the user
starting_salary=float(input("Enter your starting annual salary:"))

#Find the best savings rate for a starting salary that the user enters
find_savings_rate(starting_salary)




