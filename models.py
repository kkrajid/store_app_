# server/models.py

import sqlite3

class Database:
    def __init__(self, db_name='ecommerce.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def execute_query(self, query, params=()):
        self.cursor.execute(query, params)
        self.conn.commit()

    def fetch_query(self, query, params=()):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()

class Product:
    @staticmethod
    def create_table():
        db = Database()
        db.execute_query('''
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                price REAL NOT NULL,
                description TEXT
            )
        ''')
        db.close()

    @staticmethod
    def select_all():
        db = Database()
        result = db.fetch_query('SELECT * FROM products')
        db.close()
        return result

    @staticmethod
    def select_by_id(product_id):
        db = Database()
        result = db.fetch_query('SELECT * FROM products WHERE id = ?', (product_id,))
        db.close()
        return result[0] if result else None

    @staticmethod
    def add_product(name, price, description):
        db = Database()
        try:
            db.execute_query('INSERT INTO products (name, price, description) VALUES (?, ?, ?)', (name, price, description))
            db.close()
            return True
        except sqlite3.Error as e:
            print(f"Error adding product: {e}")
            db.close()
            return False

if __name__ == '__main__':
    Product.create_table()
