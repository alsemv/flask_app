from flask import Blueprint, render_template, jsonify, app
from src.users.user import User

recipient_blueprint = Blueprint('recipient', __name__, url_prefix='/recipient')


@recipient_blueprint.route('/')
def index():
    pass


@recipient_blueprint.route('/list')
def recipients_list():
    user = User.query.filter_by(id=1).first()
    recipients = user.recipients

    results = [recipient.serialize() for recipient in recipients]
    return jsonify(results)

