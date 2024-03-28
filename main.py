import logging
from app.presenter import NotesPresenter
from app.view import display_main_menu, input_filename
from app.logging_config import configure_logging  # Импортируем функцию configure_logging

def main():
    logger = configure_logging()  # Вызываем функцию configure_logging для настройки логирования
    presenter = NotesPresenter()

    while True:
        display_main_menu()
        choice = input("Введите номер пункта меню: ")

        if choice == "1":
            presenter.create_note()
        elif choice == "2":
            presenter.get_notes()
        elif choice == "3":
            presenter.edit_note()
        elif choice == "4":
            presenter.delete_note()
        elif choice == "5":
            filename = input_filename()
            file_format = input("Введите формат файла (json/csv): ")
            presenter.save_notes_to_file(filename, file_format)
        elif choice == "6":
            presenter.load_notes_from_file()
        elif choice == "7":
            break

if __name__ == "__main__":
    main()
