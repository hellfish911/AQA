"""
This module processes a text excerpt for 'Alice in wonderland'.

It performs various text manipulations and analyses, aimed at extracting
and counting specific elements within the text.
"""

# task 01: Split alice_in_wonderland into multiple lines
alice_in_wonderland = """
"Would you tell me, please, which way I ought to go from here?"
"That depends a good deal on where you want to get to," said the Cat.
"I don’t much care where ——" said Alice.
"Then it doesn’t matter which way you go," said the Cat.
"—— so long as I get somewhere," Alice added as an explanation.
"Oh, you’re sure to do that," said the Cat, "if you only walk long enough."
"""

# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
single_quotes = [char for char in alice_in_wonderland if char == "'"]
print(single_quotes)

# task 03 == Виведіть змінну alice_in_wonderland на друк
print(alice_in_wonderland)

# Задачі 04 -10:
# Переведіть задачі з книги "Математика, 5 клас"
# на мову пітон і виведіть відповідь, так, щоб було
# зрозуміло дитині, що навчається в п'ятому класі

# task 04

# Площа Чорного моря становить 436 402 км2, а площа Азовського
# моря становить 37 800 км2. Яку площу займають Чорне та Азов-
# ське моря разом?

black_sea_area = 436402  # площа Чорного моря в км²
azov_sea_area = 37800    # площа Азовського моря в км²

total_area = black_sea_area + azov_sea_area
print(f'Чорне та Азовське моря разом займають {total_area} км².')

# task 05
# Мережа супермаркетів має 3 склади, де всього розміщено
# 375 291 товар. На першому та другому складах перебуває
# 250 449 товарів. На другому та третьому – 222 950 товарів.
# Знайдіть кількість товарів, що розміщені на кожному складі.

total_goods = 375291
goods_first_and_second = 250449
goods_second_and_third = 222950

# Знайдемо кількість товарів на другому складі:
goods_second = (
    goods_first_and_second
    + goods_second_and_third
    - total_goods
) // 2

# Тепер знайдемо кількість товарів на першому та третьому складах:
goods_first = goods_first_and_second - goods_second
goods_third = goods_second_and_third - goods_second

print(f'На першому складі {goods_first} товарів.')
print(f'На другому складі {goods_second} товарів.')
print(f'На третьому складі {goods_third} товарів.')

# task 06
# Михайло разом з батьками вирішили купити комп’ютер, ско-
# риставшись послугою «Оплата частинами». Відомо, що сплачу-
# вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
# вартість комп’ютера.

monthly_payment = 1179
months = 18  # 1.5 роки = 18 місяців

computer_price = monthly_payment * months
print(f"Вартість комп'ютера становить {computer_price} грн.")

# task 07
# Знайди остачу від діленя чисел:
# a) 8019 : 8     d) 7248 : 6
# b) 9907 : 9     e) 7128 : 5
# c) 2789 : 5     f) 19224 : 9

number_a = 8019
divisor_a = 8

number_b = 9907
divisor_b = 9

number_c = 2789
divisor_c = 5

number_d = 7248
divisor_d = 6

number_e = 7128
divisor_e = 5

number_f = 19224
divisor_f = 9

remainder_a = number_a % divisor_a
remainder_b = number_b % divisor_b
remainder_c = number_c % divisor_c
remainder_d = number_d % divisor_d
remainder_e = number_e % divisor_e
remainder_f = number_f % divisor_f

print(f'{number_a} : {divisor_a}, остача = {remainder_a}')
print(f'{number_b} : {divisor_b}, остача = {remainder_b}')
print(f'{number_c} : {divisor_c}, остача = {remainder_c}')
print(f'{number_d} : {divisor_d}, остача = {remainder_d}')
print(f'{number_e} : {divisor_e}, остача = {remainder_e}')
print(f'{number_f} : {divisor_f}, остача = {remainder_f}')

# task 08
# Іринка, готуючись до свого дня народження, склала список того,
# що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
# для даного її замовлення.
# Назва товару    Кількість   Ціна
# Піца велика     4           274 грн
# Піца середня    2           218 грн
# Сік             4           35 грн
# Торт            1           350 грн
# Вода            3           21 грн

big_pizza_price = 274
medium_pizza_price = 218
juice_price = 35
cake_price = 350
water_price = 21

# Кількість товарів:
big_pizza_qty = 4
medium_pizza_qty = 2
juice_qty = 4
cake_qty = 1
water_qty = 3

total_cost = (big_pizza_price * big_pizza_qty +
              medium_pizza_price * medium_pizza_qty +
              juice_price * juice_qty +
              cake_price * cake_qty +
              water_price * water_qty
              )
print(f'Для замовлення Іринці потрібно {total_cost} грн.')

# task 09
# Ігор займається фотографією. Він вирішив зібрати всі свої 232
# фотографії та вклеїти в альбом. На одній сторінці може бути
# cрозміщено щонайбільше 8 фото. Скільки сторінок знадобиться
# Ігорю, щоб вклеїти всі фото?

total_photos = 232
photos_per_page = 8

pages_needed = (total_photos + photos_per_page - 1) // photos_per_page
print(f'Ігорю знадобиться {pages_needed} сторінок для всіх фото.')

# task 10
# Родина зібралася в автомобільну подорож із Харкова в Буда-
# пешт. Відстань між цими містами становить 1600 км. Відомо,
# що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
# становить 48 літрів.
# 1) Скільки літрів бензину знадобиться для такої подорожі?
# 2) Скільки щонайменше разів родині необхідно заїхати на зап-
# равку під час цієї подорожі, кожного разу заправляючи пов-
# ний бак?

distancekm = 1600
fuelper100km = 9
tankcapacity = 48

# 1. Скільки літрів бензину знадобиться:
fuelneeded = (distancekm / 100) * fuelper100km
print(f'Для подорожі знадобиться {fuelneeded} літрів бензину.')

# 2. Скільки разів треба заправитись:
stopsneeded = (fuelneeded + tankcapacity - 1) // tankcapacity
print(f'Родина має заїхати на заправку {stopsneeded} разів.')
