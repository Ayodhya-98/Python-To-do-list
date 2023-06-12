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
    
   for item in todo_list:
       task_number=1
       task_name=item[0]
       task_status=item[1]
       print(f"{task_number} | {task_name} | {task_status}")
       task_number+=1

def add_item(task):
    todo_list.append(task)
    
def change_task_status(task_number,task_status):
    task=todo_list[task_number-1]
    completed_task=(task[0],task_status)
    todo_list[task_number-1]=completed_task
    
  

while True:
    display_menu()
    choice=int(input("Please enter your choice :"))
    if choice==1:
        display_list()
    elif choice==2:
        item_name=input("Enter the Task name :")
        is_complete=False
        task=(item_name, is_complete)
        add_item(task)
    elif choice==3:
        task_number=int(input("Enter the Task number to complete :"))
        change_task_status(task_number,True)
    elif choice==4:
        task_number=int(input("Enter the Task number to incomplete :"))
        change_task_status(task_number,False)
              
  
  
    
    
    
    
    