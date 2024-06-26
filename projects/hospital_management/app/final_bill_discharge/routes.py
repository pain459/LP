from flask import Blueprint, request, jsonify
from app import db
from app.models import Bill

bp = Blueprint('final_bill_discharge', __name__)

@bp.route('/', methods=['POST'])
def create_bill():
    data = request.get_json()
    new_bill = Bill(**data)
    db.session.add(new_bill)
    db.session.commit()
    return jsonify(new_bill.id), 201

@bp.route('/<int:bill_id>', methods=['GET'])
def get_bill(bill_id):
    bill = Bill.query.get_or_404(bill_id)
    return jsonify(bill)

@bp.route('/<int:bill_id>', methods=['PUT'])
def update_bill(bill_id):
    data = request.get_json()
    bill = Bill.query.get_or_404(bill_id)
    for key, value in data.items():
        setattr(bill, key, value)
    db.session.commit()
    return jsonify(bill)

@bp.route('/<int:bill_id>', methods=['DELETE'])
def delete_bill(bill_id):
    bill = Bill.query.get_or_404(bill_id)
    db.session.delete(bill)
    db.session.commit()
    return '', 204
