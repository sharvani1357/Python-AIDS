n=list(map(int,input("enter elements:").split()))
n.sort()
for i in range(len(n)):
    max=n[-1]
    if n[i]>max:
        max=n[i]
    elif n[i]<max:
        secmax=n[i]
print("second max is:",secmax)