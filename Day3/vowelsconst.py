def vowelsconst(s):
    v=0
    c=0
    for i in s:
        if i in 'aeiouAEIOU':
            v+=1
        else:
            c+=1
    print("vowels:",v)
    print("consonants:",c)
s=input("enter a string:")
vowelsconst(s)