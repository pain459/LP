import logging
from flask import Blueprint, request, jsonify
from sqlalchemy.exc import IntegrityError
import requests
from .models import db, DoctorAnalysisAndTests, Symptom, Test, Medicine

# Configure logging
logger = logging.getLogger(__name__)

doctor_analysis_and_tests_blueprint = Blueprint('doctor_analysis_and_tests', __name__)

def check_patient_exists(patient_unique_id):
    response = requests.get(f'http://patient_registration_service:5000/patients/{patient_unique_id}')
    return response.status_code == 200

def fetch_dictionary(model):
    records = model.query.all()
    return {record.id: record.name for record in records}

def translate_codes(codes, dictionary):
    translated = {}
    for code in codes:
        if code not in dictionary:
            return None, f"Invalid code {code}. Valid codes are: {list(dictionary.keys())}"
        translated[code] = dictionary[code]
    return translated, None

@doctor_analysis_and_tests_blueprint.route('/doctor_analysis_and_tests', methods=['POST'])
def add_analysis_and_tests():
    data = request.get_json()
    patient_unique_id = data['patient_unique_id']

    if not check_patient_exists(patient_unique_id):
        return jsonify({'error': 'Patient record not found.'}), 404

    symptoms_dict = fetch_dictionary(Symptom)
    tests_dict = fetch_dictionary(Test)
    medicines_dict = fetch_dictionary(Medicine)

    analysis, error = translate_codes(data['analysis'], symptoms_dict)
    if error:
        return jsonify({'error': error}), 400

    tests, error = translate_codes(data['tests'], tests_dict)
    if error:
        return jsonify({'error': error}), 400

    medicines, error = translate_codes(data['medicines'], medicines_dict)
    if error:
        return jsonify({'error': error}), 400

    new_record = DoctorAnalysisAndTests(
        patient_unique_id=patient_unique_id,
        analysis=analysis,
        tests=tests,
        medicines=medicines
    )
    try:
        db.session.add(new_record)
        db.session.commit()
        return jsonify({'message': 'Record added successfully!'}), 201
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@doctor_analysis_and_tests_blueprint.route('/doctor_analysis_and_tests/<patient_unique_id>', methods=['GET'])
def get_record(patient_unique_id):
    record = DoctorAnalysisAndTests.query.filter_by(patient_unique_id=patient_unique_id).first_or_404()
    return jsonify({
        'patient_unique_id': record.patient_unique_id,
        'analysis': record.analysis,
        'tests': record.tests,
        'medicines': record.medicines
    }), 200

@doctor_analysis_and_tests_blueprint.route('/doctor_analysis_and_tests/<patient_unique_id>', methods=['PUT'])
def update_record(patient_unique_id):
    data = request.get_json()
    record = DoctorAnalysisAndTests.query.filter_by(patient_unique_id=patient_unique_id).first_or_404()

    symptoms_dict = fetch_dictionary(Symptom)
    tests_dict = fetch_dictionary(Test)
    medicines_dict = fetch_dictionary(Medicine)

    if 'analysis' in data:
        analysis, error = translate_codes(data['analysis'], symptoms_dict)
        if error:
            return jsonify({'error': error}), 400
        record.analysis = analysis

    if 'tests' in data:
        new_tests, error = translate_codes(data['tests'], tests_dict)
        if error:
            return jsonify({'error': error}), 400
        record.tests = {**record.tests, **new_tests}

    if 'medicines' in data:
        new_medicines, error = translate_codes(data['medicines'], medicines_dict)
        if error:
            return jsonify({'error': error}), 400
        record.medicines = {**record.medicines, **new_medicines}

    try:
        db.session.commit()
        return jsonify({'message': 'Record updated successfully!'}), 200
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@doctor_analysis_and_tests_blueprint.route('/doctor_analysis_and_tests/<patient_unique_id>', methods=['DELETE'])
def delete_record(patient_unique_id):
    record = DoctorAnalysisAndTests.query.filter_by(patient_unique_id=patient_unique_id).first_or_404()
    try:
        db.session.delete(record)
        db.session.commit()
        return jsonify({'message': 'Record deleted successfully!'}), 200
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@doctor_analysis_and_tests_blueprint.route('/doctor_analysis_and_tests/<patient_unique_id>/<category>/<int:code>', methods=['DELETE'])
def delete_detail(patient_unique_id, category, code):
    record = DoctorAnalysisAndTests.query.filter_by(patient_unique_id=patient_unique_id).first_or_404()

    if category == 'tests':
        if code in record.tests:
            del record.tests[code]
        else:
            return jsonify({'error': f'Code {code} not found in tests.'}), 400
    elif category == 'medicines':
        if code in record.medicines:
            del record.medicines[code]
        else:
            return jsonify({'error': f'Code {code} not found in medicines.'}), 400
    else:
        return jsonify({'error': 'Invalid category. Valid categories are: tests, medicines.'}), 400

    try:
        db.session.commit()
        return jsonify({'message': f'{category[:-1].capitalize()} detail deleted successfully!'}), 200
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400
