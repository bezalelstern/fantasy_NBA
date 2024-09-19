from flask import Flask
from db import db
from import_stat import get_stats
from flask import Blueprint, request, jsonify
from bluprints.players import players_bp
from models.player import Player
from models.stats import Stats


teams_bp = Blueprint('teams', __name__, url_prefix='api/teams')

@teams_bp.route('/<team_id>', methods=['POST'])
def creat_team(team_id):
    data = request.get_json()
    if not data or 'name' not in data or 'players' not in data:
        return jsonify({'message': 'Missing data'}), 400
    ids_player = data['ids_player']
    if len(ids_player) is not 5:
        return jsonify({'message': 'Number of players must be 5'}), 400
    positions = ["PG", "SG", "SF", "PF", "C"]
    team_position = []
    for id_player in ids_player:
        player = Stats.query.get(id_player)
        if player is None:
            return jsonify({'message': 'Player not found'}), 404
        if player.position not in positions:
            return jsonify({'message': 'Invalid player position'}), 400
        if player.position in team_position:
            return jsonify({'message': 'Duplicate player position'}), 400
        team_position.append(player.position)

    new_team = Player(team_id=team_id, name=data['name'])
    db.session.add(new_team)
    db.session.commit()
    return jsonify({'message': 'Team created successfully'}), 201

@teams_bp.route('/<team_id>', methods=['GET'])
def get_team(team_id):
    team = Player.query.get_or_404(team_id)
    return jsonify(team.to_dict())

@teams_bp.route('/<team_id>', methods=['PUT'])
def update_team(team_id):
    team = Player.query.get_or_404(team_id)
    data = request.get_json()
    if data is None or 'name' not in data:
        return jsonify({'message': 'Missing data'}), 400
    team.name = data['name']
    db.session.commit()
    return jsonify(team.to_dict())

@teams_bp.route('/<team_id>', methods=['DELETE'])
def delete_team(team_id):
    team = Player.query.get_or_404(team_id)
    db.session.delete(team)
    db.session.commit()
    return jsonify({'message': 'Team deleted successfully'}), 200



