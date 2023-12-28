from app import app, auth, db
from flask import render_template, url_for, request, make_response, jsonify, session, send_file



@app.route('/')
def home():
    if 'user' in session:
        user_email = session['user']['email']
        return render_template('dashboard.html', user_email=user_email)
    return render_template('index.html')