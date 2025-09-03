principle_amount=int(input("enter principle amount"))
Total_months=int(input("enter total months"))
Rate_of_interest=int(input("enter rate of interest"))
Simple_Interest=(principle_amount*Total_months*Rate_of_interest)/100
#SimpleInterest
print(f"simple interest={Simple_Interest:.2f}")
#Total amount Hands on
Total_hand=principle_amount+Simple_Interest
print(f"total amount in hand={Total_hand:.2f}")