from flask import Blueprint, request, jsonify
from app import db
from app.models import LabReport

bp = Blueprint('lab_reports', __name__)

@bp.route('/', methods=['POST'])
def create_lab_report():
    data = request.get_json()
    new_lab_report = LabReport(**data)
    db.session.add(new_lab_report)
    db.session.commit()
    return jsonify(new_lab_report.id), 201

@bp.route('/<int:report_id>', methods=['GET'])
def get_lab_report(report_id):
    lab_report = LabReport.query.get_or_404(report_id)
    return jsonify({
        "id": lab_report.id,
        "patient_id": lab_report.patient_id,
        "test_name": lab_report.test_name,
        "test_result": lab_report.test_result,
        "test_date": lab_report.test_date.isoformat(),
        "doctor_id": lab_report.doctor_id
    })

@bp.route('/<int:report_id>', methods=['PUT'])
def update_lab_report(report_id):
    data = request.get_json()
    lab_report = LabReport.query.get_or_404(report_id)
    for key, value in data.items():
        setattr(lab_report, key, value)
    db.session.commit()
    return jsonify({
        "id": lab_report.id,
        "patient_id": lab_report.patient_id,
        "test_name": lab_report.test_name,
        "test_result": lab_report.test_result,
        "test_date": lab_report.test_date.isoformat(),
        "doctor_id": lab_report.doctor_id
    })

@bp.route('/<int:report_id>', methods=['DELETE'])
def delete_lab_report(report_id):
    lab_report = LabReport.query.get_or_404(report_id)
    db.session.delete(lab_report)
    db.session.commit()
    return '', 204
