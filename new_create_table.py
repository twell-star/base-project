# временный пример списка с шириной столбцов
col_widths = [10, 20, 30]

def format_whole_number(amount):
    """Форматирует целочисленное значение суммы с пробелами (например, 155000 → "155 000")."""
    if isinstance(amount, int):
        return f'{amount:,}'.replace(',', ' ')
    return str(amount)

def add_rouble_symbol(amount):
    """Добавляет символ "руб" к денежной сумме."""
    return format_whole_number(amount) + ' ₽'

# Горизонтальная разделительная линия
def make_line(left, mid, right, fill):
    return left + mid.join(fill * (w + 2) for w in col_widths) + right
    
top_line = make_line('┌', '┬', '┐', '─')
mid_line = make_line('├', '┼', '┤', '─')
bot_line = make_line('└', '┴', '┘', '─')

# Вывод таблицы
print(top_line)
print(mid_line)
print(bot_line)

a = 104389
print(add_rouble_symbol(a))
print(format_whole_number(a))

state_line = '┌' + '─'*col_widths[1] + '┐'
print(state_line)
delta = len(state_line) - len(add_rouble_symbol(a)) - 2
print(' '*delta + add_rouble_symbol(a))
