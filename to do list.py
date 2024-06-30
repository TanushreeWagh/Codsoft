import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

TODO_FILE = 'todo_list.json'

def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TODO_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def refresh_tasks():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        status = "✓" if task['completed'] else "✗"
        task_listbox.insert(tk.END, f"[{status}] {task['task']}")

def add_task():
    task_description = simpledialog.askstring("Add Task", "Enter the task description:")
    if task_description:
        tasks.append({'task': task_description, 'completed': False})
        save_tasks(tasks)
        refresh_tasks()

def update_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        new_task_description = simpledialog.askstring("Update Task", "Enter the new task description:")
        if new_task_description:
            tasks[selected_task_index[0]]['task'] = new_task_description
            save_tasks(tasks)
            refresh_tasks()
    else:
        messagebox.showwarning("Warning", "Please select a task to update.")

def mark_task_completed():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        tasks[selected_task_index[0]]['completed'] = True
        save_tasks(tasks)
        refresh_tasks()
    else:
        messagebox.showwarning("Warning", "Please select a task to mark as completed.")

def delete_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        tasks.pop(selected_task_index[0])
        save_tasks(tasks)
        refresh_tasks()
    else:
        messagebox.showwarning("Warning", "Please select a task to delete.")

root = tk.Tk()
root.title("My To-Do List Application")

tasks = load_tasks()

task_listbox = tk.Listbox(root, width=70, height=30)
task_listbox.pack()

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(fill='x')

update_button = tk.Button(root, text="Update Task", command=update_task)
update_button.pack(fill='x')

mark_completed_button = tk.Button(root, text="Mark as Completed", command=mark_task_completed)
mark_completed_button.pack(fill='x')

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack(fill='x')

refresh_tasks()

root.mainloop()