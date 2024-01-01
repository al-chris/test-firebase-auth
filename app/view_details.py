from app import app, auth, login_required
from flask import request, render_template, session, redirect, url_for


@app.route('/view_details', methods=['GET', 'POST'])
@login_required
def view_details():
    pass