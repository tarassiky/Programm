from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from currency_model import CurrencyDataManager
from currency_controller import register_routes

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///currency_data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class CurrencyRecord(db.Model):
    id = db.Column(db.String(3), primary_key=True)
    value = db.Column(db.Float, nullable=False)
    updated_at = db.Column(db.String(20), default="")

with app.app_context():
    db.create_all()
    currency_manager = CurrencyDataManager(db, CurrencyRecord)
    register_routes(app, db, CurrencyRecord, currency_manager)

if __name__ == '__main__':
    app.run(debug=True)