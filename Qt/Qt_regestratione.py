import sys
from BD.DataBase import CryptoWalletDatabase
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton


class Regestration(QMainWindow):
    def __init__(self, other):
        super().__init__()
        uic.loadUi('ui_files\\regestratoine_window.ui', self)
        self.db = CryptoWalletDatabase("BD\\DataBase")
        self.setWindowTitle('Регестрация в систему')
        self.db.connect()
        self.other = other
        self.regestratione.clicked.connect(self.regestratione_btn)
        self.back.clicked.connect(self.close_entr)
        self.back.clicked.connect(self.close_entr)
        self.check_nick.clicked.connect(self.check_nick_btn)

        self.show()

    def close_entr(self):
        self.close()

    def check_nick_btn(self):
        if self.db.check_nick(self.nick.text):
            print('Такое имя занято.')
        else:
            print('Такое имя свободно.')

    def regestratione_btn(self):
        if self.db.check_user_exists(self.nick.text(), self.mail.text()):
            print("Пользователь с таким именем или email уже существует.")
        else:

            self.db.insert_user_data((self.nick.text(), self.mail.text(), self.passw.text(),
                                      self.name.text(), self.Sname.text(), self.mname.text()))
            print("Регистрация выполнена успешно.")
            id = self.db.verify_user_credentials(self.nick.text(), self.passw.text())
            self.other.start_profile(id)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget_wallet = Regestration()
    widget_wallet.show()
    sys.exit(app.exec())
