db.create_table("users", ["users_id  INTEGER PRIMARY KEY", "user_name TEXT", "users_email TEXT",
"user_pasword TEXT", "name TEXT", "surname TEXT", "middle_name TEXT"])
db.create_table("wallets", ["users_id  INTEGER PRIMARY KEY", "RUB REAL", "EUR REAL",
"USD REAL", "BTC REAL", "ETH REAL"])
# таблица базы данных

#main
from DataBase import CryptoWalletDatabase

db = CryptoWalletDatabase("DataBase")
db.connect()

username = "user123"
email = "user123@example.com"
if db.check_user_exists(username, email):
    print("Пользователь с таким именем или email уже существует.")
else:
    password = "password123"
    name = "sdfsdf"
    surname = "12345"
    middlename = "yrhfbv"
    db.insert_user_data((username, email, password, name, surname, middlename))
    print("Регистрация выполнена успешно.")

db.disconnect()