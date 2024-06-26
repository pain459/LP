from flask import Blueprint, request, jsonify
from app import db
from app.models import Patient

bp = Blueprint('patient_registration', __name__)

@bp.route('/', methods=['POST'])
def create_patient():
    data = request.get_json()
    new_patient = Patient(**data)
    db.session.add(new_patient)
    db.session.commit()
    return jsonify(new_patient.id), 201

@bp.route('/<int:patient_id>/', methods=['GET'])
def get_patient(patient_id):
    patient = Patient.query.get_or_404(patient_id)
    return jsonify({
        "id": patient.id,
        "name": patient.name,
        "age": patient.age,
        "gender": patient.gender,
        "address": patient.address,
        "contact": patient.contact,
        "registration_date": patient.registration_date.isoformat()
    })

@bp.route('/<int:patient_id>/', methods=['PUT'])
def update_patient(patient_id):
    data = request.get_json()
    patient = Patient.query.get_or_404(patient_id)
    for key, value in data.items():
        setattr(patient, key, value)
    db.session.commit()
    return jsonify({
        "id": patient.id,
        "name": patient.name,
        "age": patient.age,
        "gender": patient.gender,
        "address": patient.address,
        "contact": patient.contact,
        "registration_date": patient.registration_date.isoformat()
    })

@bp.route('/<int:patient_id>/', methods=['DELETE'])
def delete_patient(patient_id):
    patient = Patient.query.get_or_404(patient_id)
    db.session.delete(patient)
    db.session.commit()
    return '', 204
