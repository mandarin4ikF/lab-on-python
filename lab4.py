# словарь со всеми доступными предметами
# ключ: (очки выживания, размер в ячейках рюкзака)
items = {
    "r": (25, 3),  # винтовка
    "p": (15, 2),  # пистолет
    "a": (15, 2),  # боекомплект
    "m": (20, 2),  # аптечка
    "i": (5, 1),  # ингалятор
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
all_items_sum = sum(val[0] for val in items.values())

best_score = -1000
best_combination = []

item_keys = list(items.keys())


# перебор всех вариантов (поиск оптимального рюкзака)
def find_best(index, current_weight, chosen_items):
    global best_score, best_combination

    # если превысили вместимость рюкзака - дальше не идем
    if current_weight > MAX_CAPACITY:
        return

    # когда просмотрели все предметы до конца
    if index == len(item_keys):
        # считаем сумму очков взятых с собой вещей
        taken_sum = sum(items[k][0] for k in chosen_items)
        # не взятые очки = все очки минус взятые
        left_sum = all_items_sum - taken_sum

        # итоговые очки: стартовые + взятые - оставленные
        final_score = START_POINTS + taken_sum - left_sum

        if final_score > best_score:
            best_score = final_score
            best_combination = chosen_items.copy()
        return

    key = item_keys[index]
    points, weight = items[key]

    # ветка 1: берем предмет в рюкзак
    chosen_items.append(key)
    find_best(index + 1, current_weight + weight, chosen_items)
    chosen_items.pop()

    # ветка 2: не берем предмет
    find_best(index + 1, current_weight, chosen_items)


# запускаем поиск лучшего набора
find_best(0, 0, [])

# заполняем ячейки рюкзака обозначениями
# каждый предмет занимает столько ячеек, каков его размер
backpack_cells = []
for key in best_combination:
    size = items[key][1]
    for _ in range(size):
        backpack_cells.append(f"[{key}]")

# если остались свободные ячейки - заполняем пустыми
while len(backpack_cells) < MAX_CAPACITY:
    backpack_cells.append("[ ]")

# формируем двумерный инвентарь 2x4
print("Итоговый инвентарь:")
for r in range(ROWS):
    row_slice = backpack_cells[r * COLS : (r + 1) * COLS]
    print(", ".join(row_slice))

print(f"\nИтоговые очки выживания: {best_score}")

# проверка условия задачи
if best_score > 0:
    print("Проверка пройдена: итоговый счет положительный!")
else:
    print("Внимание: счет отрицательный!")