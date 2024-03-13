def calc_savings_needed():
    real_annual_salary = float(input("Starting annual salary: " ))
    monthly_salary = real_annual_salary / 12

    months = 36
    home_total_cost = 1000000
    epsilon = 100
    portion_down_payment = home_total_cost * .25
    semi_annual_raise = .07
    current_savings = 0
    num_of_guesses = 0
    monthly_interest = .04/12
    high = 1.0
    low = 0.0
    guess_rate = (high + low) / 2.0
    is_impossibble = False # if guess_rate == 1.0, then is_impossible = true 

    

    while abs(current_savings - portion_down_payment) >= epsilon:
        if (guess_rate > .9):
            is_impossibble = True
            break

        annual_salary = real_annual_salary
        monthly_salary = annual_salary / 12
        month = 0
        current_savings = 0

        while (month < months):  
            current_savings += current_savings * monthly_interest + (guess_rate * monthly_salary)
            month += 1

            if month % 6 == 0 and month > 0:
                annual_salary += annual_salary * semi_annual_raise
                monthly_salary = annual_salary / 12

        if abs(current_savings - portion_down_payment) >= epsilon:
            if current_savings < portion_down_payment:
                low = guess_rate
            else:
                high = guess_rate
            num_of_guesses += 1    
            guess_rate = (high + low) / 2

    if is_impossibble:
        print("It is not possible to pay down payment in the given timeframe.")
    else:
        print("Best savings rate:", guess_rate)
        print("Steps in bisection search:", num_of_guesses)


calc_savings_needed()

