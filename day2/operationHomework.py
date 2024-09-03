# Problem

# You went out with 3 of your friends for lunch. Total bill came 125.86
# create a code that will resolve the payment based on these:
#     1- What is your total bill?
#     2- How much tip will you like to give in %? 5, 10 or 15
#     3- How many people to split the bill with? 
#     4- Each person will pay:
# NB: All value should take only 2 numbers after the decimal portion

# Solution

total_bill = float(input("What is your total bill? $"))
tip_value = int(input("How much tip will you like to give in %? 5, 10 or 15 "))
number_of_payers = int(input("How many people to split the bill with? "))

# calculate final bill
final_bill = total_bill + total_bill * tip_value / 100

# calculate each person bill
each_person_bill = final_bill / number_of_payers

final_bill_per_person = round(each_person_bill, 2)

print(f"Each person should pay: ${final_bill_per_person}")