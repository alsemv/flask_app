from src import app


@app.route('/login', methods=['GET', 'POST'])
def login():
    return "login page"