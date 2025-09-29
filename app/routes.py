from flask import Blueprint, render_template, request
from werkzeug.security import generate_password_hash 

main_bp = Blueprint('main_bp', __name__)

@main_bp.route('/', methods=['GET', 'POST'])
def home():
    hello = "Hello, World! Hello _Flask!"
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        
        password_hash = generate_password_hash(password)
        
        print(f"Name: {name}, Email: {email}, Password: {password_hash}")  
    
    return render_template('index.html', hello=hello)
