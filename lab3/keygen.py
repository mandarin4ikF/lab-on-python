import tkinter as tk
import random
import string
import pygame


# генерация одного блока из 5 символов
def generate_block():
    # берем 3 случайные заглавные буквы
    letters = [random.choice(string.ascii_uppercase) for i in range(3)]
    # берем 2 случайные цифры
    digits = [random.choice(string.digits) for i in range(2)]

    # объединяем буквы и цифры в один список
    block = letters + digits

    # перемешиваем список чтобы порядок был случайным
    random.shuffle(block)

    # склеиваем список в одну строку
    return "".join(block)


# функция срабатывает при нажатии на кнопку
def clicked():
    # соединяем три готовых блока через дефис
    key = f"{generate_block()}-{generate_block()}-{generate_block()}"
    # выводим получившийся ключ на экран
    lbl_key.configure(text=key)


# список цветов для анимации текста
colors = [
    "#FF0000",
    "#FF7F00",
    "#FFFF00",
    "#00FF00",
    "#0000FF",
    "#4B0082",
    "#9400D3",
]
color_index = 0


# плавная смена цвета заголовка
def animate_title():
    global color_index
    # меняем цвет текста надписи
    lbl_title.configure(fg=colors[color_index])
    # сдвигаем индекс на следующий цвет по кругу
    color_index = (color_index + 1) % len(colors)
    # вызываем эту же функцию снова через 100 миллисекунд
    window.after(100, animate_title)


# создаем главное окно программы
window = tk.Tk()
window.title("Red Dead Redemption 2")
window.geometry("900x500")
# запрещаем менять размер окна мышкой
window.resizable(False, False)

# включаем музыку и ставим на бесконечный повтор
pygame.mixer.init()
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play(-1)

# ставим картинку на весь фон окна
bg_img = tk.PhotoImage(file="bg.png")
label_bg = tk.Label(window, image=bg_img)
label_bg.place(x=0, y=0, relwidth=1, relheight=1)

# заголовок программы
lbl_title = tk.Label(
    window, text="ULTIMATE KEYGEN", font=("Impact", 35), bg="black"
)
lbl_title.place(relx=0.5, rely=0.15, anchor="center")

# поле куда пишется сгенерированный ключ
lbl_key = tk.Label(
    window,
    text="XXXXX-XXXXX-XXXXX",
    font=("Consolas", 28, "bold"),
    bg="black",
    fg="white",
)
lbl_key.place(relx=0.5, rely=0.45, anchor="center")

# кнопка запуска генерации
btn_generate = tk.Button(
    window,
    text="GENERATE",
    font=("Arial", 16, "bold"),
    bg="red",
    fg="black",
    command=clicked,
)
btn_generate.place(relx=0.5, rely=0.75, anchor="center")

# запускаем переливание цветов
animate_title()

# держим окно открытым
window.mainloop()