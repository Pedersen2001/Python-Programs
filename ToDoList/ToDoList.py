import tkinter as tk
from tkinter import messagebox


class ToDoList:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        # Task list
        self.tasks = []

        # Entry for new task
        self.task_entry = tk.Entry(root, width=50)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        # Add Task button
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=5, pady=10)

        # Task list display
        self.task_listbox = tk.Listbox(root, width=50)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

        # Delete Task button
        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_index]
            self.task_listbox.delete(selected_index)
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to delete.")


if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoList(root)
    root.mainloop()
