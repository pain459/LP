from flask import Blueprint

bp = Blueprint('patient_registration', __name__)

from app.patient_registration import routes
from app.patient_registration.models import Patient
