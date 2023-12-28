from flask import Flask

import pyrebase


app = Flask(__name__)
app.secret_key = 'scret'


firebaseConfig = {
    "apiKey": "AIzaSyAUzqJPNEj-aticZJnN9T6c42IC7BzmRQI",
    "authDomain": "test-firebase-auth-822e8.firebaseapp.com",
    "databaseURL": "https://test-firebase-auth-822e8.firebaseio.com",
    "projectId": "test-firebase-auth-822e8",
    "storageBucket": "test-firebase-auth-822e8.appspot.com",
    "messagingSenderId": "372336096232",
    "appId": "1:372336096232:web:26d1be3220c36158906a5d",
    "measurementId": "G-TYZQYWY7QR"
}

firebase = pyrebase.initialize_app(firebaseConfig)

auth = firebase.auth()
db = firebase.database()


from app import views
from app import signup
from app import login
from app import logout