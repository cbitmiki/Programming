annual_salary = float(input("Starting annual salary: "))
monthly_salary = annual_salary / 12

portion_saved_percentage = float(input("Enter the percent of your salary to save, as a decimal: "))
portion_saved = portion_saved_percentage * monthly_salary

total_cost = float(input("Enter the cost of your dream home: "))
portion_down_payment = total_cost * 0.25

current_savings = float(0)
num_of_months = 0
monthly_interest = float(0.04/12)

while current_savings < portion_down_payment:
    current_savings = (current_savings + portion_saved) + (current_savings * monthly_interest)
    num_of_months = num_of_months + 1

print("Number of months: ", num_of_months)


