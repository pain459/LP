from flask import Blueprint

bp = Blueprint('doc_analysis', __name__)

from app.doc_analysis import routes
from app.doc_analysis.models import Analysis
