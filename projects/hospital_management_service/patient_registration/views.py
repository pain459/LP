from flask import Blueprint, request, jsonify
from .models import db, Patient

patient_blueprint = Blueprint('patient', __name__)

@patient_blueprint.route('/patients', methods=['POST'])
def add_patient():
    data = request.get_json()
    new_patient = Patient(
        name=data['name'],
        age=data['age'],
        gender=data['gender'],
        address=data.get('address', ''),
        contact=data['contact']
    )
    db.session.add(new_patient)
    db.session.commit()
    return jsonify({'message': 'Patient added successfully!'}), 201

@patient_blueprint.route('/patients', methods=['GET'])
def get_patients():
    patients = Patient.query.all()
    return jsonify([{
        'patient_id': p.patient_id,
        'name': p.name,
        'age': p.age,
        'gender': p.gender,
        'address': p.address,
        'contact': p.contact
    } for p in patients]), 200

@patient_blueprint.route('/patients/<int:patient_id>', methods=['GET'])
def get_patient(patient_id):
    patient = Patient.query.get_or_404(patient_id)
    return jsonify({
        'patient_id': patient.patient_id,
        'name': patient.name,
        'age': patient.age,
        'gender': patient.gender,
        'address': patient.address,
        'contact': patient.contact
    }), 200

@patient_blueprint.route('/patients/<int:patient_id>', methods=['PUT'])
def update_patient(patient_id):
    data = request.get_json()
    patient = Patient.query.get_or_404(patient_id)
    patient.name = data['name']
    patient.age = data['age']
    patient.gender = data['gender']
    patient.address = data.get('address', patient.address)
    patient.contact = data['contact']
    db.session.commit()
    return jsonify({'message': 'Patient updated successfully!'}), 200

@patient_blueprint.route('/patients/<int:patient_id>', methods=['DELETE'])
def delete_patient(patient_id):
    patient = Patient.query.get_or_404(patient_id)
    db.session.delete(patient)
    db.session.commit()
    return jsonify({'message': 'Patient deleted successfully!'}), 200
