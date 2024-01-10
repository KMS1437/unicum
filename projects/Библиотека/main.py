import json


def load_data():
    try:
        with open("library.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []
    return data


def save_data(data):
    with open("library.json", "w") as file:
        json.dump(data, file, indent=4)


def add_book():
    title = input("Введите название книги: ")
    author = input("Введите автора книги: ")
    year = input("Введите год издания книги: ")
    book = {
        "title": title,
        "author": author,
        "year": year
    }
    data.append(book)
    save_data(data)
    print("Книга успешно добавлена!")


def delete_book():
    show_books()
    book_index = int(input("Введите номер книги для удаления: ")) - 1
    if book_index >= 0 and book_index < len(data):
        del data[book_index]
        save_data(data)
        print("Книга успешно удалена!")
    else:
        print("Некорректный номер книги!")


def edit_book():
    show_books()
    book_index = int(input("Введите номер книги для редактирования: ")) - 1
    if book_index >= 0 and book_index < len(data):
        book = data[book_index]
        title = input("Введите новое название книги: ")
        author = input("Введите нового автора книги: ")
        year = input("Введите новый год издания книги: ")
        book["title"] = title
        book["author"] = author
        book["year"] = year
        save_data(data)
        print("Книга успешно отредактирована!")
    else:
        print("Некорректный номер книги!")


def show_books():
    if len(data) == 0:
        print("Библиотека пуста!")
    else:
        for i, book in enumerate(data):
            print(f"{i + 1}. Название: {book['title']}, Автор: {book['author']}, Год издания: {book['year']}")


data = load_data()

while True:
    print("\nМеню:")
    print("1. Добавить книгу")
    print("2. Удалить книгу")
    print("3. Редактировать книгу")
    print("4. Показать все книги")
    print("0. Выход")

    choice = input("Выберите пункт меню: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        delete_book()
    elif choice == "3":
        edit_book()
    elif choice == "4":
        show_books()
    elif choice == "0":
        break
    else:
        print("Некорректный пункт меню! Попробуйте еще раз.")
