def print_pattern(n):
    for i in range(n):
        for j in range(n):
            if i==j:
                print("$",end=" ")
            else:
                print("*",end=" ")
        print()
n=int(input("enter a number:"))
print_pattern(n)