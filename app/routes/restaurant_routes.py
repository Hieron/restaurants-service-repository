from flask import Blueprint, request
from app.controllers.restaurant_controller import RestaurantController

restaurant_routes = Blueprint('restaurant_routes', __name__)
restaurant_controller = RestaurantController()

@restaurant_routes.route('/restaurants', methods=['GET'])
def get_restaurants():
    search = {
        'postalCode': request.args.get('postalCode'),
        'streetAddress': request.args.get('streetAddress'),
        'addressLocality': request.args.get('addressLocality'),
        'addressRegion': request.args.get('addressRegion'),
        'addressCountry': request.args.get('addressCountry')
    }
    return restaurant_controller.get_restaurants(search)

@restaurant_routes.route('/restaurants/<int:restaurant_id>', methods=['GET'])
def get_restaurant(restaurant_id):
    return restaurant_controller.get_restaurant(restaurant_id)

@restaurant_routes.route('/restaurants', methods=['POST'])
def create_restaurant():
    data = request.json
    return restaurant_controller.create_restaurant(data)

@restaurant_routes.route('/restaurants/<int:restaurant_id>', methods=['PUT'])
def update_restaurant(restaurant_id):
    data = request.json
    return restaurant_controller.update_restaurant(restaurant_id, data)

@restaurant_routes.route('/restaurants/<int:restaurant_id>', methods=['DELETE'])
def delete_restaurant(restaurant_id):
    return restaurant_controller.delete_restaurant(restaurant_id)