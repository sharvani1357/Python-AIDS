def my_list(n):
    l=[]
    for i in range(n):
        ele=input("enter element:")
        l.append(ele)
    return l
n=int(input("enter a number:"))
print(my_list(n))