from BD.DataBase import CryptoWalletDatabase
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton


class Entrance(QMainWindow):
    def __init__(self, other):
        super().__init__()
        uic.loadUi('ui_files\\entrance_window.ui', self)
        self.db = CryptoWalletDatabase("BD\\DataBase")
        self.setWindowTitle('Вход в систему')
        self.db.connect()
        self.entrance.clicked.connect(self.entrance_btn)
        self.back.clicked.connect(self.close_entr)
        self.other = other
        # self.show()

    def close_entr(self):
        self.close()

    def entrance_btn(self):
        id = self.db.verify_user_credentials(self.niname.text(), self.passw.text())
        if id:
            print(f"Вход выполнен успешно: {id}")
            self.other.start_profile(id)
        else:
            print("Неверный логин или пароль")
