def palindrome(n):
    for i in range(1,n+1):
        s=str(i)
        rev=s[::-1]
        if s==rev:
            print(i)
n=int(input("enter a number:"))
palindrome(n)