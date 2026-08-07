# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
alice_in_wonderland = '\"Would you tell me, please, which way I ought to go from here?\"\n\"That depends a good deal on where you want to get to,\" said the Cat.\n\"I don\'t much care where ——\" said Alice.\n\"Then it doesn\'t matter which way you go,\" said the Cat.\n\"—— so long as I get somewhere,\" Alice added as an explanation.\n\"Oh, you\'re sure to do that,\" said the Cat, "if you only walk long enough."'
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
print("Відображення символу одинарної лапки (') у тексті")
for alice in alice_in_wonderland:
    if alice == "'":
        print(alice)
# task 03 == Виведіть змінну alice_in_wonderland на друк
print(alice_in_wonderland)



"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
black_sea_square = 436492
azov_sea_square = 37800
total_square = black_sea_square + azov_sea_square
print(f' Чорне та Азовське моря разом займають площу {total_square} км2')


# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
total_items_warehouses = 375291
items_warehouse1_warehouse2 = 250449
items_warehouse2_warehouse3 = 222950

items_warehouse1 = total_items_warehouses - items_warehouse2_warehouse3
items_warehouse2 = items_warehouse1_warehouse2 - items_warehouse1
items_warehouse3 = items_warehouse2_warehouse3 - items_warehouse2
print(f' На першому складі розміщено {items_warehouse1} товарів, на другому - {items_warehouse2}, на третьому - {items_warehouse3}')


# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""

per_month = 1179
time_years = 1.5
time_months = 1.5 * 12
cost = per_month * time_months
print(time_months, cost)


# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
a = 8019 % 8
b = 9907 % 9
c = 2789 % 5
d = 7248 % 6
e = 7128 % 5
f = 19224 % 9
print(f'Відповіді до задачі. Залишок від ділення a) 8019 : 8 = {a}, b) 9907 : 9 = {b}, c) 2789 : 5 = {c}, '
      f'd) 7248 : 6 = {d}, 7128 : 5 = {e}, f) 19224 : 9 = {f}')


# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""

pizza_big = 4 * 274
pizza_middle = 2 * 218
juice = 4 * 35
cake = 1 * 350
soda = 3 * 21
costs = pizza_big + pizza_middle + juice + cake + soda
print(f'Для замовлення знадобиться {costs} грн')


# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""

photo = 232
per_page = 8
modulo = photo % per_page
if modulo == 0:
    pages = photo//per_page
else:
    pages = photo//per_page+1
print(pages, photo/per_page)


# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""

distance = 1600
fuel_per_100 = 9
tank = 48
liters = distance / 100 * fuel_per_100
count_refuel = int(liters / tank)-1
print(f'Для подорожі знадобиться {liters} літрів бензину. \nЗа умови, що поїздка почалась з повним баком, родині необхідно зупинитись {count_refuel} раз(и/ів)')
