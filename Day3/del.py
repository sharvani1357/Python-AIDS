my_list =list(map(int, input("Enter elements: ").split()))
index=int(input("Enter index to delete: "))
for i in range(len(my_list)):
    if index<len(my_list):
        del my_list[index]
        print("List after deletion: ", my_list)
    
