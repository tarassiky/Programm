# app.py
from flask import Flask
from controllers import CurrencyController

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

controller = CurrencyController()

@app.route('/')
def index():
    return controller.get_rates_view()

if __name__ == '__main__':
    app.run(debug=True)