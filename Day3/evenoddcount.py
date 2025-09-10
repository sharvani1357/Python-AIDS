def even_odd(n):
    even=0
    odd=0
    for i in range(len(n)):
        if n[i]%2==0:
            even+=1
        else:
            odd+=1
    return even,odd
n=list(map(int,input("enter elements:").split()))
print(even_odd(n))