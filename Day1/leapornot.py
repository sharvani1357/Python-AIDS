def leapyear(a):
    if a%4==0 and (a%100!=0 or a%400==0):
        print("leap year")
    else:
        print("not leap year")
a=int(input("enter a year:"))
leapyear(a)