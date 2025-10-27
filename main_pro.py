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
        lines = file.readlines()
    
    # Пропускаем заголовок
    for line in lines[1:]:
        if not line.strip():
            continue  # пропустить пустые строки
        
        parts = line.strip().split(";")
        if len(parts) < 3:
            continue  # некорректная строка
        
        region = parts[0]
        try:
            children = int(parts[1])
            rent = int(parts[2])
        except ValueError:
            continue  # пропустить строки с некорректными числами
        
        regions_data[region] = {
            "children_5_7": children,
            "avg_rent_per_sqm": rent
        }
    
    return regions_data

print(load_regions())
