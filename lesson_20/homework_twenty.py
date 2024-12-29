"""This module creates database."""

import sqlite3

"""
Створіть базу даних для інтернет-магазину з наступними таблицями:
products: таблиця для зберігання інформації про продукти, включаючи назву, опис, ціну тощо.
categories: таблиця для категорій продуктів.
products повинна мати зовнішній ключ на таблицю categories.
Напишіть SQL-скрипт для створення зазначених таблиць.
Внесіть декілька рядків даних в кожну таблицю
Виконайте JOIN-запит, який повертає інформацію про продукти та назву їх категорій
"""

conn = sqlite3.connect('market.db')
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);
""")


cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    price REAL NOT NULL,
    category_id INTEGER NOT NULL,
    FOREIGN KEY (category_id) REFERENCES categories (id)
);
""")


cursor.executemany("""
INSERT INTO categories (name)
VALUES (?);
""", [
    ('Stuff',),
    ('Clothes',),
    ('Food',),
])


cursor.executemany("""
INSERT INTO products (name, description, price, category_id)
VALUES (?, ?, ?, ?);
""", [
    ('Country', 'Better with ice', 34.34, 1),
    ('Ground', 'For standing', 78.01, 2),
    ('Hotdog', 'Wurst howl', 1.99, 3),
])


cursor.execute("""
SELECT
    products.name AS product_name,
    products.description,
    products.price,
    categories.name AS category_name
FROM
    products
JOIN
    categories
ON
    products.category_id = categories.id;
""")


results_display = cursor.fetchall()
for row in results_display:
    print(
        f'Product: {row[0]}, '
        f'Description: {row[1]}, '
        f'Price: {row[2]}, '
        f'Category: {row[3]}',
    )

conn.commit()
conn.close()
