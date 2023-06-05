todo_list=[]

def display_menu():
    print("Simple Todo list")
    print("1- Display The TODO list")
    print("2- Add items to TODO list")
    print("3- Mark item as complete")
    print("4- Mark item as incomplete")
    print("5- Delete item")
    print("6- Exit the Programme")
    
def display_list():
   pass
    
    
  

while True:
    display_menu()
    choice=int(input("Please enter your choice :"))
    if choice==1:
        display_list()
    elif choice==2:
        item_name=input("Enter the Tsk name :")
        task=(item_name,)      
  
    
    
    
    
    