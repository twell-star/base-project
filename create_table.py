def print_fancy_table(headers, rows, currency_columns=None):
    """
    Выводит таблицу с форматированием.
    Проверка различия версий
    
    Args:
        headers (list): Заголовки столбцов
        rows (list): Строки данных
        currency_columns (list, optional): Индексы столбцов, содержащих денежные значения
    """
    if currency_columns is None:
        currency_columns = []
    
    # Ширина столбцов
    all_data = [headers] + rows
    col_widths = []
    
    for i in range(len(headers)):
        if i in currency_columns:
            # Для столбцов с денежными значениями учитываем форматирование с символом " ₽"
            max_width = 0
            for row in rows:
                if isinstance(row[i], (int, float)):
                    width = len(f"{row[i]:,}".replace(',', ' ') + " ₽")
                else:
                    width = len(str(row[i]))
                max_width = max(max_width, width)
            # Также учитываем ширину заголовка
            max_width = max(max_width, len(headers[i]))
            col_widths.append(max_width)
        else:
            col_widths.append(max(len(str(row[i])) for row in all_data))
    
    # Горизонтальная разделительная линия
    def make_line(left, mid, right, fill):
        return left + mid.join(fill * (w + 2) for w in col_widths) + right
    
    top_line = make_line("┌", "┬", "┐", "─")
    mid_line = make_line("├", "┼", "┤", "─")
    bot_line = make_line("└", "┴", "┘", "─")
    
    def format_row(row, is_header=False):
        formatted_items = []
        for i, item in enumerate(row):
            if not is_header and i in currency_columns:
                # Форматируем денежные значения с пробелами как разделителями тысяч и символом " ₽"
                if isinstance(item, (int, float)):
                    item_str = f"{item:,}".replace(',', ' ') + " ₽"
                    formatted_items.append(item_str.rjust(col_widths[i]))
                else:
                    # Для нечисловых значений в денежных столбцах просто выравниваем по правому краю
                    item_str = str(item)
                    formatted_items.append(item_str.rjust(col_widths[i]))
            else:
                formatted_items.append(str(item).ljust(col_widths[i]))
        return "│ " + " │ ".join(formatted_items) + " │"
    
    # Вывод
    print(top_line)
    print(format_row(headers, is_header=True))
    print(mid_line)
    for row in rows:
        print(format_row(row))
    print(bot_line)
def format_fancy_table(headers, rows, currency_columns=None):
    """
    Форматирует таблицу как строку с форматированием.
    
    Args:
        headers (list): Заголовки столбцов
        rows (list): Строки данных
        currency_columns (list, optional): Индексы столбцов, содержащих денежные значения
        
    Returns:
        str: Строковое представление таблицы
    """
    if currency_columns is None:
        currency_columns = []
    
    # Ширина столбцов
    all_data = [headers] + rows
    col_widths = []
    
    for i in range(len(headers)):
        if i in currency_columns:
            # Для столбцов с денежными значениями учитываем форматирование с символом " ₽"
            max_width = 0
            for row in rows:
                if isinstance(row[i], (int, float)):
                    width = len(f"{row[i]:,}".replace(',', ' ') + " ₽")
                else:
                    width = len(str(row[i]))
                max_width = max(max_width, width)
            # Также учитываем ширину заголовка
            max_width = max(max_width, len(headers[i]))
            col_widths.append(max_width)
        else:
            col_widths.append(max(len(str(row[i])) for row in all_data))
    
    # Горизонтальная разделительная линия
    def make_line(left, mid, right, fill):
        return left + mid.join(fill * (w + 2) for w in col_widths) + right
    
    top_line = make_line("┌", "┬", "┐", "─")
    mid_line = make_line("├", "┼", "┤", "─")
    bot_line = make_line("└", "┴", "┘", "─")
    
    def format_row(row, is_header=False):
        formatted_items = []
        for i, item in enumerate(row):
            if not is_header and i in currency_columns:
                # Форматируем денежные значения с пробелами как разделителями тысяч и символом " ₽"
                if isinstance(item, (int, float)):
                    item_str = f"{item:,}".replace(',', ' ') + " ₽"
                    formatted_items.append(item_str.rjust(col_widths[i]))
                else:
                    # Для нечисловых значений в денежных столбцах просто выравниваем по правому краю
                    item_str = str(item)
                    formatted_items.append(item_str.rjust(col_widths[i]))
            else:
                formatted_items.append(str(item).ljust(col_widths[i]))
        return "│ " + " │ ".join(formatted_items) + " │"
    
    # Формирование строк таблицы
    lines = []
    lines.append(top_line)
    lines.append(format_row(headers, is_header=True))
    lines.append(mid_line)
    for row in rows:
        lines.append(format_row(row))
    lines.append(bot_line)
    
    return "\n".join(lines)

# Пример использования
if __name__ == "__main__":
    # Пример 1: Таблица без денежных столбцов
    headers1 = ["Имя", "Возраст", "Город"]
    rows1 = [
        ["Алиса", 24, "Москва"],
        ["Боб", 19, "Санкт-Петербург"],
        ["Чарли", 35, "Новосибирск"]
    ]
    print("Пример 1: Таблица без денежных значений")
    print(format_fancy_table(headers1, rows1))
    
    print("\n" + "="*50 + "\n")
    
    # Пример 2: Таблица с денежными значениями (столбец с индексом 2)
    headers2 = ["Регион", "Прибыль", "Рентабельность"]
    rows2 = [
        ["Казань", 50000, "16.7%"],
        ["Екатеринбург", 30000, "10.0%"],
        ["Краснодар", 70000, "25.0%"]
    ]
    print("Пример 2: Таблица с денежными значениями")
    print(format_fancy_table(headers2, rows2, currency_columns=[1]))

# Пример использования
if __name__ == "__main__":
    # Пример 1: Таблица без денежных столбцов
    headers1 = ["Имя", "Возраст", "Город"]
    rows1 = [
        ["Алиса", 24, "Москва"],
        ["Боб", 19, "Санкт-Петербург"],
        ["Чарли", 35, "Новосибирск"]
    ]
    print("Пример 1: Таблица без денежных значений")
    print_fancy_table(headers1, rows1)
    
    print("\n" + "="*50 + "\n")
    
    # Пример 2: Таблица с денежными значениями (столбец с индексом 2)
    headers2 = ["Регион", "Прибыль", "Рентабельность"]
    rows2 = [
        ["Казань", 50000, "16.7%"],
        ["Екатеринбург", 30000, "10.0%"],
        ["Краснодар", 70000, "25.0%"]
    ]
    print("Пример 2: Таблица с денежными значениями")
    print_fancy_table(headers2, rows2, currency_columns=[1])
