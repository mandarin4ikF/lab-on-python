import os
import time

# \u001b[ — CSI, 4x — цвет бэкграунда 
BLUE = "\u001b[44m"
WHITE = "\u001b[47m"
RED = "\u001b[41m"
RESET = "\u001b[0m" #0m — сброс стилей


def flag():
    # выводим построчно * пробелов на ширину полосы
    for i in range(8):
        print(f"{BLUE}{' ' * 7}{WHITE}{' ' * 7}{RED}{' ' * 7}{RESET}")
    print()


def pattern():
    for i in range(8):
        row = ""
        for j in range(8):
            color = WHITE if (i + j) % 2 == 0 else BLUE
            row += f"{color}   {RESET}"
        print(row)
    print()


def animation():
    frames = [
        "   [|] Загрузка...",
        "   [/] Загрузка...",
        "   [-] Загрузка...",
        "   [\\] Загрузка...",
    ]
    for i in range(3):
        for frame in frames:
            os.system("clear")
            print(frame)
            time.sleep(0.2) # скорость анимации
    print("Готово!")


def sequence():
    file = open("sequence.txt")
    count1 = 0
    count2 = 0

    for line in file:
        num = float(line)
        if num < 0:
            count1 += 1
        elif num > 0:
            count2 += 1


    all = count1 + count2   
    p_count1 = round((count1 / all) * 100, 1)
    p_count2 = round((count2 / all) * 100, 1)

    print(f"< 0: {BLUE}{' ' * int(p_count1 // 2)}{RESET} {p_count1}% ({count1})")
    print(f"> 0: {RED}{' ' * int(p_count2 // 2)}{RESET} {p_count2}% ({count2})\n")


def plot():
    for y in range(16, -1, -1):
        line = ""
        for x in range(-4, 5):
            line += "* " if x**2 == y else "  "
        print(line)


flag()
pattern()
sequence()
plot()
#animation()