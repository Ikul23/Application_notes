from .model import Заметка
from .view import display_main_menu, display_notes_list, display_note_details, display_edit_note_form

class NotesController:
    def __init__(self):
        self.notes = []

    def load_notes(self):
        # ...

    def save_notes(self):
        # ...

    def run(self):
        while True:
            display_main_menu()
            choice = input("Введите номер пункта меню: ")

            # Обработка выбора пользователя
            if choice == "1":
                self.create_note()
            elif choice == "2":
                self.get_notes()
            elif choice == "3":
                note_id = int(input("Введите ID заметки: "))
                self.edit_note(note_id)
            elif choice == "4":
                note_id = int(input("Введите ID заметки: "))
                self.delete_note(note_id)
            elif choice == "5":
                break

        print("Спасибо за использование приложения!")

# Создать экземпляр контроллера
notes_controller = NotesController()

# Загрузить данные из файла (JSON/CSV)
notes_controller.load_notes()
