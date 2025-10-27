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
    regions_data = {}
    
    with open(filename, "r", encoding="utf-8") as file:
        # Указываем delimiter=';', так как используется точка с запятой
        reader = csv.DictReader(file, delimiter=";")
        
        for row in reader:
            try:
                region = row["region"]
                children = int(row["children_5_7"])
                rent = int(row["avg_rent_per_sqm"])
                regions_data[region] = {
                    "children_5_7": children,
                    "avg_rent_per_sqm": rent
                }
            except (KeyError, ValueError, TypeError):
                # Пропускаем строки с отсутствующими колонками или некорректными значениями
                continue
    
    return regions_data

print(load_regions())
