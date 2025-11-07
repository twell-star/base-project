# временный пример списка с шириной столбцов
col_widths = [10, 20, 30]

# Горизонтальная разделительная линия
def make_line(left, mid, right, fill):
    return left + mid.join(fill * (w + 2) for w in col_widths) + right
    
top_line = make_line("┌", "┬", "┐", "─")
mid_line = make_line("├", "┼", "┤", "─")
bot_line = make_line("└", "┴", "┘", "─")

# Вывод таблицы
print(top_line)
print(mid_line)
print(bot_line)
