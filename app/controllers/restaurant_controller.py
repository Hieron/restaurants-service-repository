from flask import jsonify, make_response, abort
from app.models.restaurant import Restaurant
from app.models.address import Address
from app.database.db import db

class RestaurantController:
    def format_restaurant(self, restaurant):
        return {
            'id': restaurant.id,
            'name': restaurant.name,
            'url': restaurant.url,
            'menu': restaurant.menu,
            'telephone': restaurant.telephone,
            'priceRange': restaurant.priceRange,
            'address': {
                'postalCode': restaurant.address.postalCode,
                'streetAddress': restaurant.address.streetAddress,
                'addressLocality': restaurant.address.addressLocality,
                'addressRegion': restaurant.address.addressRegion,
                'addressCountry': restaurant.address.addressCountry
            }
        }

    def get_restaurants(self, search):

        query = Restaurant.query

        if any(search.values()):
            query = query.join(Restaurant.address)
            for key, value in search.items():
                if value:
                    query = query.filter(getattr(Address, key) == value)

        restaurants = query.all()

        output = [self.format_restaurant(restaurant) for restaurant in restaurants]
        return jsonify({
            'success': True,
            'data': output
        })

    def get_restaurant(self, restaurant_id):
        restaurant = Restaurant.query.get(restaurant_id)
        if restaurant is None:
            return jsonify({
                'success': False,
                'message': 'Restaurant not found.'
            }), 404

        return jsonify(self.format_restaurant(restaurant))

    def create_restaurant(self, data):
        restaurant = Restaurant(
            name=data['name'],
            url=data.get('url'),
            menu=data.get('menu'),
            telephone=data.get('telephone'),
            priceRange=data.get('priceRange')
        )
        address_data = data['address']
        address = Address(
            postalCode=address_data['postalCode'],
            streetAddress=address_data['streetAddress'],
            addressLocality=address_data['addressLocality'],
            addressRegion=address_data['addressRegion'],
            addressCountry=address_data['addressCountry']
        )
        restaurant.address = address
        db.session.add(restaurant)
        db.session.commit()
        return jsonify({
            'success': True,
            'message': 'Restaurant created successfully.', 
            'restaurant_id': restaurant.id
        })

    def update_restaurant(self, restaurant_id, data):
        restaurant = Restaurant.query.get(restaurant_id)
        if restaurant is None:
            return jsonify({
                'success': False,
                'message': 'Restaurant not found.'
            }), 404
        
        restaurant.name = data.get('name', restaurant.name)
        restaurant.url = data.get('url', restaurant.url)
        restaurant.menu = data.get('menu', restaurant.menu)
        restaurant.telephone = data.get('telephone', restaurant.telephone)
        restaurant.priceRange = data.get('priceRange', restaurant.priceRange)
        address_data = data.get('address')
        if address_data:
            address = restaurant.address
            address.postalCode = address_data.get('postalCode', address.postalCode)
            address.streetAddress = address_data.get('streetAddress', address.streetAddress)
            address.addressLocality = address_data.get('addressLocality', address.addressLocality)
            address.addressRegion = address_data.get('addressRegion', address.addressRegion)
            address.addressCountry = address_data.get('addressCountry', address.addressCountry)
        db.session.commit()
        return jsonify({
            'success': True,
            'message': 'Restaurant updated successfully.'
        })

    def delete_restaurant(self, restaurant_id):
        restaurant = Restaurant.query.get(restaurant_id)
        if restaurant is None:
            return jsonify({
                'success': False,
                'message': 'Restaurant not found.'
            }), 404
        
        db.session.delete(restaurant)
        db.session.commit()
        return jsonify({
            'success': True,
            'message': 'Restaurant excluded successfully.'
        })
