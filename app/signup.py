from app import app, auth
from flask import request, render_template, session, redirect, url_for


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        try:
            # Create a new user with email and password
            user = auth.create_user_with_email_and_password(
                email=email,
                password=password
            )

            # Store user information in the session
            session['user'] = {'email': user['email'], 'uid': user['localId']}

            return redirect(url_for('home'))

        except Exception as e:
            print(e)
            return 'Signup failed.'

    return render_template('signup.html')  # Create an HTML template for the signup form
