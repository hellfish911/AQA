# task 01 == Виправте синтаксичні помилки
print('Hello', end = '')
print('world!')

# task 02 == Виправте синтаксичні помилки
hello = 'Hello'
world = 'world'
print(f'{hello} {world}!')

# task 03  == Вcтавте пропущену змінну у ф-цію print
for letter in 'Hello world!':
    print(letter)

# task 04 == Зробіть так, щоб кількість бананів була
# завжди в чотири рази більша, ніж яблук
apples = 2
banana = apples * 4

# task 05 == виправте назви змінних
storona_one = 1
storona_two = 2
storona_three = 3
storona_four = 4

# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача
perimeter = storona_one + storona_two + storona_three + storona_four
print('Figure Perimeter:', perimeter)

"""
    # Задачі 07 -10:
    # Переведіть задачі з книги "Математика, 2 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в другому класі
"""
# task 07
"""
У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
Скільки всього дерев посадили в саду?
"""
yabluni = 4
grushi = yabluni + 5
slyvy = yabluni - 2
total_derev = yabluni + grushi + slyvy
print(f'Всього дерев у саду: {total_derev}')
# task 08
"""
До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""
temp_before = 5
temp_after = temp_before - 10
temp_evening = temp_after + 4
print(f'Температура надвечір: {temp_evening} градусів')
# task 09
"""
Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скількі сьогодні дітей у театральному гуртку?
"""
hlopchiki = 24
divchatka = hlopchiki // 2
hlopchiki_present = hlopchiki - 1
divchatka_present = divchatka - 2
total_children = hlopchiki_present + divchatka_present
print(f'Сьогодні в гуртку: {total_children} дітей')
# task 10
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""
price_first = 8
price_second = price_first + 2
price_third = (price_first + price_second) / 2
total_price = price_first + price_second + price_third
print(f'Вартість усіх книг: {total_price} грн.')
