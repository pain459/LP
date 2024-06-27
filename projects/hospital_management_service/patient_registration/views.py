import logging
from flask import Blueprint, request, jsonify
from sqlalchemy.exc import IntegrityError
from .models import db, Patient

# Configure logging
logger = logging.getLogger(__name__)

patient_blueprint = Blueprint('patient', __name__)

@patient_blueprint.route('/patients', methods=['POST'])
def add_patient():
    data = request.get_json()
    cleaned_contact = Patient.clean_contact(data['contact'])
    unique_id = Patient.generate_unique_id(data['name'], cleaned_contact)
    new_patient = Patient(
        name=data['name'],
        age=data['age'],
        gender=data['gender'],
        address=data.get('address', ''),
        contact=cleaned_contact,
        unique_id=unique_id
    )
    try:
        db.session.add(new_patient)
        db.session.commit()
        logger.info(f"Patient added successfully: {unique_id}")
        return jsonify({'message': 'Patient added successfully!', 'unique_id': unique_id}), 201
    except IntegrityError as e:
        db.session.rollback()
        logger.error(f"IntegrityError: {e}")
        if 'unique_id' in str(e.orig):
            return jsonify({'error': 'A patient with this unique ID already exists.'}), 400
        if 'contact' in str(e.orig):
            return jsonify({'error': 'A patient with this contact already exists.'}), 400
        return jsonify({'error': 'An error occurred while adding the patient.'}), 500

@patient_blueprint.route('/patients', methods=['GET'])
def get_patients():
    try:
        patients = Patient.query.all()
        logger.info("Retrieved all patients.")
        return jsonify([{
            'patient_id': p.patient_id,
            'name': p.name,
            'age': p.age,
            'gender': p.gender,
            'address': p.address,
            'contact': p.contact,
            'unique_id': p.unique_id
        } for p in patients]), 200
    except Exception as e:
        logger.error(f"Error retrieving patients: {e}")
        return jsonify({'error': 'An error occurred while retrieving patients.'}), 500

@patient_blueprint.route('/patients/<unique_id>', methods=['GET'])
def get_patient(unique_id):
    try:
        patient = Patient.query.filter_by(unique_id=unique_id).first_or_404()
        logger.info(f"Retrieved patient: {unique_id}")
        return jsonify({
            'patient_id': patient.patient_id,
            'name': patient.name,
            'age': patient.age,
            'gender': patient.gender,
            'address': patient.address,
            'contact': patient.contact,
            'unique_id': patient.unique_id
        }), 200
    except Exception as e:
        logger.error(f"Error retrieving patient {unique_id}: {e}")
        return jsonify({'error': 'An error occurred while retrieving the patient.'}), 500

@patient_blueprint.route('/patients/<unique_id>', methods=['PUT'])
def update_patient(unique_id):
    data = request.get_json()
    try:
        patient = Patient.query.filter_by(unique_id=unique_id).first_or_404()
        patient.name = data['name']
        patient.age = data['age']
        patient.gender = data['gender']
        patient.address = data.get('address', patient.address)
        patient.contact = Patient.clean_contact(data['contact'])
        db.session.commit()
        logger.info(f"Patient updated successfully: {unique_id}")
        return jsonify({'message': 'Patient updated successfully!'}), 200
    except IntegrityError as e:
        db.session.rollback()
        logger.error(f"IntegrityError: {e}")
        if 'contact' in str(e.orig):
            return jsonify({'error': 'A patient with this contact already exists.'}), 400
        return jsonify({'error': 'An error occurred while updating the patient.'}), 500
    except Exception as e:
        logger.error(f"Error updating patient {unique_id}: {e}")
        return jsonify({'error': 'An error occurred while updating the patient.'}), 500

@patient_blueprint.route('/patients/<unique_id>', methods=['DELETE'])
def delete_patient(unique_id):
    try:
        patient = Patient.query.filter_by(unique_id=unique_id).first_or_404()
        db.session.delete(patient)
        db.session.commit()
        logger.info(f"Patient deleted successfully: {unique_id}")
        return jsonify({'message': 'Patient deleted successfully!'}), 200
    except Exception as e:
        logger.error(f"Error deleting patient {unique_id}: {e}")
        return jsonify({'error': 'An error occurred while deleting the patient.'}), 500

@patient_blueprint.route('/patients/search', methods=['GET'])
def search_patient_by_contact():
    contact = request.args.get('contact')
    if not contact:
        return jsonify({'error': 'Contact parameter is required.'}), 400
    cleaned_contact = Patient.clean_contact(contact)
    try:
        patient = Patient.query.filter_by(contact=cleaned_contact).first_or_404()
        logger.info(f"Retrieved patient by contact: {cleaned_contact}")
        return jsonify({
            'patient_id': patient.patient_id,
            'name': patient.name,
            'age': patient.age,
            'gender': patient.gender,
            'address': patient.address,
            'contact': patient.contact,
            'unique_id': patient.unique_id
        }), 200
    except Exception as e:
        logger.error(f"Error retrieving patient by contact {cleaned_contact}: {e}")
        return jsonify({'error': 'An error occurred while retrieving the patient.'}), 500
