from models.team import Team as Team
from models.stats import Stats as Stats
from flask import jsonify, request
from db import db
from models.player import Player

def create_team(data):
    if not data or 'name' not in data or 'players' not in data:
        return jsonify({'message': 'Missing data'}), 400
    ids_player = data['ids_player']
    if len(ids_player) is not 5:
        return jsonify({'message': 'Number of players must be 5'}), 400
    positions = ["PG", "SG", "SF", "PF", "C"]
    team_position = []
    new_team = Team(name=data['name'])
    for id_player in ids_player:
        player = Stats.query.get(id_player)
        if player is None:
            return jsonify({'message': 'Player not found'}), 404
        if player.position not in positions:
            return jsonify({'message': 'Invalid player position'}), 400
        if player.position in team_position:
            return jsonify({'message': 'Duplicate player position'}), 400
        team_position.append(player.position)

    db.session.add(new_team)
    db.session.commit()
    return jsonify({'message': 'Team created successfully'}), 201

def update_team(team_id):
    team = Player.query.get_or_404(team_id)
    data = request.get_json()
    if data is None or 'name' not in data:
        return jsonify({'message': 'Missing data'}), 400
    team.name = data['name']
    db.session.commit()
    return team.to_dict()