from app.controller import NotesController
from app.view import display_main_menu

def main():
    # Создать экземпляр контроллера
    notes_controller = NotesController()

    # Загрузить данные из файла (JSON/CSV)
    notes_controller.load_notes()
    notes_controller.run()
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
            break

    print("Спасибо за использование приложения!")


if __name__ == "__main__":
    main()
