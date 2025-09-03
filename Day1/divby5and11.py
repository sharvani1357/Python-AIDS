def divisible(a):
    if a%5==0 and a%11==0:
        print("Divisible by both 5 and 11")
    else:
        print("Not divisble")
a=int(input("enter a number:"))
divisible(a)