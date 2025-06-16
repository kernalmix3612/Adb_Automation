from datetime import *
from sched import scheduler
from tkinter import messagebox
###import pandas as pd
##from pandas import *
import tkinter as tk
import time
##import schedule
from pathlib import Path

def display_menu():
    print("\n1. Add a task")
    print("2. View all tasks")
    print("3. Mark a task as complete")
    print("4. Delete a task")
    print("5. Exit\n")

def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append({"task": task, "complete": False})

def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        for idx, task in enumerate(tasks, 1):
            status = "Complete" if task["complete"] else "Incomplete"
            print(f"{idx}. {task['task']} [{status}]")

def mark_task_complete(tasks):
    task_num = int(input("Enter the task number to mark as complete: "))
    if 0 < task_num <= len(tasks):
        tasks[task_num - 1]["complete"] = True
        print("Task marked as complete.")
    else:
        print("Invalid task number.")

def delete_task(tasks):
    task_num = int(input("Enter the task number to delete: "))
    if 0 < task_num <= len(tasks):
        tasks.pop(task_num - 1)
        print("Task deleted.")
    else:
        print("Invalid task number.")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Choose an option: ")
        
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_task_complete(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()



##def write_reminder():
    #Remind title
    #Remind Details
    #Remind Date
    #Remind time
    #Remid type
    #return

##def read_task(): #This function uses the pandas library to read our tasks from a CSV file. The parse_dates parameter ensures that our date and time columns are interpreted correctly.
    script_dir = Path(__file__).parent # Get the directory of the script
    csv_file = script_dir / 'Data' / 'task.csv' # Build the relative path to the CSV file
    df = pd.read_csv(csv_file, parse_dates=[['date','time']]) # Read the CSV file using pandas
    #return df

##def show_alert(task): #To display pop-up alert by tkinter
    root = tk.Tk() # Initialize Tkinter
    root.withdraw() # Only show window if we need it
    response =  messagebox.askyesno("Task alert:", f"Do you want to work on the task \"{task['name']}\" now?")
    if response:
        pass
    root.destroy()

##def execute_tasks():
##    tasks = read_task()
##    tasks = tasks.sort_values(by="date_time")
##    now = datetime.now()
##    for index, task in tasks.iterrows():
##        task_time = task['date_time'].to_pydatetime()
##        print("Task time:",task_time)
##        if now < task_time:
##            second_until_tasks = (task_time-now).total_seconds()
##            print("Waiting for task time:",second_until_tasks," seconds")
##            time.sleep(second_until_tasks)
##        print("Execute Task!")
##        show_alert(task)
##        print("Take executed!")

##def main():
    schedule.every().day.at("14:59:00").do(execute_tasks)
    #read_task()
    while True:
        schedule.run_pending()
        time.sleep(1)
##if __name__ == "__main__":
    main()