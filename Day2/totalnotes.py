def total_notes(n):
    if n>2000:
        twoth=n//2000
        print("2000 ->",twoth)
        n-=2000
    if n>=500:
        fivth=n//500
        print("500 ->",fivth)
        n-=500
    if n>=200:
        twohn=n//200
        print("200 ->",twohn)
        n-=200
    if n>=100:
        hnd=n//100
        print("100 ->",hnd)
        n-=100
    if n>=50:
        fift=n//50
        print("50 ->",fift)
        n-=50
    if n>=20:
        twenty=n//20
        print("20 ->",twenty)
        n-=20
    if n>=10:
        ten=n//10
        print("10 ->",ten)
        n-=10
    if n>=2:
        two=n//2
        print("2 ->",two)
        n-=2
    else:
        one=n//1
        print("1 ->",one)
        n-=1
n=int(input("Enter the amount: "))
print(total_notes(n))