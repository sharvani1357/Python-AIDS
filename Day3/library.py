def add(dict,id,title):
    dict[id]=title
    print(dict)
def remove(dict,id):
    del dict[id]
    print(dict)
def search(dict,id):
    if id in dict:
        print(dict[id])
    else:
        print("Not Found")
def update(dict,id,title):
    dict[id]=title
    print(dict)
def display(dict):
    print(dict)
def count(dict):
    print(len(dict))
dict={1:"Web technologies",2:"computer networks",3:"python",4:"Java"}
print("Enter Choice:")
print("1.Add a book\n2.Remove a book\n3.Search for a book\n4.Update the title\n5.Display all books\n6.Count no of books")
choice=int(input())
if choice==1:
    idtoadd=int(input("Enter id"))
    titletoadd=input("Enter title")
    add(dict,idtoadd,titletoadd)
elif choice==2:
    idtodelete=int(input("Enter id to delete"))
    remove(dict,idtodelete)
elif choice==3:
    idtosearch=int(input("Enter id to search"))
    search(dict,idtosearch)
elif choice==4:
    idtoupdate=int(input("Enter id to update"))
    titletoupdate=input("Enter title to update")
    update(dict,idtoupdate,titletoupdate)
elif choice==5:
    display(dict)
elif choice==6:
    count(dict)
else:
    print("Invalid choice")

