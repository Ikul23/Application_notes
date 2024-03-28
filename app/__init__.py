
from .controller import NotesController
from .model import Note
from .presenter import NotesPresenter
from .view import (
    display_main_menu,
    input_note_details,
    input_note_id,
    input_filename,
    display_notes_list,
    display_note_details,
    display_message,
)
from .logging_config import configure_logging

# Версия приложения
__version__ = '1.0'

# Другие общие настройки и инициализации, если необходимо
