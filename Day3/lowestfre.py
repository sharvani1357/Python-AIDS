def count_occurance(s):
    f={}
    for i in s:
        if i in f:
            f[i]+=1
        else:
            f[i]=1
    return f
s=input("enter a string:")
d=count_occurance(s)
print("frequency of each character:",d)
print("lowest=",min(d,key=d.get))
