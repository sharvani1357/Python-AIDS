def print_factors(n):
    for i in range(1,n):
        if n%i==0:
            print(i)
n=int(input("enter a number:"))
print_factors(n)
