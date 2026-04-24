# to do  list
d={ 
# add task, delete task, view task, update task, exit
"1" : "Add the task",
"2" :  "Delete the task",
"3" : "View the task",
"4" : "Update the task",
"5" : "Mark the task as completed",
"6" :  "Exit",
}
#global store
store = []
# display menu
def display_menu():
    print("To Do List Menu:")
    for key, value in d.items():
        print(f"{key}. {value}")
# taking input from the user
def choice():
    # global variable store
    global store
    user=input("Enter the number of the task you want to perform: ")
    print(user)
    #print(d[user])
    # conditional statement for add task
    if user == "1":
        print("You have selected to add the task")
        inpuut=input("Add your task: ")
        store.append(inpuut)
        print("Task added successfully")
        print("Your task is: ", store)
        # for deleting the task
    elif user=="2":
        print("You have selected to delete the task")
        print("Your task is: ", store)
        # taking input from the user to delete the task
        #num_del = int(input("Enter the number of the task you want to delete: "))
        num_del = input("Enter the number of the task you want to delete: ")
       
        delete_task = input("Are you sure you want to delete the task? (yes/no): ")
        #if delete_task == "yes":
        if delete_task.lower() in ["YES","yes"]:
            # deleting the task from the store
            # here using remove method because it will remove by the value and not by the index
            store.remove(num_del)
            # here using pop method because it will remove by the index
            #store.pop(num_del - 1)
            print("Task deleted successfully")
        else:
            print("Task not deleted")
            # for viewing the task
    elif user=="3":
        print("You have selected to view the task")
        # it will print the task in the store but number will not be printed
        """for task in store:
            print( task)
        print("Your task is: ", store)
    """
        # it will print the task in the store with number
        for index, task in enumerate(store, start=1):
            print(f"{index}. {task}")
        # print("Your task is: ", store)
        # for updating the task
    elif user=="4":
        print("You have selected to update the task")
        print("Your task is: ", store)
        # taking input from the user to update the task
        old_task = input("\nEnter the task you want to update: ")
        if old_task in store:
            new_task = input("Enter new task: ")
            index = store.index(old_task)
            store[index] = new_task
            print("Task updated successfully")
        else:
            print("Task not found")
        print("Updated tasks:")
        for task in store:
            print(task)
        # the code for updating task using value
        """num_update =int(input("Enter the task you want to update: "))
        update_task = input("Enter the updated task: ")
        store[num_update-1] = update_task"""
        # updating the task in the store
        print("Updated task is: ", store)
       
        # marking the task as completed
    elif user =="5":
        print("You have selected to mark the task as completed")
        print("Your task is: ", store)
        # taking input from the user to mark the task as completed
        num_completed=int(input("Enter the number of task you want to mark as completed: "))
        # marking the task as completed in the store
        store[num_completed-1] = store[num_completed-1] + "- Completed"
        print("\nTask marked as completed successfully", store[num_completed-1])
    else:
        print("You selected an invalid option. Please try again.")

while True:
    user_input = input("Do you want to continue? (yes/no): ")
    if user_input.lower() in ["YES","yes", "Y", "y"]:
        # calling the function
        display_menu()
        choice()
        # returning to the menu after performing the task
        continue
    else:
        break