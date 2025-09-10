def tech_workshop(l1,l2,l3):
    s1=set(l1)
    s2=set(l2)
    s3=set(l3)
    for i in s1:
        i=i.lower()
    for i in s2:
        i=i.lower()
    for i in s3:
        i=i.lower()
    print("Day1 without duplicates",s1)
    print("Day2 without duplicates",s2)
    print("Day3 without duplicates",s3)
    total=s1|s2|s3
    print("Total no of attendees",len(total))
    threedays=s1&s2&s3
    print("Three days attendees",threedays)
    oneday=(s1-(s2|s3))|(s2-(s3|s1))|(s3-(s1|s2))
    print("Exactly one day",oneday)
    overlap=(s1&s2)|(s2&s3)|(s3&s1)
    print("Overlap",overlap)
    sort=sorted(s1|s2|s3)
    l=list(sort)
    print("Sorted order of attendees",l)
    count=len(sort)
    print("Total count of sorted list",count)
l1=["Shivani","Sharvani","khushi"]
l2=["sharanya","Varshitha","Shivani"]
l3=["khushi","Shivani","sharanya"]
tech_workshop(l1,l2,l3)
    