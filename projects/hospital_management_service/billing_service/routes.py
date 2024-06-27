from flask import request, jsonify
from . import app, db
from .models import DoctorAnalysisAndTests, Test, Medicine, DoctorAnalysisAndTestsArchive

@app.route('/billing/<patient_unique_id>', methods=['GET'])
def get_bill(patient_unique_id):
    record = DoctorAnalysisAndTests.query.filter_by(patient_unique_id=patient_unique_id).first_or_404()
    total = 0.0
    for test_id in record.tests.keys():
        test = Test.query.get(test_id)
        total += float(test.price)
    for med_id in record.medicines.keys():
        medicine = Medicine.query.get(med_id)
        total += float(medicine.price)
    return jsonify({
        'patient_unique_id': record.patient_unique_id,
        'total': total
    }), 200

@app.route('/billing/<patient_unique_id>/pay', methods=['POST'])
def pay_bill(patient_unique_id):
    record = DoctorAnalysisAndTests.query.filter_by(patient_unique_id=patient_unique_id).first_or_404()
    archive_record = DoctorAnalysisAndTestsArchive(
        patient_unique_id=record.patient_unique_id,
        analysis=record.analysis,
        tests=record.tests,
        medicines=record.medicines
    )
    db.session.add(archive_record)
    db.session.delete(record)
    db.session.commit()
    return jsonify({'message': 'Payment successful and record archived.'}), 200

@app.route('/billing/archive/<patient_unique_id>', methods=['GET'])
def get_archived_record(patient_unique_id):
    record = DoctorAnalysisAndTestsArchive.query.filter_by(patient_unique_id=patient_unique_id).all()
    if not record:
        return jsonify({'error': 'No archived records found for this patient.'}), 404

    archived_records = []
    for rec in record:
        archived_records.append({
            'patient_unique_id': rec.patient_unique_id,
            'analysis': rec.analysis,
            'tests': rec.tests,
            'medicines': rec.medicines,
            'paid_at': rec.paid_at
        })

    return jsonify(archived_records), 200
