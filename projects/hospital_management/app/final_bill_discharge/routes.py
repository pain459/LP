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

@bp.route('/<int:bill_id>/', methods=['GET'])
def get_bill(bill_id):
    bill = Bill.query.get_or_404(bill_id)
    return jsonify({
        "id": bill.id,
        "patient_id": bill.patient_id,
        "total_amount": bill.total_amount,
        "payment_status": bill.payment_status,
        "discharge_date": bill.discharge_date.isoformat()
    })

@bp.route('/<int:bill_id>/', methods=['PUT'])
def update_bill(bill_id):
    data = request.get_json()
    bill = Bill.query.get_or_404(bill_id)
    for key, value in data.items():
        setattr(bill, key, value)
    db.session.commit()
    return jsonify({
        "id": bill.id,
        "patient_id": bill.patient_id,
        "total_amount": bill.total_amount,
        "payment_status": bill.payment_status,
        "discharge_date": bill.discharge_date.isoformat()
    })

@bp.route('/<int:bill_id>/', methods=['DELETE'])
def delete_bill(bill_id):
    bill = Bill.query.get_or_404(bill_id)
    db.session.delete(bill)
    db.session.commit()
    return '', 204

@bp.route('/sync_patient', methods=['POST'])
def sync_patient():
    data = request.get_json()
    patient_id = data.get('patient_id')
    if patient_id:
        # Perform any necessary initialization with the patient ID
        return jsonify({"message": "Patient ID synced successfully"}), 200
    return jsonify({"message": "Patient ID missing"}), 400
