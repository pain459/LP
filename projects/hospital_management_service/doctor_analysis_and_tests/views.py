from flask import Blueprint, request, jsonify
from sqlalchemy.exc import IntegrityError
import requests
from .models import db, DoctorAnalysisAndTests, Symptom, Test, Medicine

doctor_analysis_and_tests_blueprint = Blueprint('doctor_analysis_and_tests', __name__)

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
        for k, v in new_tests.items():
            record.tests[k] = v

    if 'medicines' in data:
        new_medicines, error = translate_codes(data['medicines'], medicines_dict)
        if error:
            return jsonify({'error': error}), 400
        for k, v in new_medicines.items():
            record.medicines[k] = v

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
