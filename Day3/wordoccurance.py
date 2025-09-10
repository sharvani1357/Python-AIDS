def word_occurence(s):
    f={}
    for i in s:
        if i in f:
            f[i]+=1
        else:
            f[i]=1
    return f
s=input("enter a string:")
print(word_occurence(s))