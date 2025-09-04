def counting(n):
    count=0
    for i in str(n):
        count=count+1
    return count
n=int(input("enter a number:"))
print(counting(n))