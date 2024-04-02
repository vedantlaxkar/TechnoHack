from tkinter import *

class TodoList:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.configure(background="black")  # Setting background color to black

        self.tasks = []

        # Main Page (Front Page)
        self.main_frame = Frame(self.root, bg="black")
        self.main_frame.pack(pady=50)

        self.add_button = Button(self.main_frame, text="Add Task", font=("Helvetica", 14), bg="#4682B4", fg="white", command=self.goto_add_task)
        self.add_button.pack(padx=10, pady=5)

        self.show_button = Button(self.main_frame, text="Show Tasks", font=("Helvetica", 14), bg="#4682B4", fg="white", command=self.goto_show_tasks)
        self.show_button.pack(padx=10, pady=5)

        self.clear_button = Button(self.main_frame, text="Clear All", font=("Helvetica", 14), bg="#4682B4", fg="white", command=self.clear_tasks)
        self.clear_button.pack(padx=10, pady=5)

        # Add Task Frame
        self.add_task_frame = Frame(self.root, bg="black")
        self.task_label = Label(self.add_task_frame, text="Enter Task:", font=("Helvetica", 16), bg="black", fg="white")
        self.task_label.pack(padx=10, pady=10)
        self.task_entry = Entry(self.add_task_frame, font=("Helvetica", 16))
        self.task_entry.pack(padx=10, pady=10)
        self.add_task_button = Button(self.add_task_frame, text="Add Task", font=("Helvetica", 14), bg="#4682B4", fg="white", command=self.add_task)
        self.add_task_button.pack(padx=10, pady=10)
        self.add_task_back_button = Button(self.add_task_frame, text="Back", font=("Helvetica", 14), bg="#4682B4", fg="white", command=self.clear_screen)
        self.add_task_back_button.pack(padx=10, pady=10)

        # Show Task Frame
        self.show_task_frame = Frame(self.root, bg="black")
        self.tasks_label = Label(self.show_task_frame, text="Tasks:", font=("Helvetica", 16), bg="black", fg="white")
        self.tasks_label.pack(padx=10, pady=10)
        self.tasks_listbox = Listbox(self.show_task_frame, font=("Helvetica", 16), width=40, height=10)
        self.tasks_listbox.pack(padx=10, pady=10)
        self.mark_complete_button = Button(self.show_task_frame, text="Mark Complete", font=("Helvetica", 14), bg="#4682B4", fg="white", command=self.mark_complete)
        self.mark_complete_button.pack(padx=10, pady=5)
        self.delete_button = Button(self.show_task_frame, text="Delete Task", font=("Helvetica", 14), bg="#4682B4", fg="white", command=self.delete_task)
        self.delete_button.pack(padx=10, pady=5)
        self.show_task_back_button = Button(self.show_task_frame, text="Back", font=("Helvetica", 14), bg="#4682B4", fg="white", command=self.clear_screen)
        self.show_task_back_button.pack(padx=10, pady=10)

    def goto_add_task(self):
        self.clear_screen()
        self.add_task_frame.pack(padx=10, pady=10)

    def goto_show_tasks(self):
        self.clear_screen()
        self.update_tasks_listbox()
        self.show_task_frame.pack(padx=10, pady=10)

    def clear_screen(self):
        for frame in [self.add_task_frame, self.show_task_frame]:
            frame.pack_forget()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_entry.delete(0, END)
            self.update_tasks_listbox()

    def update_tasks_listbox(self):
        self.tasks_listbox.delete(0, END)
        for task in self.tasks:
            self.tasks_listbox.insert(END, task)

    def mark_complete(self):
        selected_task = self.tasks_listbox.curselection()
        if selected_task:
            index = int(selected_task[0])
            self.tasks[index] = "✔ " + self.tasks[index]
            self.update_tasks_listbox()

    def delete_task(self):
        selected_task = self.tasks_listbox.curselection()
        if selected_task:
            index = int(selected_task[0])
            del self.tasks[index]
            self.update_tasks_listbox()

    def clear_tasks(self):
        self.tasks.clear()
        self.update_tasks_listbox()

if __name__ == "__main__":
    root = Tk()
    todo_app = TodoList(root)
    root.mainloop()
