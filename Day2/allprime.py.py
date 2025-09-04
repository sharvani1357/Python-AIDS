def isprime(n):
    for i in range(1,n):
        for j in range(2,int(i**(1/2))+1):
            if i%j!=0:
                print(j,end="")
n=int(input("enter a number:"))
print(isprime(n))