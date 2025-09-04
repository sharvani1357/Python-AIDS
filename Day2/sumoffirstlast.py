def sumoffirstlast(n):
    s=str(n)
    return int(s[0])+int(s[-1])
n=int(input("enter a number:"))
print(sumoffirstlast(n))
