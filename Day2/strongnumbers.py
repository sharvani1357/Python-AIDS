def factorial(n):
    s=str(n)
    sum=0
    f=1
    for i in s:
        i=int(i)
        f=f*i
        sum=sum+f
    return sum
n=int(input("enter a number:"))
print(factorial(n))