def totalbill(tu):
    if tu<=50:
        return tu*3.80
    elif tu>50 and tu<=100:
        return (50*3.80)+(tu-50)*4.20
    elif tu>100 and tu<=200:
        return (50*3.80)+(50*4.20)+(tu-100)*5.10
    elif tu>200 and tu<=300:
        return (50*3.80)+(50*4.20)+(100*5.10)+(tu-200)*6.30
    else:
        return (50*3.80)+(50*4.20)+(100*5.10)+(200*6.30)+(tu-300)*7.50
present_month=int(input("Present Month Reading="))
last_month=int(input("Last Month Reading="))
tu=present_month-last_month
print(totalbill(tu))