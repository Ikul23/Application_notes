from datetime import datetime

def display_main_menu():
    print("Меню:")
    print("1. Создать новую заметку")
    print("2. Посмотреть список заметок")
    print("3. Редактировать заметку")
    print("4. Удалить заметку")
    print("5. Выйти из программы")

def display_notes_list(notes):
    print("Список заметок:")
    for note in notes:
        print(f"ID: {note.id}, Заголовок: {note.title}")

def display_note_details(note):
    print(f"Заметка ID: {note.id}")
    print(f"Заголовок: {note.title}")
    print(f"Тело: {note.body}")
    print(f"Дата создания: {note.created_date}")
    print(f"Дата изменения: {note.modified_date}")

def display_edit_note_form(note):
    print(f"Редактирование заметки ID: {note.id}")
    print("Введите новые данные:")
    title = input("Новый заголовок: ")
    body = input("Новое тело заметки: ")
    note.title = title
    note.body = body
    note.modified_date = datetime.now()
    print("Заметка успешно отредактирована.")
