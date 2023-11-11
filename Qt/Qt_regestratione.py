import sys
from BD.DataBase import CryptoWalletDatabase
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
import smtplib
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Regestration(QMainWindow):
    def __init__(self, other):
        super().__init__()
        uic.loadUi('ui_files\\regestratoine_window.ui', self)
        self.db = CryptoWalletDatabase("BD\\DataBase")
        self.setWindowTitle('Регестрация в систему')
        self.code_m = None
        self.db.connect()
        self.other = other
        self.Ui_comp()
        # self.show()

    def Ui_comp(self):
        self.back.clicked.connect(self.close_entr)
        self.regestratione.clicked.connect(self.regestratione_btn)
        self.check_nick.clicked.connect(self.check_nick_btn)
        self.send_code.clicked.connect(self.send_code_btn)

    def send_code_btn(self):
        def generate_verification_code():
            return str(random.randint(1000, 9999))

        smtp_server = 'smtp.gmail.com'
        smtp_port = 587
        smtp_username = 'egorovicegorka87@gmail.com'
        smtp_password = 'igqm jnya yvzw xtpb'

        recipient_email = str(self.mail.text())

        self.code_m = generate_verification_code()

        msg = MIMEMultipart()
        msg['From'] = smtp_username
        msg['To'] = recipient_email
        msg['Subject'] = 'Код подтверждения'

        message = f'Ваш код подтверждения: {self.code_m}'
        msg.attach(MIMEText(message, 'plain'))

        try:
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(smtp_username, recipient_email, msg.as_string())
            server.quit()
            print("Письмо с кодом подтверждения отправлено успешно.")
        except Exception as e:
            print("Ошибка при отправке письма: ", str(e))

    def close_entr(self):
        self.close()

    def check_nick_btn(self):
        if self.db.check_user_exists(self.nick.text, ''):
            print('Такое имя занято.')
        else:
            print('Такое имя свободно.')

    def regestratione_btn(self):
        if self.code_m is not None and str(self.code_m) == str(self.code.text()):
            if self.db.check_user_exists(self.nick.text(), self.mail.text()):
                print("Пользователь с таким именем или email уже существует.")
            else:

                self.db.insert_user_data((self.nick.text(), self.mail.text(), self.passw.text(),
                                          self.name.text(), self.Sname.text(), self.mname.text()))
                print("Регистрация выполнена успешно.")
                id = self.db.verify_user_credentials(self.nick.text(), self.passw.text())
                self.other.start_profile(id)
        else:
            print('Неверный код')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget_wallet = Regestration()
    widget_wallet.show()
    sys.exit(app.exec())
