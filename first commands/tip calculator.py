print("Welcome to the tip calculator")
bill = float(input("What was the total bill? "))
percentage = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
tip = bill * (percentage / 100)
total_bill = bill + tip
split = float(input("How many people to split the bill? "))
each_pay = total_bill / split
final_amount = round(each_pay, 2)
final_amount = "{:.2f}".format(each_pay)
print(f"Each person should pay: {final_amount}")
