from flask import Blueprint

bp = Blueprint('lab_reports', __name__)

from app.lab_reports import routes
from app.lab_reports.models import LabReport
