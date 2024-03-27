import json
import csv
from datetime import datetime

class NotesController:
    def __init__(self):
        self.notes = []

    def load_notes(self):
        filename = input("Введите имя файла для загрузки заметок: ")
        # Реализуйте загрузку заметок из файла
        pass

    def save_notes(self):
        filename = input("Введите имя файла для сохранения заметок: ")
        # Реализуйте сохранение заметок в файл
        pass

    def run(self):
        # Основной цикл приложения
        pass

    def create_note(self):
        pass

    def get_notes(self):
        pass

    def edit_note(self, note_id):
        pass

    def delete_note(self, note_id):
        pass
