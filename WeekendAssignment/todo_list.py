"""
 TODO:
 Functions:
    - Present user with menu 
       - take in input
    - add task
       - take additional input
       - actually add the task to the todo list
    - delete task
       - take additional input
    - show all tasks
"""
tasks = []
choice = input("Press 1 to add task.\nPress 2 to delete task.\nPress 3 to view all tasks.\nPress 'q' to quit. ")

if choice == 1:
    tasks_dict = add_task()
    tasks.append(tasks_dict)
    # put tasks_dict into tasks


elif choice == 2:
    delete_task()

elif choice == 3:
    view_tasks()
    
elif choice == "q":
    quit()



def add_task():
    title = input("Name of task: ")
    priority = input("Priority of task (high, medium, low): ")
    tasks_dict = {
        "title": title,
        "priority": priority
    }
    return tasks_dict


# show all tasks with index number of each task. input index to delete respective task

def delete_task():
    for i, val in enumerate(tasks):
        print( i, val)
         
    number = input("Enter number of task to delete: ")
    del tasks[number]

# allow user to view tasks with format : title - priority
def view_tasks(): 
    for index, task in enumerate(tasks): # {"title": "dishes", "priority": "high"}
        print(index, task["title"], task["priority"])



