import logging
from app import NotesController, display_main_menu
from app.logging_config import configure_logging

def main():
    # Настройка логирования
    logger = configure_logging()

    # Создать экземпляр контроллера с передачей объекта логгера
    notes_controller = NotesController(logger)

    # Загрузить данные из файла (JSON/CSV)
    filename = input("Введите имя файла для загрузки заметок: ")
    notes_controller.load_notes(filename)

    # Запуск приложения
    while True:
        display_main_menu()
        choice = input("Введите номер пункта меню: ")

        # Обработка выбора пользователя
        if choice == "1":
            notes_controller.create_note()
        elif choice == "2":
            notes_controller.get_notes()
        elif choice == "3":
            note_id = int(input("Введите ID заметки: "))
            notes_controller.edit_note(note_id)
        elif choice == "4":
            note_id = int(input("Введите ID заметки: "))
            notes_controller.delete_note(note_id)
        elif choice == "5":
            filename = input("Введите имя файла для сохранения заметок: ")
            notes_controller.save_notes(filename)
            break  # Выход из цикла при выборе пункта 5

if __name__ == "__main__":
    main()
