class NotesController:
    def __init__(self, logger):
        self.logger = logger
        self.notes = []

    def load_notes(self, filename):
        """Загружает заметки из файла."""
        # Ваш код загрузки заметок
        self.logger.info(f"Загружены заметки из файла: {filename}")

    def save_notes(self, filename):
        """Сохраняет заметки в файл."""
        # Ваш код сохранения заметок
        self.logger.info(f"Сохранены заметки в файл: {filename}")

    def edit_note(self, note_id):
        """Редактирует заметку по ее ID."""
        # Ваш код редактирования заметки
        self.logger.info(f"Редактирование заметки с ID {note_id}")

    def get_notes(self):
        """Получает список всех заметок."""
        # Ваш код получения списка заметок
        self.logger.info("Получен список всех заметок")

    def create_note(self):
        """Создает новую заметку."""
        # Ваш код создания новой заметки
        self.logger.info("Создана новая заметка")

    def delete_note(self, note_id):
        """Удаляет заметку по ее ID."""
        # Ваш код удаления заметки
        self.logger.info(f"Удаление заметки с ID {note_id}")

    def check_duplicate_id(self, note_id):
        """Проверяет, существует ли заметка с данным ID."""
        for note in self.notes:
            if note.id == note_id:
                return True
        return False
