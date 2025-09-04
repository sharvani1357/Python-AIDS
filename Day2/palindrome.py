def palindrome(n):
    s=str(n)
    rev=s[::-1]
    if s==rev:
        return "Palindrome"
    else:
        return "Not Palindrome"
n=int(input("enter a number:"))
print(palindrome(n))