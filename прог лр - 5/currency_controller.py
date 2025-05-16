from flask import render_template, request, redirect, url_for, flash


def register_routes(app, db, model, currency_manager):
    @app.route('/', methods=['GET', 'POST'])
    def index():
        error_message = None
        if request.method == 'POST':
            try:
                currencies = request.form['currencies'].split(',')
                currency_manager.update_currency_list(currencies)
            except ValueError as e:
                error_message = str(e)

        rates = currency_manager.get_currency_rates()
        return render_template(
            'index.html',
            rates=rates,
            currency_rates=currency_manager,
            error_message=error_message
        )

    @app.route('/update/<currency_id>', methods=['GET', 'POST'])
    def update(currency_id):
        if request.method == 'POST':
            if currency_manager.refresh_single_rate(currency_id):
                flash("Курс успешно обновлен", "success")
            return redirect(url_for('index'))
        return render_template('update.html', currency_id=currency_id)

    @app.route('/delete/<currency_id>', methods=['POST'])
    def delete(currency_id):
        if not currency_manager.remove_currency(currency_id):
            flash("Не удалось удалить валюту", "error")
        return redirect(url_for('index'))

    @app.route('/set_currencies', methods=['POST'])
    def set_currencies():
        try:
            currencies = request.form['currencies'].split(',')
            currency_manager.update_currency_list(currencies)
        except ValueError as e:
            flash(str(e), "error")
        return redirect(url_for('index'))