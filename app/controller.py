
import json
import csv
import datetime
from .model import Note
from .logging_config import configure_logging

class NotesController:
    def __init__(self, logger):
        self.logger = configure_logging()
        self.notes = []

    def create_note(self, title, body):
        new_note = Note(title, body)
        self.notes.append(new_note)
        self.logger.info("Создана новая заметка")
        return new_note

    def get_all_notes(self):
        self.logger.info("Получен список всех заметок")
        return self.notes

    def edit_note(self, note_id, new_title, new_body):
        for note in self.notes:
            if note.id == note_id:
                note.title = new_title
                note.body = new_body
                note.updated_at = datetime.datetime.now()
                self.logger.info(f"Редактирование заметки с ID {note_id}")
                return True  # Заметка успешно отредактирована
        return False  # Заметка с указанным ID не найдена

    def delete_note_by_id(self, note_id):
        for note in self.notes:
            if note.id == note_id:
                self.notes.remove(note)
                self.logger.info(f"Удаление заметки с ID {note_id}")
                return True  # Заметка успешно удалена
        return False  # Заметка с указанным ID не найдена

    def save_notes_to_file(self, filename, format='json'):
        if format == 'json':
            data = [{'id': str(note.id), 'title': note.title, 'body': note.body,
                     'created_at': str(note.created_at), 'updated_at': str(note.updated_at)}
                    for note in self.notes]

            with open(filename, 'w') as file:
                json.dump(data, file, indent=4)
            return True  # Заметки успешно сохранены в файл
        elif format == 'csv':
            # Implement saving to CSV
            with open(filename, 'w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body', 'created_at', 'updated_at'])
                writer.writeheader()
                for note in self.notes:
                    writer.writerow({
                        'id': note.id,
                        'title': note.title,
                        'body': note.body,
                        'created_at': note.created_at,
                        'updated_at': note.updated_at
                    })
            return True
        else:
            return False  # Неподдерживаемый формат файла
