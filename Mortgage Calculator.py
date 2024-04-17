def mortgage_calculator():
    principal = float(input("How big of a loan do you need? "))
    interest_rate = 0.05 / 12
    term = float(input("Would you like a 15 year, 20 year, or 30 year term? "))
    number_of_payments = term * 12

    monthly_payment = principal * ((interest_rate * ((1 + interest_rate)**number_of_payments)) / (((1 + interest_rate) ** number_of_payments) - 1))
    final_monthly_payment = round(monthly_payment, 2)
    print(final_monthly_payment)

mortgage_calculator()

