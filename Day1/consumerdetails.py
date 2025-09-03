#CONSUMER DETAILS
cno=int(input("Consumer Number="))
cname=input("Consumer Name=")
present_month=int(input("Present Month Reading="))
last_month=int(input("Last Month Reading="))
total_units=present_month-last_month
current_bill=total_units*3.80
print("CONSUMER DETAILS:")
print(f"Consumer Number:{cno}\nConsumer Name:{cname}\nPresent Month Reading:{present_month}\nLast Month Reading:{last_month}\nTotal Units Consumed:{total_units}\nCurrent Bill:{current_bill:.2f}")

