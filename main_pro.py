"""Модуль для анализа финансовой эффективности детских центров развития.

Этот модуль загружает демографические данные, данные о бизнесах и предположения
из CSV-файлов, позволяет пользователю выбрать регионы для анализа и вычисляет
финансовые показатели для выбранных регионов.
"""

import csv
import math

def load_regions(filename='regions.csv'):
    """Загружает демографические данные по регионам из CSV-файла.
    
    Формат файла:
        region;children_5_7;avg_rent_per_sqm
        Казань;41800;1050
        ...
        
    Args:
        filename (str, optional): Путь к CSV-файлу с данными. По умолчанию 'regions.csv'.
        
    Returns:
        dict: Словарь вида:
            {
                "Казань": {"children_5_7": 41800, "avg_rent_per_sqm": 1050},
                ...
            }
            
    Исключения:
        FileNotFoundError: Если файл не найден.
        KeyError, ValueError, TypeError: При некорректных данных в файле.
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
    """Загружает данные о бизнесах из CSV-файла.
    
    Формат файла:
        region;ip_count
        Казань;376
        ...
        
    Args:
        filename (str, optional): Путь к CSV-файлу с данными. По умолчанию 'businesses.csv'.
        
    Returns:
        dict: Словарь, где ключи - названия регионов, значения - словари с данными:
            {
                "Казань": {"ip_count": 376},
                ...
            }
            
    Исключения:
        FileNotFoundError: Если файл не найден.
        KeyError, ValueError, TypeError: При некорректных данных в файле.
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
    """Загружает данные о предположениях из CSV-файла.
    
    Формат файла:
        region;param;value
        Казань;area_sqm;40
        ...
        
    Args:
        filename (str, optional): Путь к CSV-файлу с данными. По умолчанию 'assumptions.csv'.
        
    Returns:
        dict: Словарь, где ключи - названия регионов, значения - словари с параметрами:
            {
                "Казань": {"area_sqm": 40, "param_name": value, ...},
                ...
            }
            
    Исключения:
        FileNotFoundError: Если файл не найден.
        KeyError, ValueError, TypeError: При некорректных данных в файле.
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

def select_regions(regions_dict):
    """Позволяет пользователю выбрать регионы для анализа через интерактивное меню.
    
    Функция выводит список всех доступных регионов и предлагает выбрать режим анализа:
    - S: Анализ одного региона
    - D: Сравнение двух регионов
    - A: Анализ всех регионов
    
    Args:
        regions_dict (dict): Словарь с данными по регионам в формате:
            {
                "Казань": {"children_5_7": 41800, "avg_rent_per_sqm": 1050},
                ...
            }
            
    Returns:
        list: Список выбранных регионов для анализа.
        
    Raises:
        SystemExit: Если пользователь сделал некорректный выбор.
    """
    regions_list = sorted(regions_dict.keys()) # Список всех регионов
    selected_regions = [] # Список для хранения выбранных регионов
    
    # Выводим список всех доступных регионов
    print('\nДля дальнейшего анализа можно выбрать следующие регионы:')
    for index, region in enumerate(regions_list, 1):
        print(f'{index}. {region}')
    print(f'Всего в списке {len(regions_list)} регионов.\n')
    
    # Предлагаем пользователю выбрать режим анализа
    print('Введите код режима анализа:')
    print('S - Анализ одного региона')
    print('D - Сравнение двух регионов')
    print('A - Анализ всех регионов')
    
    # Основной цикл обработки выбора режима анализа
    while True:
        mode = input('Введите код режима: ')
        match mode:
            # Обработка выбора одного региона
            case 'S' | 's':
                while True:
                    choise_region = int(input('Введите номер региона: '))
                    # Проверяем, что номер региона в допустимом диапазоне
                    if choise_region in range(1, len(regions_list)+1):
                        selected_regions.append(regions_list[choise_region-1])
                        print(f'\nВы выбрали для анализа {selected_regions[0]}')
                        return selected_regions
                    else:
                        print('\nНеверно. Повторите выбор региона.\n')
            # Обработка выбора двух регионов для сравнения
            case 'D' | 'd':
                while True:
                    choise_region1 = int(input('Введите номер первого региона: '))
                    choise_region2 = int(input('Введите номер второго региона: '))
                    # Проверяем, что оба номера регионов в допустимом диапазоне и не равны друг другу
                    if choise_region1 in range(1, len(regions_list)+1) and\
                    choise_region2 in range(1, len(regions_list)+1) and\
                    choise_region1 != choise_region2:
                        selected_regions.append(regions_list[choise_region1-1])
                        selected_regions.append(regions_list[choise_region2-1])
                        print(f'\nВы выбрали для сравнительного анализа {selected_regions[0]} и {selected_regions[1]}')
                        return selected_regions
                    else:
                        print('\nНеверно. Повторите выбор регионов.\n')
            # Обработка выбора всех регионов
            case 'A' | 'a':
                selected_regions = regions_list
                print(f'\nВы выбрали для анализа все регионы')
                return selected_regions
            # Обработка некорректного ввода
            case _:
                print('\nНеверно. Повторите выбор режима.\n')

def calculate_financials(region, regions=None, businesses=None, assumptions=None):
    """
    Вычисляет финансовые показатели для региона.
    
    Args:
        region (str): Название региона.
        regions (dict, optional): Словарь с данными о регионах. По умолчанию None.
        businesses (dict, optional): Словарь с бизнес-показателями для регионов. По умолчанию None.
        assumptions (dict, optional): Словарь с предположениями для регионов. По умолчанию None.
        
    Returns:
        dict: Словарь с финансовыми показателями для региона.
        
    Исключения:
        KeyError: Если в словарях regions, businesses или assumptions отсутствуют необходимые ключи.
        TypeError: Если типы данных в словарях regions, businesses или assumptions некорректны.
        ZeroDivisionError: При делении на ноль при расчете плотности конкуренции.
    """
    if regions is None:
        regions = load_regions()[region]
    if businesses is None:
        businesses = load_businesses()[region]
    if assumptions is None:
        assumptions = load_assumptions()[region]
    financials = {}
    rent = regions['avg_rent_per_sqm'] * assumptions['area_sqm']   # расходы на аренду (ежемесячные)
    salaries = assumptions['teachers'] * assumptions['salary_per_teacher']   # зарплата персонала центра
    monthly_sales_volume = 60   # объем продаж в месяц (базовый сценарий)
    initial_investment = 500000   # начальные инвестиции в бизнес
    financials['region'] = region
    financials['total_costs'] = rent + salaries + assumptions['marketing'] + assumptions['other_costs']   # общие месячные затраты
    financials['monthly_revenue'] = assumptions['avg_check'] * monthly_sales_volume   # месячная выручка
    financials['profit'] = financials['monthly_revenue'] - financials['total_costs']   # чистая прибыль в месяц
    financials['profitability'] = round((financials['profit'] / financials['monthly_revenue']) * 100, 1)   # рентабельность
    match financials['profitability']:
        case x if x <= 10:
            financials['profitability_level'] = 'low'   # низкий уровень рентабельности
        case x if x <= 25:
            financials['profitability_level'] = 'regular'   # обычный уровень рентабельности
        case x if x > 25:
            financials['profitability_level'] = 'high'   # высокий уровень рентабельности
    financials['break_even_children'] = math.ceil(financials['total_costs'] / assumptions['avg_check'])   # точка безубыточности
    financials['competition_density'] = round(businesses['ip_count'] / (regions['children_5_7'] / 1000), 1)   # плотность конкуренции
    match financials['competition_density']:
        case x if x <= 8:
            financials['competition_level'] = 'low'   # низкий уровень конкуренции
        case x if x <= 12:
            financials['competition_level'] = 'medium'   # умеренный уровень конкуренции
        case x if x > 12:
            financials['competition_level'] = 'high'   # высокий уровень конкуренции
    if financials['profit'] > 0:
        financials['payback_period_month'] = math.ceil(initial_investment / financials['profit'])   # срок окупаемости в полных месяцах
    else:
        financials['payback_period_month'] = 'no payback'

    return financials
    
regions_data = load_regions()
print(regions_data)
businesses_data = load_businesses()
print(businesses_data)
assumptions_data = load_assumptions()
print(assumptions_data)
selected_regions = sorted(select_regions(load_regions()))
print(selected_regions)
result = {}
for region in selected_regions:
    result[region] = calculate_financials(region)
print(result)
