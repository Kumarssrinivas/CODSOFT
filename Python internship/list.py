import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, root_window):
        self.root_window = root_window
        self.root_window.title("To-Do List")

        self.task_data = []

        self.main_frame = tk.Frame(root_window)
        self.main_frame.pack(pady=10)

        self.task_listbox = tk.Listbox(self.main_frame, width=50, height=10, selectmode=tk.MULTIPLE)
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)
        self.task_listbox.bind("<Delete>", self.handle_delete_key)

        self.list_scrollbar = tk.Scrollbar(self.main_frame)
        self.list_scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)
        self.task_listbox.config(yscrollcommand=self.list_scrollbar.set)
        self.list_scrollbar.config(command=self.task_listbox.yview)

        self.task_input = tk.Entry(root_window, width=40)
        self.task_input.pack(pady=10)

        self.add_task_btn = tk.Button(root_window, text="Add Task", width=15, command=self.add_task)
        self.add_task_btn.pack(pady=5)

        self.delete_task_btn = tk.Button(root_window, text="Delete Task", width=15, command=self.delete_task)
        self.delete_task_btn.pack(pady=5)

        self.mark_complete_btn = tk.Button(root_window, text="Mark Complete", width=15, command=self.mark_task_complete)
        self.mark_complete_btn.pack(pady=5)

        self.exit_btn = tk.Button(root_window, text="Exit", command=root_window.quit)
        self.exit_btn.pack(pady=5)

    def add_task(self):
        new_task = self.task_input.get()
        if new_task.strip() != "":
            self.task_data.append({"task": new_task, "completed": False})
            self.refresh_task_listbox()
            self.task_input.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def delete_task(self):
        selected_indices = self.task_listbox.curselection()
        if selected_indices:
            for index in selected_indices[::-1]:
                self.task_data.pop(index)
            self.refresh_task_listbox()
        else:
            messagebox.showwarning("Warning", "You must select a task to delete.")

    def handle_delete_key(self, event):
        self.delete_task()

    def mark_task_complete(self):
        selected_indices = self.task_listbox.curselection()
        if selected_indices:
            for index in selected_indices:
                if not self.task_data[index]["completed"]:
                    self.task_data[index]["completed"] = True
            self.refresh_task_listbox()
        else:
            messagebox.showwarning("Warning", "You must select a task to mark complete.")

    def refresh_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for index, task_info in enumerate(self.task_data):
            task_text = f"{index + 1}. {task_info['task']}"
            if task_info["completed"]:
                task_text += " (Completed)"
            self.task_listbox.insert(tk.END, task_text)
            if task_info["completed"]:
                self.task_listbox.itemconfig(tk.END, {'bg': 'light green'})

if __name__ == "__main__":
    root_window = tk.Tk()
    todo_app = ToDoListApp(root_window)
    root_window.mainloop()
