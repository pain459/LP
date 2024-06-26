from flask import Blueprint, request, jsonify
from app import db
from app.models import Analysis

bp = Blueprint('doc_analysis', __name__)

@bp.route('/', methods=['POST'])
def create_analysis():
    data = request.get_json()
    new_analysis = Analysis(**data)
    db.session.add(new_analysis)
    db.session.commit()
    return jsonify(new_analysis.id), 201

@bp.route('/<int:analysis_id>', methods=['GET'])
def get_analysis(analysis_id):
    analysis = Analysis.query.get_or_404(analysis_id)
    return jsonify(analysis)

@bp.route('/<int:analysis_id>', methods=['PUT'])
def update_analysis(analysis_id):
    data = request.get_json()
    analysis = Analysis.query.get_or_404(analysis_id)
    for key, value in data.items():
        setattr(analysis, key, value)
    db.session.commit()
    return jsonify(analysis)

@bp.route('/<int:analysis_id>', methods=['DELETE'])
def delete_analysis(analysis_id):
    analysis = Analysis.query.get_or_404(analysis_id)
    db.session.delete(analysis)
    db.session.commit()
    return '', 204
