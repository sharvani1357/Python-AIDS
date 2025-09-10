def count_characters(s1):
    alphabets=0
    digits=0
    special_characters=0
    for i in s1:
        if i.isalpha():
            alphabets+=1
        elif i.isdigit():
            digits+=1
        else:
            special_characters+=1
    print("alphabets:",alphabets)
    print("digits:",digits)
    print("special characters:",special_characters)
s1=input("enter a string:")
count_characters(s1)