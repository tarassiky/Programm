# controllers/currency_controller.py
import sqlite3
from flask import render_template
from model import CurrencyRates


class CurrencyController:
    def __init__(self):
        self.model = CurrencyRates()
        self.init_db()

    def init_db(self):
        with sqlite3.connect('currency.db') as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS rates (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    currency TEXT NOT NULL,
                    rate REAL NOT NULL,
                    date TEXT NOT NULL
                )
            ''')
            conn.commit()

    def save_rates(self, rates):
        with sqlite3.connect('currency.db') as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM rates")
            for currency, rate in rates.items():
                if currency != 'date':
                    cursor.execute(
                        "INSERT INTO rates (currency, rate, date) VALUES (?, ?, ?)",
                        (currency, rate, rates['date'])
                    )
            conn.commit()

    def get_rates_view(self):
        rates = self.model.get_rates()
        self.save_rates(rates)
        return render_template('index.html', rates=rates)

    def update_currencies(self, currencies):
        self.model.set_currencies(currencies)
        return self.get_rates_view()