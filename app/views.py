from app import app, auth, db
from flask import render_template, url_for, request, make_response, jsonify, session, send_file



# def login_is_required(function):
#     def wrapper(*args, **kwargs):
#         if 'user' not in session:
#             return render_template('index.html')
#         else:
#             return function()
#     return wrapper


@app.route('/')
# @login_is_required
def home():
    if 'user' in session:
        user_email = session['user']['email']
        return render_template('new_dashboard.html', user_email=user_email)
    return render_template('index.html')

    user_email = session['user']['email']

    return render_template('new_dashboard.html', user_email=user_email)