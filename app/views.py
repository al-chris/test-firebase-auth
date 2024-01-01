from app import app, auth, db, login_required
from flask import render_template, url_for, request, make_response, jsonify, session, send_file, redirect, flash



@app.route('/home')
@login_required
def home():
    # if 'user' in session:
    #     user_email = session['user']['email']
    #     return render_template('new_dashboard.html', user_email=user_email)
    # return render_template('index.html')

    user_email = session['user']['email']

    return render_template('new_dashboard.html', user_email=user_email)


@app.route('/')
def landing():
    return render_template('index.html')


@app.route('/error')
def error():
    return render_template('error.html')