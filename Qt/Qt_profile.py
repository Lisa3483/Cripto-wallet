from BD.DataBase import CryptoWalletDatabase
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5.QtGui import QPixmap
import requests


class Profile(QMainWindow):
    def __init__(self, id, other):
        super().__init__()
        uic.loadUi('ui_files\\profil.ui', self)
        self.db = CryptoWalletDatabase("BD\\DataBase")
        self.setWindowTitle('Профиль пользователя')
        self.id = id
        self.db.connect()
        self.Money_set()
        self.Ui_comp()
        self.get_curs()

    def Money_set(self):
        result = list(self.db.all_maney(self.id)[0])

        self.RUB_count.setText(str(result[1]))
        self.USDT_count.setText(str(result[3]))
        self.EUR_count.setText(str(result[2]))
        self.BTC_count.setText(str(result[4]))
        self.ETH_count.setText(str(result[5]))
        self.goout.clicked.connect(self.close_prof)

    def Ui_comp(self):
        self.deposit.clicked.connect(self.deposit_btn)
        self.update.clicked.connect(self.update_btn)
        btc = QPixmap('image\\btc.png')
        self.Btcpix.setPixmap(btc)
        rub = QPixmap('image\\rub.png')
        self.Rubpix.setPixmap(rub)
        dol = QPixmap('image\\dol.png')
        self.Usdtpix.setPixmap(dol)

    def deposit_btn(self):
        print(1)
        result = list(self.db.all_maney(self.id)[0])[1]

        self.db.deposit_rub(self.id, 100 + float(result))

    def update_btn(self):
        self.Money_set()
        self.get_curs()

    def close_prof(self):
        self.close()

    def get_curs(self):

        exchange_rates = self.get_exchange_rates()
        print("API Response:", exchange_rates)
        if exchange_rates:
            rub_to_usd = exchange_rates.get("rub", {}).get("usd", "N/A")

            eur_to_usd = exchange_rates.get("eur", {}).get("usd", "N/A")
            bitcoin_to_usd = exchange_rates.get("bitcoin", {}).get("usd", "N/A")
            ethereum_to_usd = exchange_rates.get("ethereum", {}).get("usd", "N/A")
            self.label_6.setText(str(rub_to_usd))
            self.label_9.setText(str(1.0))
            self.label_14.setText(str(eur_to_usd))
            self.label_19.setText(str(bitcoin_to_usd))
            self.label_24.setText(str(ethereum_to_usd))
        else:
            print("Не удалось получить данные о курсах.")

    def get_exchange_rates(self):
        url = "https://api.coingecko.com/api/v3/simple/price"
        params = {
            "ids": "rub,usd,eur,bitcoin,ethereum",
            "vs_currencies": "usd"
        }

        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return None


def start_profile():
    prof = Profile()
    prof.show()
