def display_main_menu():
    print("Меню:")
    print("1. Создать новую заметку")
    print("2. Посмотреть список заметок")
    print("3. Редактировать заметку")
    print("4. Удалить заметку")
    print("5. Сохранить заметки в файл")
    print("6. Загрузить заметки из файла")
    print("7. Выйти из программы")

def input_note_details():
    title = input("Введите заголовок заметки: ")
    body = input("Введите текст заметки: ")
    return title, body

def input_note_id():
    return input("Введите ID заметки: ")

def input_filename():
    return input("Введите имя файла: ")

def input_file_format():
    return input("Введите формат файла (json/csv): ")

def display_notes_list(notes):
    print("Список заметок:")
    for note in notes:
        print(f"{note.id}: {note.title}")

def display_note_details(note):
    print("Заголовок:", note.title)
    print("Тело:", note.body)
    print("Дата создания:", note.created_at)
    print("Дата последнего обновления:", note.updated_at)

def display_message(message):
    print(message)
