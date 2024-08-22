from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache
from flask_limiter import Limiter
from config.config import Config
from routes.customer_routes import init_routes as init_customer_routes
from routes.customer_account_routes import init_routes as init_customer_account_routes
from routes.product_routes import init_routes as init_product_routes
from routes.order_routes import init_routes as init_order_routes
from utils.jwt_utils import token_required
from utils.cache_utils import cache
from utils.limiter_utils import limiter


app = Flask(__name__)


app.config.from_object(Config)


db = SQLAlchemy(app)


cache.init_app(app)


limiter.init_app(app)


init_customer_routes(app)
init_customer_account_routes(app)
init_product_routes(app)
init_order_routes(app)


@app.route('/')
def home():
    return 'Welcome to the Customer and Product API!'


@app.errorhandler(404)
def not_found(error):
    return {'message': 'Resource not found'}, 404

@app.errorhandler(500)
def internal_error(error):
    return {'message': 'Internal server error'}, 500

if __name__ == '__main__':
    app.run(debug=True)
