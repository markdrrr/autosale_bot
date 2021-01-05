import datetime
import uuid
import pyqiwi
from data.config import WALLET_QIWI, QIWI_TOKEN, QIWI_PUBKEY

# from utils.db_api.qiwi import add_payment
wallet = pyqiwi.Wallet(token=QIWI_TOKEN, number=WALLET_QIWI)
from pyqiwi import generate_form_link


class NotEnoughMoney:
    pass


class NoPaymentFound(Exception):
    pass


class Payment:
    def __init__(self, amount=0, id=None):
        self.amount = amount
        self.id = id

    async def create(self):
        self.id = str(uuid.uuid4())
        # await add_payment(self.id, self.user_id, 0, 'qiwi')

    @staticmethod
    def check_payment(comment):
        start_date = datetime.datetime.now() - datetime.timedelta(days=2)
        transactions = wallet.history(start_date=start_date)
        transactions = transactions.get('transactions')
        for transaction in transactions:
            if transaction.comment:
                if str(comment) in transaction.comment:
                    amount = transaction.total.amount
                    return amount
        else:
            raise NoPaymentFound

    @property
    def link(self):
        # return f'https://oplata.qiwi.com/create?publicKey={QIWI_PUBKEY}&amount={self.amount}&comment={self.id}'
        return f'https://qiwi.com/payment/form/99?amountFraction=00&extra%5B%27account%27%5D=+{WALLET_QIWI}&extra%5B%27comment%27%5D={self.id}&'
