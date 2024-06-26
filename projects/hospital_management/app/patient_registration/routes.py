import requests
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
    patient_id = new_patient.id

    # Notify other services
    services = ["http://doc_analysis:5002/sync_patient", 
                "http://lab_reports:5003/sync_patient", 
                "http://final_bill_discharge:5004/sync_patient"]
    for service in services:
        try:
            requests.post(service, json={"patient_id": patient_id})
        except requests.exceptions.RequestException as e:
            print(f"Error notifying service {service}: {e}")

    return jsonify(new_patient.id), 201

@bp.route('/<int:patient_id>/', methods=['DELETE'])
def delete_patient(patient_id):
    patient = Patient.query.get_or_404(patient_id)
    db.session.delete(patient)
    db.session.commit()
    return '', 204
