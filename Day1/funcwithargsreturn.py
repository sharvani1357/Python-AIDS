def kilo_to_miles(kilo):
    miles=kilo*0.621
    return miles
kilo=float(input("Enter distance in kilometers: "))
z=kilo_to_miles(kilo)
print(f"Miles={z}")