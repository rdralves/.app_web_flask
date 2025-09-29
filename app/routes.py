from flask import Blueprint, render_template

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    hello = "Hello, World!/nHello _Flask!"
    return render_template('index.html', hello=hello)
