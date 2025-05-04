from typing import final

print("Welcome to tip Calculator")
bill = float(input("what was the total bill"))
tip = int(input("how much tip would like to give"))
split = int(input("How much people to split the bill"))
tip_percent = tip / 100
total_Tip_Amount = bill * tip_percent
total_Bill = bill + total_Tip_Amount
bill_Personel = total_Bill / split
final_Bill = round(bill_Personel , 2)
print(f"Each person should pay: ${final_Bill}")