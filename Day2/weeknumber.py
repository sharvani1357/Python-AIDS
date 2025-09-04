def weeknumber(no):
    if no==1:
        return "Sunday"
    elif no==2:
        return "Monday"
    elif no==3:
        return "Tuesday"
    elif no==4:
        return "Wednesday"
    elif no==5:
        return "Thursday"
    elif no==6:
        return "Friday"
    elif no==7:
        return "Saturday"
    else:
        return "Invalid"
no=int(input("enter the number"))
print(weeknumber(no))