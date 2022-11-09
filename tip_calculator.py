'''
write a code that allows you to convert tips
the code must be interactive and take user input at the  command line
after tip has been calculated, the program should ask the user if they would like to enter another tip, and run again if the answer is yes
code should be split into functions
logically broken up
well named
'''

# ask user what the total of the bill is
def user_input():
    print("Welcome to my tip calculator.")
    try:
        original_bill = float(input("What is the total? $"))

    # ask number of people splitting the bill
        people_splitting = int(input("People splitting the bill?"))

    # percentage of the tip given
        tip = float(input("What percentage tip would you like to give?"))
        tip_percentage = round(original_bill * (.01 * tip), 2)
    except ValueError:
        print("Please enter a valid number.")
        return user_input()

        #calculating tax amount at 10%
    tax_amount = original_bill * 0.10
    return tip_calculator(original_bill, people_splitting, tip_percentage, tax_amount)

def do_over():
    repeat = input("Would you like to rerun the calculator? Please enter y / n.")
    try:
        if repeat == "n": 
            print("Thank you for using my tip calculator!")
            
        elif repeat == "y":
            user_input()  
        else:
            raise Exception 
    except Exception:
        print("Your entry is invalid. Let's try again.")
        do_over()

def tip_calculator(original_bill, people_splitting, tip_percentage, tax_amount):
    total_bill = round(original_bill + tax_amount + tip_percentage, 2)
    print(f'Your total bill is $ {total_bill}.')
    split_bill = round((total_bill / people_splitting), 2)
    print(f"Your bill total per person is $ {split_bill}.")
    do_over()

user_input()