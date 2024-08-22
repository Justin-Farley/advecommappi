from flask import Blueprint, request, jsonify
from services.customer_service import create_customer, get_customer, update_customer, delete_customer
from utils.jwt_utils import token_required, admin_required

bp = Blueprint('customer', __name__)

@bp.route('/customers', methods=['POST'])
@admin_required
def add_customer():
    data = request.json
    customer = create_customer(data)
    return jsonify(customer), 201

@bp.route('/customers/<int:id>', methods=['GET'])
@token_required
def retrieve_customer(id):
    customer = get_customer(id)
    if customer:
        return jsonify(customer), 200
    return jsonify({'message': 'Customer not found'}), 404

@bp.route('/customers/<int:id>', methods=['PUT'])
@admin_required
def update_customer_info(id):
    data = request.json
    customer = update_customer(id, data)
    if customer:
        return jsonify(customer), 200
    return jsonify({'message': 'Customer not found'}), 404

@bp.route('/customers/<int:id>', methods=['DELETE'])
@admin_required
def delete_customer_info(id):
    success = delete_customer(id)
    if success:
        return jsonify({'message': 'Customer deleted'}), 200
    return jsonify({'message': 'Customer not found'}), 404
