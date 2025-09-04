def print_pattern(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i==j or i+j==n+1:
                print("$",end=" ")
            else:
                print("*",end=" ")
        print(end="\n")
n=int(input("enter a number:"))
print_pattern(n)