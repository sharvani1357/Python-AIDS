def string_length(s):
    count=0
    for i in s:
        count+=1
    return count
def string_compare(s1,s2):
    if s1==s2:
        return True
    else:
        return False
def string_concat(s1,s2):
    return s1+s2
s=input("enter a string:")
print("length is:",string_length(s))
s1=input("enter first string:")
s2=input("enter second string:")
print("are they equal?",string_compare(s1,s2))
print("concatenated string is:",string_concat(s1,s2))
