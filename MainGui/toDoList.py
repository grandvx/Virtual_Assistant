import tkinter as tk
from tkinter import messagebox

class TodoListManager:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List")

        self.create_widgets()

        # Load tasks when the program starts
        self.load_tasks()

        # Save tasks when the program exits
        self.master.protocol("WM_DELETE_WINDOW", self.save_tasks)

    def create_widgets(self):
        self.frame_tasks = tk.Frame(self.master)
        self.frame_tasks.pack()

        self.listbox_tasks = tk.Listbox(self.frame_tasks, height=10, width=50)
        self.listbox_tasks.pack(side=tk.LEFT)

        self.scrollbar_tasks = tk.Scrollbar(self.frame_tasks)
        self.scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

        self.listbox_tasks.config(yscrollcommand=self.scrollbar_tasks.set)
        self.scrollbar_tasks.config(command=self.listbox_tasks.yview)

        self.entry_task = tk.Entry(self.master, width=50)
        self.entry_task.pack()

        self.button_add_task = tk.Button(self.master, text="Add Task", width=48, command=self.add_task)
        self.button_add_task.pack()

        self.button_delete_task = tk.Button(self.master, text="Delete Task", width=48, command=self.delete_task)
        self.button_delete_task.pack()

        self.button_mark_done = tk.Button(self.master, text="Mark as Done", width=48, command=self.mark_done)
        self.button_mark_done.pack()

    def add_task(self):
        task = self.entry_task.get()
        if task:
            self.listbox_tasks.insert(tk.END, task)
            self.entry_task.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def delete_task(self):
        try:
            index = self.listbox_tasks.curselection()[0]
            self.listbox_tasks.delete(index)
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def mark_done(self):
        try:
            index = self.listbox_tasks.curselection()[0]
            self.listbox_tasks.itemconfig(index, {'bg': 'light gray'})
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to mark as done.")

    def save_tasks(self):
        with open("tasks.txt", "w") as file:
            tasks = self.listbox_tasks.get(0, tk.END)
            for task in tasks:
                file.write(task + "\n")
        self.master.destroy()  # Close the window after saving tasks

    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as file:
                for line in file:
                    self.listbox_tasks.insert(tk.END, line.strip())
        except FileNotFoundError:
            pass

