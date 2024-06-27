from flask import Blueprint, request, jsonify
from .models import db, Patient

patient_blueprint = Blueprint('patient', __name__)

@patient_blueprint.route('/patients', methods=['POST'])
def add_patient():
    data = request.get_json()
    unique_id = Patient.generate_unique_id(data['name'])
    new_patient = Patient(
        name=data['name'],
        age=data['age'],
        gender=data['gender'],
        address=data.get('address', ''),
        contact=data['contact'],
        unique_id=unique_id
    )
    db.session.add(new_patient)
    db.session.commit()
    return jsonify({'message': 'Patient added successfully!', 'unique_id': unique_id}), 201

@patient_blueprint.route('/patients', methods=['GET'])
def get_patients():
    patients = Patient.query.all()
    return jsonify([{
        'patient_id': p.patient_id,
        'name': p.name,
        'age': p.age,
        'gender': p.gender,
        'address': p.address,
        'contact': p.contact,
        'unique_id': p.unique_id
    } for p in patients]), 200

@patient_blueprint.route('/patients/<unique_id>', methods=['GET'])
def get_patient(unique_id):
    patient = Patient.query.filter_by(unique_id=unique_id).first_or_404()
    return jsonify({
        'patient_id': patient.patient_id,
        'name': patient.name,
        'age': patient.age,
        'gender': patient.gender,
        'address': patient.address,
        'contact': patient.contact,
        'unique_id': patient.unique_id
    }), 200

@patient_blueprint.route('/patients/<unique_id>', methods=['PUT'])
def update_patient(unique_id):
    data = request.get_json()
    patient = Patient.query.filter_by(unique_id=unique_id).first_or_404()
    patient.name = data['name']
    patient.age = data['age']
    patient.gender = data['gender']
    patient.address = data.get('address', patient.address)
    patient.contact = data['contact']
    db.session.commit()
    return jsonify({'message': 'Patient updated successfully!'}), 200

@patient_blueprint.route('/patients/<unique_id>', methods=['DELETE'])
def delete_patient(unique_id):
    patient = Patient.query.filter_by(unique_id=unique_id).first_or_404()
    db.session.delete(patient)
    db.session.commit()
    return jsonify({'message': 'Patient deleted successfully!'}), 200
