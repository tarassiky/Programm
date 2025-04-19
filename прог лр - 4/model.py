# model.py
import requests
from xml.etree import ElementTree as ET
from datetime import datetime


class CurrencyRates:
    _instance = None

    def __new__(cls, currencies=None):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.currencies = currencies or ["USD", "EUR", "GBP"]
            cls._instance.rates = {}
            cls._instance.fetch_rates()
        return cls._instance

    def fetch_rates(self):
        try:
            response = requests.get("https://www.cbr.ru/scripts/XML_daily.asp")
            if response.status_code == 200:
                root = ET.fromstring(response.content)
                self.rates = {'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
                for valute in root.findall('Valute'):
                    code = valute.find('CharCode').text
                    if code in self.currencies:
                        value = float(valute.find('Value').text.replace(',', '.'))
                        nominal = int(valute.find('Nominal').text)
                        self.rates[code] = round(value / nominal, 4)
            return True
        except Exception as e:
            print(f"Error fetching rates: {e}")
            return False

    def get_rates(self):
        return self.rates

    def set_currencies(self, currencies):
        self.currencies = currencies
        self.fetch_rates()