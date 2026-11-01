from database import get_connection

def create_table():
    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute("""
    CREATE TABLE IF NOT EXISTS products(
        id SERIAL PRIMARY KEY,
        name VARCHAR(150),
        category VARCHAR(50),
        animal_type VARCHAR(50),
        price DECIMAL(10,2),
        quantity  INTEGER
    );
                       
        """)

        connection.commit()
        print("Products table created successfully!")

    finally:
        cursor.close()
        connection.close()

def add_product(name, category, animal_type, price, quantity):
    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute(
            "INSERT INTO products (name, category, animal_type, price, quantity) VALUES (%s, %s, %s, %s, %s)",
            (name, category, animal_type, price, quantity)
        )
        connection.commit()

    finally:
        cursor.close()
        connection.close()

def get_products():
    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute("SELECT * FROM products")
        products = cursor.fetchall()
        return products

    finally:
        cursor.close()
        connection.close()

def update_product(product_id, price, quantity):
    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute(
            "UPDATE products SET price = %s, quantity = %s WHERE id = %s",
            (price, quantity, product_id)
        )
        connection.commit()

    finally:
        cursor.close()
        connection.close()

def delete_product(product_id):
    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute(
            "DELETE FROM products WHERE id = %s",
            (product_id,)
        )
        connection.commit()

    finally:
        cursor.close()
        connection.close()


if __name__ == "__main__":
    delete_product(1)
    print(get_products())