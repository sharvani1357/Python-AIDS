def sumofdigits(n):
    sum=0
    for i in str(n):
        sum=sum+int(i)
    return sum
n=int(input("enter a number:"))
print(sumofdigits(n))