import json
import hashlib
import tkinter as tk
from tkinter import messagebox, font

def register():
    global username_entry, password_entry
    with open('credentials.json') as file:
        credentials = json.load(file)

    username = username_entry.get()
    password = password_entry.get()

    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    if username in credentials:
        messagebox.showerror('Ошибка', 'Пользователь с таким именем уже существует.')
    else:
        credentials[username] = hashed_password
        with open('credentials.json', 'w') as file:
            json.dump(credentials, file)
        messagebox.showinfo('Успех', 'Регистрация прошла успешно!')

def login():
    global username_entry, password_entry
    with open('credentials.json') as file:
        credentials = json.load(file)

    username = username_entry.get()
    password = password_entry.get()

    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    if username in credentials and hashed_password == credentials[username]:
        messagebox.showinfo('Успех', 'Вход выполнен успешно!')
    else:
        messagebox.showerror('Ошибка', 'Неверное имя пользователя или пароль.')

def main():
    global username_entry, password_entry
    root = tk.Tk()
    root.title('Система аутентификации')
    root.geometry('400x300')

    welcome_label = tk.Label(root, text='Добро пожаловать в систему аутентификации', font=('Arial', 14))
    welcome_label.pack(pady=20)

    label_username = tk.Label(root, text='Имя пользователя:')
    label_username.pack()

    username_entry = tk.Entry(root)
    username_entry.pack()

    label_password = tk.Label(root, text='Пароль:')
    label_password.pack()

    password_entry = tk.Entry(root, show='*')
    password_entry.pack()

    register_button = tk.Button(root, text='Зарегистрироваться', command=register, bg='green', fg='white')
    register_button.pack(pady=10)

    login_button = tk.Button(root, text='Войти', command=login, bg='blue', fg='white')
    login_button.pack()

    root.mainloop()

if __name__ == '__main__':
    main()
