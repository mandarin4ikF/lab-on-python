import csv
import random
# minidom - модуль для работы с XML через модель DOM 
# DOM превращает весь XML-документ в «дерево» объектов 
import xml.dom.minidom as minidom

file = open('books-en.csv', encoding='latin-1')

# csv.DictReader читает первую строку файла как имена столбцов
# а каждую строку данных превращает в словарь: {Book-Title: ..., Price: ...}
books = list(csv.DictReader(file, delimiter=';'))
file.close()

# считаем сколько названий длиннее 30 символов
ans1 = 0
for b in books:
    if len(b['Book-Title']) > 30:
        ans1 = ans1 + 1
print('1)', ans1)

# поиск по автору с ценой до 150
author = input('2) Автор (например Rowling): ').lower()
for b in books:
    raw_price = b['Price'].replace(',', '.')
    price = float(raw_price)
    
    if author in b['Book-Author'].lower():  # берем автора по ключу и делаем буквы строчными
        if price <= 150:
            print(b['Book-Author'], '-', b['Book-Title'], f'({price} руб.)')

# сохраняем 20 случайных книг в файл
f = open('result.txt', 'w', encoding='utf-8')
for i in range(20):
    # random.choice(books) выбирает ровно один случайный элемент из переданного списка
    b = random.choice(books)
    year = b['Year-Of-Publication']
    f.write(f"{i + 1}. {b['Book-Author']}. {b['Book-Title']} - {year}\n")
f.close()
print('3) result.txt готов')


# minidom.parse(...) открывает XML-файл считывает его синтаксис и строит в памяти DOM дерево 
dom = minidom.parse('currency.xml')
res = {}

# dom.getElementsByTagName('Valute') ищет по всему XML-дереву ВСЕ теги с именем <Valute> 
for v in dom.getElementsByTagName('Valute'):
    # v.getElementsByTagName('Name'): ищет тег <Name> уже только ВНУТРИ конкретного блока <Valute>
    # [0] берем первый (и единственный) найденный элемент
    # .firstChild: достает текст <Name>Текст</Name> между тегами
    # .data: извлекает саму строчку с текстом из этого узла
    name = v.getElementsByTagName('Name')[0].firstChild.data
    val = v.getElementsByTagName('Value')[0].firstChild.data

    res[name] = float(val.replace(',', '.'))

print('4)', res)


# ДОПЗАДАНИЕ 1
# Издательства без повторений
publishers = set()
for b in books:
    publishers.add(b['Publisher'])

print('Доп 1) Уникальных издательств:', len(publishers))
# покажем первые 10 для наглядности в консоли
print('Примеры издательств:', list(publishers)[:10])


# ДОПЗАДАНИЕ 2 
# Самые популярные 20 книг
def get_downloads(book):
    return int(book['Downloads']) # переводим в int для правильной сортировки чисел

top_20 = sorted(books, key=get_downloads, reverse=True)[:20]

print('Доп 2) Топ-20 популярных книг:')
for i in range(20):
    book = top_20[i]
    print(f"{i + 1}. {book['Book-Title']} (скачиваний: {book['Downloads']})")