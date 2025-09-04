def chardigspcl(n):
    if n.isalpha():
        return "Character"
    elif n.isdigit():
        return "Digits"
    else:
        return "Special characters"
n=input("enter the value")
print(chardigspcl(n))