def add_product(product1):
    products.append(product1)
    return products
def remove_product(product2):
    if product2 in products:
        products.remove(product2)
    return products
def check_product(product3):
    if product3 in products:
        return True
    else:
        return False
def display_products():
    return products
def total_products():
    return len(products)
def sort_products():
    return sorted(products)
def clear_products():
    return products.clear()
def exit_program():
    return "Exit"
products=list(map(str, input("Enter products: ").split()))
choice=int(input("1.Add product\n2.Remove product\n3.Check product\n4.Display products\n5.Total products\nEnter your choice: "))
if choice>=1:
    product1=input("Enter product to add: ")
    print("Products after adding:", add_product(product1))
elif choice==2:
    product2=input("Enter product to remove: ")
    print("Products after removing:", remove_product(product2))
elif choice==3:
    product3=input("Enter product to check: ")
    print("Is product available?", check_product(product3))
elif choice==4:
    print("All products:", display_products())
elif choice==5:
    print("Total number of products:", total_products())
elif choice==6:
    print("sort the items:",sort_products())
elif choice==7:
    print("Clear the list:", clear_products())
elif choice==8:
    print("Exit the program:", exit_program())
else:
    print("Invalid choice")