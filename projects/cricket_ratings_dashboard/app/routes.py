from flask import Blueprint, request, jsonify
from .models import CountryRanking, db

main = Blueprint('main', __name__)

@main.route('/rankings', methods=['GET'])
def get_rankings():
    rankings = CountryRanking.query.all()
    return jsonify([r.to_dict() for r in rankings])

@main.route('/ranking', methods=['POST'])
def add_ranking():
    data = request.get_json()
    new_ranking = CountryRanking(
        unique_id=data['unique_id'],
        country=data['country'],
        points=data['points']
    )
    db.session.add(new_ranking)
    db.session.commit()
    return jsonify(new_ranking.to_dict()), 201

@main.route('/ranking/<int:id>', methods=['PUT'])
def update_ranking(id):
    data = request.get_json()
    ranking = CountryRanking.query.get(id)
    if not ranking:
        return jsonify({'message': 'Ranking not found'}), 404

    ranking.unique_id = data.get('unique_id', ranking.unique_id)
    ranking.country = data.get('country', ranking.country)
    ranking.points = data.get('points', ranking.points)
    db.session.commit()
    return jsonify(ranking.to_dict())

@main.route('/ranking/<int:id>', methods=['DELETE'])
def delete_ranking(id):
    ranking = CountryRanking.query.get(id)
    if not ranking:
        return jsonify({'message': 'Ranking not found'}), 404

    db.session.delete(ranking)
    db.session.commit()
    return jsonify({'message': 'Ranking deleted'})
