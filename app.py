from flask import Flask, request
from flask_cors import CORS
from services import postSeller as ps
from services import postBuyer as pb
from services import postPost as pp
from services import getPost as gp

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

app.secret_key = 'secret'

@app.route('/')
def hello_world():
    return "resQmeals backend!"

@app.route('/api/postSeller', methods=['POST'])
def post_seller():
    req = request.get_json()
    restaurant_name = req.get('restaurant_name')
    seller_address = req.get('seller_address')
    seller_contact_number = req.get('seller_contact_number')
    return ps.postRestaurants(restaurant_name, seller_address, seller_contact_number)

@app.route('/api/postBuyer', methods=['POST'])
def post_buyer():
    req = request.get_json()
    buyer_name = req.get('buyer_name')
    buyer_address = req.get('buyer_address')
    buyer_contact_number = req.get('buyer_contact_number')
    return pb.postUser(buyer_name, buyer_address, buyer_contact_number)

@app.route('/api/postPost', methods=['POST'])
def create_post_route():
    req = request.get_json()
    restaurant_id = req.get('restaurant_id')
    food_name = req.get('food_name')
    item_quantity = req.get('item_quantity')
    claimer = req.get('claimer')
    status = req.get('status')
    return pp.postPost(restaurant_id, food_name, item_quantity, claimer, status)

@app.route('/api/getPosts', methods=['GET'])
def get_posts_route():
    restaurant_id = request.args.get('restaurant_id')
    if restaurant_id:
        posts = gp.getPost(restaurant_id)
        return posts
    else:
        return 'Missing restaurant_id parameter'

# # main driver function
if __name__ == '__main__':
    app.run(port=8080, debug=True)