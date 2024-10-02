#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator!")
people = input("How many people on the bill?\n")
bill = input("How much is the bill?\n")
tip = input("How much would you like to tip, 10%, 12%, or 15%?\n")
tip_percent = int(tip) / 100
total_tip = float(bill) * float(tip_percent)
total_bill = float(bill) + float(total_tip)
split_bill = (float(total_bill) / float(people))
print(f"Each person should pay ${split_bill:.2f}")