from app import app, auth
from flask import  session, redirect, url_for, flash


@app.route('/logout')
def logout():
    session.pop('user', None)
    flash("You've been logged out!", "info")
    return redirect(url_for('home'))