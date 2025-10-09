# finance_calculator.py

def main():
  try:
    monthly_income = float(input("Enter your monthly income: "))
    monthly_expenses = float(input("Enter your total monthly expenses: "))
  except ValueError:
    print("Please enter valid numbers for income and expenses.")
    return

  monthly_savings = monthly_income - monthly_expenses
  annual_savings = monthly_savings * 12
  interest_rate = 0.05
  projected_savings = annual_savings + (annual_savings * interest_rate)

  print(f"Your monthly savings are ${monthly_savings:.2f}.")
  print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}.")

if __name__ == "__main__":
  main()