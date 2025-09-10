def word_counnt(s):
    count=0
    for i in s:
        if i==" " or i=="\n":
            count+=1
    return count+1
s=input("enter a string:")
print("number of words:",word_counnt(s))