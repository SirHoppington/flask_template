from flask import Blueprint


general = Blueprint('login', __name__)

@login.route('/', methods=["GET"])
def index():
    return "Hello, World!"
