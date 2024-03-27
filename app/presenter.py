from datetime import datetime

def format_date(date):
    """Форматирует дату для отображения."""
    return datetime.strptime(date, '%Y-%m-%d %H:%M:%S').strftime('%d.%m.%Y %H:%M:%S')

def format_notes_list(notes):
    """Форматирует список заметок для отображения."""
    formatted_notes = []
    for note in notes:
        formatted_note = {
            "ID": note.id,
            "Заголовок": note.title,
            "Дата создания": format_date(note.created_date),
            "Дата изменения": format_date(note.modified_date)
        }
        formatted_notes.append(formatted_note)
    return formatted_notes

def format_note_details(note):
    """Форматирует детали заметки для отображения."""
    formatted_note = {
        "ID": note.id,
        "Заголовок": note.title,
        "Тело": note.body,
        "Дата создания": format_date(note.created_date),
        "Дата изменения": format_date(note.modified_date)
    }
    return formatted_note
