from flask import Blueprint, render_template, request

main_bp = Blueprint('main', __name__)

@main_bp.route('/', methods=['GET', 'POST'])
def home():
    hello = "Hello, World! Hello _Flask!"
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        
        print(f"Name: {name}, Email: {email}, Password: {password}")
    
    
    return render_template('index.html', hello=hello)
