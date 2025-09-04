def sumofnatural(n):
    sum=0
    for i in range(1,n+1):
        sum=sum+i
    return sum
n=int(input("enter a number:"))
print(sumofnatural(n))