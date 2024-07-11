from flask import Blueprint, request, jsonify
from .models import CountryRanking, Player, db
from . import redis_client

main = Blueprint('main', __name__)

@main.route('/rankings', methods=['GET'])
def get_rankings():
    rankings = CountryRanking.query.all()
    return jsonify([r.to_dict() for r in rankings])

@main.route('/ranking', methods=['POST'])
def add_ranking():
    data = request.get_json()
    existing_ranking = CountryRanking.query.filter_by(unique_id=data['unique_id']).first()
    if existing_ranking:
        existing_ranking.country = data['country']
        existing_ranking.points = data['points']
        db.session.commit()
        redis_client.zadd('country_rankings', {data['country']: data['points']})
        return jsonify(existing_ranking.to_dict()), 200
    else:
        new_ranking = CountryRanking(
            unique_id=data['unique_id'],
            country=data['country'],
            points=data['points']
        )
        db.session.add(new_ranking)
        db.session.commit()
        redis_client.zadd('country_rankings', {data['country']: data['points']})
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
    redis_client.zadd('country_rankings', {data['country']: data['points']})
    return jsonify(ranking.to_dict())

@main.route('/ranking/<int:id>', methods=['DELETE'])
def delete_ranking(id):
    ranking = CountryRanking.query.get(id)
    if not ranking:
        return jsonify({'message': 'Ranking not found'}), 404

    redis_client.zrem('country_rankings', ranking.country)
    db.session.delete(ranking)
    db.session.commit()
    return jsonify({'message': 'Ranking deleted'})

@main.route('/rankings/sorted', methods=['GET'])
def get_sorted_rankings():
    rankings = redis_client.zrevrange('country_rankings', 0, -1, withscores=True)
    sorted_rankings = [{ 'country': rank[0].decode('utf-8'), 'points': rank[1] } for rank in rankings]
    return jsonify(sorted_rankings)

@main.route('/players/top', methods=['GET'])
def get_top_players():
    top_players = redis_client.zrevrange('player_rankings', 0, 99, withscores=True)
    player_details = []
    for player_id, points in top_players:
        player_id = player_id.decode('utf-8')
        player = Player.query.filter_by(unique_id=player_id).first()
        if player:
            player_info = player.to_dict()
            player_info['points'] = points
            player_details.append(player_info)
    return jsonify(player_details)
