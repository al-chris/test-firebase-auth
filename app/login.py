from app import app, auth
from flask import request, render_template, session, redirect, url_for

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        try:
            # Sign in with email and password

            login = auth.sign_in_with_email_and_password(email, password)
            
            # Store user information in the session
            session['user'] = {'email': login['email'], 'uid': login['localId']}

            return redirect(url_for('home'))

        except Exception as e:
            print(e)
            return render_template("error.html")

    return render_template('login.html')  # Create an HTML template for the login form
