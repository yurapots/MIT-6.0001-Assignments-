#This program calculates the number of months
#a person would have to save money to make a down payment for a house

#Down payment fraction is 25% and the annual rate of return on savings is 4%

annual_salary=float(input("Enter your annual salary:"))
portion_saved=float(input("Enter the percent of your salary to save, as a decimal:"))
total_cost=float(input("Enter the cost of your dream home:"))

portion_down_payment=0.25#portion of total cost of house to be paid as down payment
down_payment=portion_down_payment*total_cost

r=0.04#annual return on savings
current_savings=0

months_counter=0
while current_savings<down_payment:
    current_savings=current_savings+(annual_salary/12)*portion_saved+current_savings*r/12
    months_counter=months_counter+1

print("Number of months to save for down payment:",months_counter)
