from app import app
from flask import render_template, url_for, request, make_response, jsonify, session, send_file



@app.get('/')
def home():
    if 'user' in session:
        user_email = session['user']['email']
        return render_template('dashboard.html', user_email=user_email)
    return render_template('index.html')