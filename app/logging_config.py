import logging

def configure_logging():
    # Создаем объект logger
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Создаем обработчик, который записывает логи в файл app.log
    file_handler = logging.FileHandler('app.log')
    file_handler.setLevel(logging.INFO)

    # Создаем форматирование для логов
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    # Добавляем обработчик к логгеру
    logger.addHandler(file_handler)

    # Возвращаем объект logger
    return logger
