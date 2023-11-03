import sqlite3
import bcrypt


class CryptoWalletDatabase:
    def __init__(self, db_name):
        self.conn = None
        self.cursor = None
        self.db_name = db_name

    def connect(self):
        try:
            self.conn = sqlite3.connect(self.db_name)
            self.cursor = self.conn.cursor()
            print(f'Успешное подключение к базе данных.')
        except sqlite3.Error as e:
            print(f"Ошибка при подключении к базе данных: {e}.")

    def disconnect(self):
        if self.conn:
            self.conn.close()
            print(f'Отключение от базы {self.db_name} выполнено.')
        else:
            print(f'Нет активного соединения с базой данных {self.db_name}.')

    def get_user_data(self, user_id, columns):
        query = f"SELECT {', '.join(columns)} FROM Users WHERE user_id = ?"
        return self.execute_query(query, (user_id,))

    def create_table(self, table_name, columns):
        columns_str = ', '.join(columns)
        create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_str})"
        self.execute_query(create_table_query)

        username, password, email, wallet_id = user_data
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        insert_query = "INSERT INTO Users (username, password, email, wallet_id) VALUES (?, ?, ?, ?)"
        self.execute_query(insert_query, (username, hashed_password, email, wallet_id))

    def insert_user_data(self, user_data):
        user_name, users_email, user_pasword, name, surname, middle_name = user_data
        user_pasword = bcrypt.hashpw(user_pasword.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        insert_query = "INSERT INTO users (user_name, users_email, user_pasword, name, surname, middle_name) VALUES (?, ?, ?, ?,?,?)"
        self.execute_query(insert_query, (user_name, users_email, user_pasword, name, surname, middle_name))
        self.create_wallet([0, 0, 0, 0, 0])

    def get_wallet_data(self, user_id, wallet_id):
        query = "SELECT wallet_name, balance, currency FROM Wallets WHERE user_id = ? AND wallet_id = ?"
        return self.execute_query(query, (user_id, wallet_id))

    def create_wallet(self, wallet_data):
        insert_query = "INSERT INTO Wallets (RUB, EUR, USD, BTC,ETH) VALUES (?, ?, ?, ?, ?)"
        self.execute_query(insert_query, wallet_data)

    def get_transactions(self, wallet_id):
        query = "SELECT transaction_id, transaction_type, amount, timestamp, description FROM Transactions WHERE wallet_id = ?"
        return self.execute_query(query, (wallet_id,))

    def add_transaction(self, transaction_data):
        insert_query = "INSERT INTO Transactions (wallet_id, transaction_type, amount, timestamp, description) VALUES (?, ?, ?, ?, ?)"
        self.execute_query(insert_query, transaction_data)

    def check_user_exists(self, user_name, users_email):
        query = "SELECT users_id FROM users WHERE user_name = ? OR users_email = ?"
        result = self.execute_query(query, (user_name, users_email))
        print(result)
        return bool(result)

    def verify_user_credentials(self, username, password):
        query = "SELECT users_id, user_pasword FROM users WHERE user_name = ?"
        result = self.execute_query(query, (username,))
        if result:
            print("result")
            user_id, hashed_password = result[0]
            if bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8')):
                return user_id
        return None

    def execute_query(self, query, data=None):
        try:
            if data:
                self.cursor.execute(query, data)
            else:
                self.cursor.execute(query)
            self.conn.commit()
            print('Запрос успешно выполнен.')
            return self.cursor.fetchall()  # Добавьте эту строку для получения результата запроса
        except sqlite3.Error as e:
            print(f"Ошибка при выполнении запроса: {e}.")
            return None

    def check_nick(self, user_name):
        query = "SELECT users_id FROM users WHERE user_name = ?"
        result = self.execute_query(query, (user_name,))
        print(result)
        return bool(result)

    def all_maney(self, id):
        query = "SELECT * FROM wallets WHERE users_id = ?"
        result = self.execute_query(query, (id,))
        print(result)
        return result

    def deposit_rub(self, id, count):
        query = "UPDATE wallets SET RUB=? WHERE users_id = ?"
        self.execute_query(query, (count, id))