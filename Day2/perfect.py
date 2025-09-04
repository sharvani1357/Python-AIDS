def perfectnumber(n):
    sum=0
    for i in range(1,n):
        if n%i==0:
            print(i)
            sum=sum+i
            print("sum=",sum)
            if sum==n:
                print("Perfect number")
n=int(input("enter a number:"))
perfectnumber(n)

