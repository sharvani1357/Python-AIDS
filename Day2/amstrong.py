def amstrong(n):
    s=str(n)
    sum=0
    for i in s:
        sum+=int(i)**len(s)
    if sum==n:
        return "amstrong"
    else:
        return "not amstrong"
n=int(input("enter a number:"))
print(amstrong(n))