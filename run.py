from src import app
from src.recipients.views import recipient_blueprint
from src.auth import views

app.register_blueprint(recipient_blueprint)
app.run(debug=app.config['DEBUG'], port=5000)