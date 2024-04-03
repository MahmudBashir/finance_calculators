import math

# This is a finance calculator programme using while loop and if-elif-else statement
# This programme allows users to access investment and home loan repayment (bond) calculator
# Ask user to select either investment or bond
# Make sure user's input is not case sensitive
# If 'investment' is selected, ask user to enter either simple or compound interest
# Display recommendation based on selection
# Incase user type invalid input please show appropriate error message


while True:
    
    print("""investment - to calculate the amount of interest you'll earn on your investment
    bond - to calculate the amount you'll have to pay on a home loan""")

    invest_bond = input("Please enter either investment or bond from the above to proceed: ").lower()
    
    if invest_bond == "investment":
        print("Thank you for selecting investment")
        amount = float(input("Please enter the amount of money to invest: "))
        time_period = int(input("Enter the number of years to invest: "))
        interest_rate = float(input("Enter interest rate in number only, please do not add '%': "))/100  # Interest rate is calculated by divided by 100 
        interest_option = input("Enter either simple or compound inerest: ")
        r = interest_rate
        P = amount
        t = time_period
            
        if interest_option == "simple":
            A = P * (1 + r*t)  # 'simple' interest formula, 'A' is the total amount once interest has been applied
            print("The amount you will get back is: $", A)
                      
        elif interest_option == "compound":
            A = P * math.pow((1 + r), t)  # 'compound' interest formula
            print("The amount you will get back is: $", A)
        break
            
    elif invest_bond == "bond":
        print("Thank you for selecting bond")
        value = float(input("Please enter the value of the house: "))
        interest_rate = float(input("Enter interest rate in number only, please do not add '%': "))/100  # Interest rate is calculated by divided by 100              
        time_period = int(input("Enter the number of months to repay the bond: "))
        P = value 
        i = interest_rate/12  # Monthly interest rate
        n = time_period
        repayment = (i * P)/(1 - (1+ i)**(-n))  # 'bond' repayment formula
        print("Your monthly repayment is: $", repayment)
        break
            
    else:
        print("Please enter only bond or investment to proceed")
        
    
    
   

        