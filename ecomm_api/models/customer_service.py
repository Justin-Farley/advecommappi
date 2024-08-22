from models.customer import Customer
from models.customer_account import CustomerAccount
from flask import jsonify

def create_customer(data):
    customer = Customer(**data)
    db.session.add(customer)
    db.session.commit()
    return customer

def get_customer(customer_id):
    return Customer.query.get(customer_id)

def update_customer(customer_id, data):
    customer = get_customer(customer_id)
    if customer:
        for key, value in data.items():
            setattr(customer, key, value)
        db.session.commit()
        return customer
    return None

def delete_customer(customer_id):
    customer = get_customer(customer_id)
    if customer:
        db.session.delete(customer)
        db.session.commit()
        return True
    return False
