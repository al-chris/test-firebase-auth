from app import app, auth
from flask import  session, redirect, url_for


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('home'))