

import json  # Add this import statement
from models import Product

def get_products(request_handler):
    products = Product.select_all()
    request_handler._send_response(200, products)

def get_product(request_handler):
    product_id = request_handler.url_args[0]
    product = Product.select_by_id(product_id)
    if product:
        request_handler._send_response(200, product)
    else:
        request_handler._send_response(404, {"error": "Product not found"})

def add_product(request_handler):
    content_length = int(request_handler.headers['Content-Length'])
    post_data = json.loads(request_handler.rfile.read(content_length))
    name = post_data['name']
    price = post_data['price']
    description = post_data['description']
    success = Product.add_product(name, price, description)
    if success:
        request_handler._send_response(201, {"message": "Product added successfully"})
    else:
        request_handler._send_response(500, {"error": "Failed to add product"})
