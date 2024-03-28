from .logging_config import configure_logging
from .controller import NotesController
from .view import input_note_details, input_note_id, display_message

class NotesPresenter:
    def __init__(self):
        self.logger = configure_logging()
        self.controller = NotesController(self.logger)

    def create_note(self):
        title, body = input_note_details()
        self.controller.create_note(title, body)
        display_message("Заметка создана успешно.")

    def get_notes(self):
        notes = self.controller.get_all_notes()
        display_notes_list(notes)

    def edit_note(self):
        note_id = input_note_id()
        new_title, new_body = input_note_details()
        success = self.controller.edit_note(note_id, new_title, new_body)
        if success:
            display_message("Заметка успешно отредактирована.")
        else:
            display_message("Заметка с указанным ID не найдена.")

    def delete_note(self):
        note_id = input_note_id()
        success = self.controller.delete_note_by_id(note_id)
        if success:
            display_message("Заметка успешно удалена.")
        else:
            display_message("Заметка с указанным ID не найдена.")

    def save_notes_to_file(self, filename, file_format):  # Modify method signature
        success = self.controller.save_notes_to_file(filename, file_format)  # Call controller method with arguments
        if success:
            display_message("Заметки успешно сохранены в файл.")
        else:
            display_message("Ошибка при сохранении заметок в файл.")

    def load_notes_from_file(self):
        filename = input_filename()
        success = self.controller.load_notes_from_file(filename)
        if success:
            display_message("Заметки успешно загружены из файла.")
        else:
            display_message("Ошибка при загрузке заметок из файла.")
