#products - id, name, category_id, price, discription, is_active, valid_from, valid_to
#categories - id, name, description

import sqlite3

connection = sqlite3.connect("shop.db")
cursor = connection.cursor()

def create_table():
    try:
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY,
            name VARCHAR(30),
            description VARCHAR(100)
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            name VARCHAR(30),
            category_id INTEGER,
            price REAL,
            description VARCHAR(100),
            is_active INTEGER,
            valid_from TEXT,
            valid_to TEXT,
            FOREIGN KEY (category_id) REFERENCES categories(id)
        )
        """)
        connection.commit()
        print("✓ Tables created successfully")
    except sqlite3.Error as error:
        print(f"✗ Error creating tables: {error}")



def insert_into_db():
    try:
        cursor.execute("""
        INSERT OR IGNORE INTO categories (id, name, description)
            VALUES
            (1, 'Cat Food', 'Food for cats'),
            (2, 'Dog Food', 'Food for dogs'),
            (3, 'Cat Toys', 'Toys for cats'),
            (4, 'Dog Toys', 'Toys for dogs'),
            (5, 'Care', 'Pet care products');
        """)

        cursor.execute("""
        INSERT OR IGNORE INTO products
        (id, name, category_id, price, description, is_active, valid_from, valid_to)
        VALUES
        (1, 'Royal Canin Cat Food', 1, 25.99, 'Dry food for cats', true, '2026-01-01', NULL),
        (2, 'Purina Cat Chow', 1, 18.50, 'Balanced cat food', true, '2026-01-01', NULL),
        (3, 'Brit Care Cat', 1, 22.75, 'Premium food for cats', true, '2026-02-01', NULL),
        (4, 'Royal Canin Dog Food', 2, 32.99, 'Dry food for dogs', true, '2026-01-01', NULL),
        (5, 'Pedigree Adult', 2, 19.90, 'Food for adult dogs', true, '2026-01-01', NULL),
        (6, 'Brit Premium Dog', 2, 27.50, 'Premium dog food', true, '2026-02-01', NULL),
        (7, 'Cat Ball', 3, 5.99, 'Small ball for cats', true, '2026-01-15', NULL),
        (8, 'Feather Wand', 3, 8.50, 'Interactive feather toy', true, '2026-01-15', NULL),
        (9, 'Cat Scratching Toy', 3, 15.99, 'Scratching toy for cats', true, '2026-03-01', NULL),
        (10, 'Dog Rope Toy', 4, 9.99, 'Rope toy for dogs', true, '2026-01-10', NULL),
        (11, 'Rubber Ball', 4, 7.50, 'Durable ball for dogs', true, '2026-01-10', NULL),
        (12, 'Dog Frisbee', 4, 12.99, 'Flying disc for dogs', false, '2026-01-10', '2026-09-01'),
        (13, 'Cat Shampoo', 5, 11.99, 'Gentle shampoo for cats', true, '2026-02-15', NULL),
        (14, 'Dog Shampoo', 5, 13.50, 'Shampoo for dogs', true, '2026-02-15', NULL),
        (15, 'Pet Nail Clippers', 5, 6.99, 'Nail clippers for pets', false, '2026-01-01', '2026-08-01');
        """)
        connection.commit()
    except sqlite3.Error as error:
        print(f"✗ Error inserting date: {error}")

def select_join_data():
    try:
        cursor.execute("""
        SELECT
            c.name AS category_name,
            p.*  
        FROM products p
        JOIN categories c
            ON c.id = p.category_id
        """)
        return cursor.fetchall()
    except sqlite3.Error as error:
        print(f"✗ Error selecting date: {error}")

create_table()
insert_into_db()
products = select_join_data()

print("Сategory_name | Product ID | Product Name | Сategory_id | Price | Description, Is_active, Valid_from, Valid_to")
print("-" * 60)

for product in products:
    print(product)

connection.close()

