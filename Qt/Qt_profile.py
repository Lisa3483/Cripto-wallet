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
        self.other = other
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

    def Ui_comp(self):
        self.deposit.clicked.connect(self.deposit_btn)
        self.update.clicked.connect(self.update_btn)
        self.goout.clicked.connect(self.close_prof)
        self.bringout.clicked.connect(self.bringout_btn)

        btc = QPixmap('image\\btc.png')
        self.Btcpix.setPixmap(btc)
        rub = QPixmap('image\\rub.png')
        self.Rubpix.setPixmap(rub)
        dol = QPixmap('image\\dol.png')
        self.Usdtpix.setPixmap(dol)

    def deposit_btn(self):
        self.other.start_deposit(self.id)

    def bringout_btn(self):
        self.other.start_bringout(self.id)

    def update_btn(self):
        self.Money_set()
        self.get_curs()

    def close_prof(self):
        self.close()

    def get_curs(self):

        rub_url = "https://www.cbr-xml-daily.ru/daily_json.js"
        rub_response = requests.get(rub_url)
        rub_data = rub_response.json()
        rub_rate = rub_data["Valute"]["USD"]["Value"]

        eur_url = "https://open.er-api.com/v6/latest/EUR"
        eur_response = requests.get(eur_url)
        eur_data = eur_response.json()
        eur_rate = eur_data["rates"]["USD"]

        self.label_6.setText(str(rub_rate))
        self.label_14.setText(str(eur_rate))
        crypto_url = "https://api.coingecko.com/api/v3/simple/price"
        params = {
            "ids": "bitcoin,ethereum",
            "vs_currencies": "usd"
        }
        crypto_response = requests.get(crypto_url, params=params)
        crypto_data = crypto_response.json()
        bitcoin_rate = crypto_data["bitcoin"]["usd"]
        ethereum_rate = crypto_data["ethereum"]["usd"]

        self.label_19.setText(str(bitcoin_rate))
        self.label_24.setText(str(ethereum_rate))
        self.label_9.setText(str(1.0))

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
