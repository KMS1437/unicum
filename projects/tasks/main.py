import tkinter as tk
from tkinter import messagebox, ttk
from tkcalendar import DateEntry
from datetime import datetime
import json

class Task:
    def __init__(self, name, priority, due_date):
        self.name = name
        self.priority = priority
        self.due_date = due_date

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Менеджер задач")
        self.root.geometry("800x400")

        self.tasks = self.load_tasks_from_json()

        s = ttk.Style()
        s.theme_use('clam')

        font_style = ('Arial', 12, 'bold')

        ttk.Label(self.root, text="Название задачи:", font=font_style).grid(row=0, column=0, sticky="w")
        self.task_name_entry = tk.Entry(self.root)
        self.task_name_entry.grid(row=0, column=1, pady=5, padx=10, sticky="w")

        ttk.Label(self.root, text="Приоритет:", font=font_style).grid(row=1, column=0, sticky="w")
        priority_values = ["Низкий", "Средний", "Высокий"]
        self.priority_dropdown = ttk.Combobox(self.root, values=priority_values)
        self.priority_dropdown.grid(row=1, column=1, pady=5, padx=10, sticky="w")

        ttk.Label(self.root, text="Дата завершения:", font=font_style).grid(row=2, column=0, sticky="w")
        self.due_date_calendar = DateEntry(self.root, date_pattern='yyyy-mm-dd')
        self.due_date_calendar.grid(row=2, column=1, pady=5, padx=10, sticky="w")

        add_button = ttk.Button(self.root, text="Добавить задачу", command=lambda: self.add_task(self.task_name_entry.get(), self.priority_dropdown.get(), self.due_date_calendar.get_date()))
        add_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.task_list_box = tk.Listbox(self.root)
        self.task_list_box.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        self.update_task_list()

    def add_task(self, name, priority, due_date):
        task = Task(name, priority, due_date)
        self.tasks.append(task)
        self.update_task_list()
        self.save_tasks_to_json()
        messagebox.showinfo("Задача добавлена",
                            f"Задача '{name}' была добавлена с приоритетом '{priority}' и датой завершения '{due_date}'.")

    def update_task_list(self):
        self.task_list_box.delete(0, tk.END)
        for task in self.tasks:
            self.task_list_box.insert(tk.END, f"{task.name} - {task.priority} - {task.due_date}")

    def save_tasks_to_json(self):
        tasks_data = [{"name": task.name, "priority": task.priority, "due_date": task.due_date.strftime('%Y-%m-%d')} for
                      task in self.tasks]
        with open('tasks.json', 'w') as json_file:
            json.dump(tasks_data, json_file, ensure_ascii=False, indent=4)

    def load_tasks_from_json(self):
        try:
            with open('tasks.json', 'r') as json_file:
                tasks_data = json.load(json_file)
                tasks = [Task(task['name'], task['priority'], datetime.strptime(task['due_date'], '%Y-%m-%d').date())
                         for task in tasks_data]
                return tasks
        except FileNotFoundError:
            return []

root = tk.Tk()
app = TaskManagerApp(root)
root.mainloop()
