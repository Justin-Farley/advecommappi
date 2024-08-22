from flask import Blueprint
from controllers.customer_controller import bp as customer_bp

def init_routes(app):
    app.register_blueprint(customer_bp, url_prefix='/api')
