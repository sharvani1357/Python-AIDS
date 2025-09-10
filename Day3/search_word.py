def search_word(s,n):
    for i in range(len(s)):
        if s[i]==n:
            print(i)
s=input("enter a string:")
n=input("enter a word to search:")
search_word(s,n)