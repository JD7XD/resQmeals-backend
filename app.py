from flask import Flask, request
from flask_cors import CORS
from services import postRestaurants as rn

app = Flask(__name__)
CORS(app)

app.secret_key = 'secret'

@app.route('/')
def hello_world():
    return "resQmeals backend!"

@app.route('/api/postRestaurant', methods=['POST'])
def post_restaurants():
    req = request.get_json()
    restaurant_name = req.get('restaurant_name')
    address = req.get('address')
    contact_number = req.get('contact_number')
    return rn.postRestaurants(restaurant_name, address, contact_number)


# # main driver function
if __name__ == '__main__':
    app.run(port=8080, debug=True)