from flask import Blueprint

bp = Blueprint('final_bill_discharge', __name__)

from app.final_bill_discharge import routes
from app.final_bill_discharge.models import Bill
