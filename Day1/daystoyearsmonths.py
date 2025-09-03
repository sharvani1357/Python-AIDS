#func with args and no return type
def days_to_yearmonth(days):
    years=days//365
    months=(days%365)//30
    print("years=",years,"months=",months)
days=int(input("enter days"))
days_to_yearmonth(days)
    