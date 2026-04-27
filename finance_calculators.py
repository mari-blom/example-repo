import math

# Introduction to remind user how to choose correctly regarding their needs
print("Investment - to calculate the amount of interest you'll earn on your investment.")
print("Bond - to calculate the amount you'll have to pay on a home loan.")

# Prompt user to choose to calculate interest of their "investment" of "bond".
investment_or_bond = input(
    "Enter either “investment” or “bond” from the menu above to proceed: ")
# If user entered "investment"
# Ask questions to get info needed to calculate interest.
if investment_or_bond.lower().strip() == "investment":
    print("Investment")
    amount_deposit = int(input("Enter the amount of money you will deposit:R"))
    interest_rate = int(input(
        "Enter the rate of interest (only the number): "))/100
    number_of_years = int(input(
        "Enter the number of years you will invest the money: "))
    simple_or_compound = (input("Enter 'simple' or 'compound' interest: "))
    # Indented if-statement to calculate "simple" or "compound" interest.
    if simple_or_compound == "simple":
        simple_interest_investment = amount_deposit * (1 + interest_rate
                                                       * number_of_years)
        print("The amount you will receive from simple interest: R",
              simple_interest_investment)
    else:
        compound_interest = amount_deposit * math.pow((1 + interest_rate),
                                                      number_of_years)
        print("The amount you will receive from compound interest: R",
              compound_interest)

# If user entered "bond"
# Ask questions to get info needed to calculate monthly repayment on bond.
elif investment_or_bond.lower().strip() == "bond":
    print("Bond")
    present_value = int(input("Enter the present value of the house:R"))
    interest_rate = int(input("Enter the interest rate: "))/100/12
    months_to_pay = int(input(
        "Enter the number of months you plan to repay the bond: "))
    repayment = (
        interest_rate * present_value)/(1-(
            1 + interest_rate)**(-months_to_pay))
    print("The amount to repay on your bond each month will be:R", repayment)

# If user does not enter a valid input, show an error message.
else:
    print("An error has occurred. Please try again.")
