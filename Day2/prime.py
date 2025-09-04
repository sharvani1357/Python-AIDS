def isprime(n):
    for i in range(2,int(n**(1/2))+1):
        if n%i==0:
            return "Not Prime"
        else:
            return "Prime"
n=int(input("enter a number:"))
print(isprime(n))