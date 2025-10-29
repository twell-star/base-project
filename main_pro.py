import csv

def load_regions(filename='regions.csv'):
    """
    Загружает демографические данные по регионам из CSV-файла.
    
    Формат файла:
    region;children_5_7;avg_rent_per_sqm
    Казань;41800;1050
    ...
    
    Возвращает словарь вида:
    {
        "Казань": {"children_5_7": 41800, "avg_rent_per_sqm": 1050},
        ...
    }
    """
    regions_data = {} # Словарь для хранения данных по регионам
    
    with open(filename, "r", encoding="utf-8") as file: # Открываем файл с помощью контекстного менеджера
        # Указываем delimiter=';', так как используется точка с запятой
        reader = csv.DictReader(file, delimiter=";") # Создаем итератор из файла - каждая строка в виде словаря
        for row in reader:
            try:
                region = row["region"]
                children = int(row["children_5_7"]) # Преобразуем строку в целое число
                rent = int(row["avg_rent_per_sqm"]) # Преобразуем строку в целое число
                # Добавляем данные в словарь
                regions_data[region] = {
                    "children_5_7": children,
                    "avg_rent_per_sqm": rent
                }
            except (KeyError, ValueError, TypeError): # Объединение нескольких исключений в одно
                # Пропускаем строки с отсутствующими колонками или некорректными значениями
                continue
    
    return regions_data

def load_businesses(filename='businesses.csv'):
    """
    Загружает данные о бизнесах из CSV-файла.
    
    Формат файла:
    region;okved;ip_count
    Казань;85.59;376
    ...
    
    Возвращает словарь вида:
    {
        "Казань": {"ip_count": 376},
        ...
    }
    """
    businesses_data = {} # Словарь для хранения данных о бизнесов по регионам и ОКВЕД
    
    with open(filename, "r", encoding="utf-8") as file: # Открываем файл с помощью контекстного менеджера
        # Указываем delimiter=';', так как используется точка с запятой
        reader = csv.DictReader(file, delimiter=";") # Создаем итератор из файла - каждая строка в виде словаря
        for row in reader:
            try:
                region = row["region"]  # Получаем регион
                ip_count = int(row["ip_count"])  # Преобразуем строку в целое число
                # Добавляем данные в словарь
                businesses_data[region] = {
                    "ip_count": ip_count,
                }   
            except (KeyError, ValueError, TypeError): # Объединение нескольких исключений в одно
                # Пропускаем строки с отсутствующими колонками или некорректными значениями
                continue
            
    return businesses_data                  

def load_assumptions(filename='assumptions.csv'):
    """
    Загружает данные о предположениях из CSV-файла.
    
    Формат файла:
    region;param;value
    Казань;area_sqm;40
    ...
    
    Возвращает словарь вида:
    {
        "Казань": {"area_sqm": 40, "teachers": 2, ...},
        ...
    }
    """
    assumptions_data = {} # Словарь для хранения данных о предположениях по регионам

    with open(filename, "r", encoding="utf-8") as file: # Открываем файл с помощью контекстного менеджера
        # Указываем delimiter=';', так как используется точка с запятой
        reader = csv.DictReader(file, delimiter=";") # Создаем итератор из файла - каждая строка в виде словаря
        for row in reader:
            try:
                region = row["region"]
                param=row["param"]
                value=int(row["value"]) # Преобразуем строку в целое число
                # Создаем подсловарь для региона, если региона нет в словаре для хранения данных о предположениях
                if region not in assumptions_data:
                    assumptions_data[region] = {}
                # Добавляем данные в подсловарь региона
                assumptions_data[region][param] = value
                
            except (KeyError, ValueError, TypeError): # Объединение нескольких исключений в одно
                # Пропускаем строки с отсутствующими колонками или некорректными значениями
                continue

    return assumptions_data 

print(load_regions())    
print(load_businesses())
print(load_assumptions())
