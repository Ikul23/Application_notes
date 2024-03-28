import uuid
import datetime

class Note:
    def __init__(self, title, body):
        self.id = uuid.uuid4()
        self.title = title
        self.body = body
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

class NotesController:
    def __init__(self):
        self.notes = []

    def create_note(self, title, body):
        new_note = Note(title, body)
        self.notes.append(new_note)
        return new_note

    def get_all_notes(self):
        return self.notes
