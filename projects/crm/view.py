import tkinter as tk
from tkinter import messagebox

class CRMView:
    def __init__(self, controller):
        self.controller = controller
        self.root = tk.Tk()
        self.root.title("crm cистема")

        self.name_label = tk.Label(self.root, text="имя:")
        self.name_label.pack()
        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack()

        self.email_label = tk.Label(self.root, text="email:")
        self.email_label.pack()
        self.email_entry = tk.Entry(self.root)
        self.email_entry.pack()

        self.phone_label = tk.Label(self.root, text="телефон:")
        self.phone_label.pack()
        self.phone_entry = tk.Entry(self.root)
        self.phone_entry.pack()

        self.add_button = tk.Button(self.root, text="добавить пользователя", command=self.add_user)
        self.add_button.pack()

        self.delete_button = tk.Button(self.root, text="удалить пользователя", command=self.delete_user)
        self.delete_button.pack()

        self.find_button = tk.Button(self.root, text="найти пользователя", command=self.find_user)
        self.find_button.pack()

        self.update_button = tk.Button(self.root, text="обновить пользователя", command=self.update_user)
        self.update_button.pack()

    def add_user(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        phone = self.phone_entry.get()
        self.controller.add_user(name, email, phone)
        messagebox.showinfo("успех", "пользователь успешно добавлен.")

    def delete_user(self):
        name = self.name_entry.get()
        self.controller.delete_user(name)
        messagebox.showinfo("успех", "пользователь успешно удален.")

    def find_user(self):
        name = self.name_entry.get()
        user = self.controller.find_user(name)
        if user:
            messagebox.showinfo("успех", f"Пользователь {user.name} найден")
        else:
            messagebox.showinfo("успех", f"Пользователь {name} не найден")

    def update_user(self):
        name = self.name_entry.get()
        new_email = self.email_entry.get()
        new_phone = self.phone_entry.get()
        self.controller.update_user(name, new_email, new_phone)
        messagebox.showinfo("успех", "пользователь успешно обновлен.")

    def run(self):
        self.root.mainloop()
