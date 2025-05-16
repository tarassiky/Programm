import requests
from bs4 import BeautifulSoup
from datetime import datetime


class CurrencyDataManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, db=None, model=None):
        if not hasattr(self, 'initialized'):
            self.db = db
            self.model = model
            self.tracked_currencies = ['USD', 'EUR', 'GBP']
            self.initialized = True
            self.load_currency_data()

    def load_currency_data(self):
        try:
            response = requests.get('https://www.cbr.ru/scripts/XML_daily.asp')
            response.raise_for_status()

            currency_data = BeautifulSoup(response.text, 'xml')
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M")

            for item in currency_data.find_all('Valute'):
                code = item.CharCode.text
                if code in self.tracked_currencies:
                    rate = float(item.Value.text.replace(',', '.'))
                    self._save_currency_rate(code, rate, current_time)
        except Exception as e:
            print(f"Ошибка загрузки данных: {e}")

    def _save_currency_rate(self, code, rate, timestamp):
        try:
            record = self.model.query.get(code)
            if record:
                record.value = rate
                record.updated_at = timestamp
            else:
                new_record = self.model(id=code, value=rate, updated_at=timestamp)
                self.db.session.add(new_record)
            self.db.session.commit()
        except Exception as e:
            print(f"Ошибка сохранения данных: {e}")
            self.db.session.rollback()

    def get_currency_rates(self):
        return {record.id: {'value': record.value, 'datetime': record.updated_at}
                for record in self.model.query.all()
                if record.id in self.tracked_currencies}

    def update_currency_list(self, currencies):
        valid_currencies = [c.strip().upper() for c in currencies if len(c.strip()) == 3]
        if not valid_currencies:
            raise ValueError("Необходимо указать минимум одну валюту")

        self.tracked_currencies = valid_currencies
        self.load_currency_data()

    def refresh_single_rate(self, currency_code):
        if currency_code in self.tracked_currencies:
            self.load_currency_data()
            return True
        return False

    def remove_currency(self, currency_code):
        record = self.model.query.get(currency_code)
        if record:
            self.db.session.delete(record)
            self.db.session.commit()
            if currency_code in self.tracked_currencies:
                self.tracked_currencies.remove(currency_code)
            return True
        return False