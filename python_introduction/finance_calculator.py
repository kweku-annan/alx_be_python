monthly_income = input("Enter your monthly income: ")
monthly_expenses = input("Enter your total monthly expenses: ")
monthly_savings =int(monthly_income) - int(monthly_expenses)

rate = 0.05
savings_projection = monthly_savings * 12 + (monthly_savings * 12 * rate)
print(f"Your monthly_savings are ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${savings_projection}")

