
import math

#To determine which type of calculation the user requires:
user_choice=input("""Choose either 'investment' or 'bond' from the menu below to proceed: 

investment   -to calculate the amount of interest you'll earn on interest.
bond         -to calculate the amount you'll have to pay on a home loan.

""")
#Make the input case-insensitive
type=user_choice.casefold()


# INVESTMENT CALCULATIONS:
if type == "investment":
    principal=float(input("Enter the deposit amount (R): "))
    rate=float(input("Enter the interest rate (%): "))
    term=int(input("Enter the number of years your plan to invest for: "))

# Check interest type (simple/compound) - calculation depending on choice
    interest=input("Would you like simple or compound interest? ")
    interest_=interest.casefold()

    if interest_ == "simple":
        total_interest=float(principal*(1+(rate/100)*term))
                
    if interest_ == "compound":
        total_interest = principal * math.pow(1+(rate/100),term)
 
# Round off value to diplay as currency
    total=round(total_interest,2)

# Display total interest result to user
    print("The total interest you will earn is R "+str(total)+".")




# BOND CALCULATION:
if type == "bond":
    price=float(input("Enter the present value of the house (R): "))
    rate=float(input("Enter the interest rate (%): "))
    monthly_rate = rate/(12*100)
    term =int(input("Enter the number of months over which the bond will be repaid: "))

# Calculate monthly repayments
    repay=(monthly_rate*price)/(1-((1+monthly_rate)**(-term)))

# Round off to display as currency
    repayment=round(repay,2)

#Display monthly bond payments
    print("You will have to pay R "+str(repayment)+" every month.")




# ERROR MESSAGE for invalid inputs (not "bond" or "investment")
elif type != "bond" and type != "investment":
    print("You have not made a valid selection. ")

