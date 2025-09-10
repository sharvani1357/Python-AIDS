def set_print(n):
    s=set()
    for i in range(n):
        ele=input("enter element:")
        s.add(ele)
    return s
n=int(input("enter no.of elements:"))
print(set_print(n))
