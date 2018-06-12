from flask import request, jsonify, render_template

from src import app
from src.auth.forms import LoginForm


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':

        if form.validate_on_submit():
            return jsonify(success=True)
        else:
            errors = form.errors.items()
            return render_template('auth/login.html', form=form, errors=errors)

    return render_template('auth/login.html', form=form)