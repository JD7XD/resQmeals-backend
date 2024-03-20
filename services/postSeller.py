import pyrebase
import os
from dotenv import load_dotenv
import datetime

load_dotenv()

firebaseConfig = {
    'apiKey': os.getenv('FIREBASE_API_KEY'),
    'authDomain': os.getenv('FIREBASE_AUTH_DOMAIN'),
    'databaseURL': os.getenv('FIREBASE_DATABASE_URL'),
    'projectId': os.getenv('FIREBASE_PROJECT_ID'),
    'storageBucket': os.getenv('FIREBASE_STORAGE_BUCKET'),
    'messagingSenderId': os.getenv('FIREBASE_MESSAGING_SENDER_ID'),
    'appId': os.getenv('FIREBASE_APP_ID'),
    'measurementId': os.getenv('FIREBASE_MEASUREMENT_ID')
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()

def unix_time():
    presentDate = datetime.datetime.now()
    unix_timestamp = datetime.datetime.timestamp(presentDate)*1000
    round_unix_time = round(unix_timestamp)
    return str(round_unix_time)

def postRestaurants(restaurant_name, seller_address, seller_contact_number):
    unix_time_stamp = unix_time()

    restaurant_id = restaurant_name.lower().replace(' ', '_') + '_' + unix_time_stamp

    data = {
        'address': seller_address,
        'contact_number': seller_contact_number,
    }

    db.child('restaurants').child(restaurant_id).set(data)

    return restaurant_id