# словарь со всеми доступными предметами
# ключ: (очки выживания, размер в ячейках рюкзака)
items = {
    "r": (25, 3),  # винтовка
    "p": (15, 2),  # пистолет
    "a": (15, 2),  # боекомплект
    "m": (20, 2),  # аптечка
    "i": (5, 1),   # ингалятор
    "k": (15, 1),  # нож
    "x": (20, 3),  # топор
    "t": (25, 1),  # оберег
    "f": (15, 1),  # фляжка
    "d": (10, 1),  # антидот
    "s": (20, 2),  # еда
    "c": (20, 2),  # арбалет
}

# параметры рюкзака по варианту 1
ROWS = 2
COLS = 4
MAX_CAPACITY = ROWS * COLS  # всего 8 ячеек
START_POINTS = 15

# считаем сумму очков вообще всех предметов
all_items_sum = sum(val[0] for val in items.values()) # .values() возвращает значения словаря

best_score = -1000 # начальное минимальное значение очков
best_combination = [] # список для хранения лучшего варианта

item_keys = list(items.keys()) # ключи словаря в список

# перебор всех вариантов (поиск оптимального рюкзака)
def find_best(index, current_weight, chosen_items): # индекс предмета, занятые ячейки, список выбранных предметов
    global best_score, best_combination

    # если превысили вместимость рюкзака, то дальше не идем
    if current_weight > MAX_CAPACITY:
        return

    # когда просмотрели все предметы до конца
    if index == len(item_keys):
        # считаем сумму очков взятых с собой вещей
        taken_sum = sum(items[k][0] for k in chosen_items)
        # не взятые очки = все очки - взятые
        left_sum = all_items_sum - taken_sum

        # итоговые очки: стартовые + взятые - оставленные
        final_score = START_POINTS + taken_sum - left_sum

        # ищем наилучший вариант
        if final_score > best_score:
            best_score = final_score
            best_combination = chosen_items.copy() # сохраняем копию списка
        return

    # получаем данные текущего предмета
    key = item_keys[index]
    points, weight = items[key] # получаем очки и размер предмета

    # ветка 1: берем предмет в рюкзак
    chosen_items.append(key) # добавляем предмет в список выбранных
    find_best(index + 1, current_weight + weight, chosen_items) # рекурсия: переходим к следующему предмету
    chosen_items.pop() # удаляем последний предмет, чтобы восстановить список

    # ветка 2: не берем предмет
    find_best(index + 1, current_weight, chosen_items) # переходим к следующему предмету без него

# запускаем поиск лучшего набора
find_best(0, 0, []) # начинаем с первого предмета и пустого рюкзака

# заполняем ячейки рюкзака обозначениями
backpack_cells = []
for key in best_combination: # перебираем предметы из лучшего варианта
    size = items[key][1] # узнаем размер предмета в ячейках
    for i in range(size): # повторяем столько раз, сколько ячеек занимает предмет
        backpack_cells.append(f"[{key}]") # добавляем обозначение предмета

# если остались свободные ячейки, то заполняем пустыми
while len(backpack_cells) < MAX_CAPACITY:
    backpack_cells.append("[ ]") # добавляем пустую ячейку

# формируем двумерный инвентарь 2x4
print("Итоговый инвентарь:")
for r in range(ROWS): # перебираем строки
    row_slice = backpack_cells[r * COLS : (r + 1) * COLS] # берем 4 ячейки для каждой строки
    print(", ".join(row_slice)) # объединяем ячейки через запятую и выводим строку

print(f"Итоговые очки выживания: {best_score}") # выводим итоговые очки

# проверка условия задачи
if best_score > 0:
    print("Проверка пройдена: итоговый счет положительный!")
else:
    print("Внимание: счет отрицательный!")
