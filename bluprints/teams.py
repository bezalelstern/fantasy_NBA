from flask import Flask
from db import db
from import_stat import get_stats
from flask import Blueprint, request, jsonify
from models.player import Player
from service.team_service import create_team, update_team as ut

teams_bp = Blueprint('teams', __name__, url_prefix='api/teams')

@teams_bp.route('/creat', methods=['POST'])
def creat_team():
    data = request.get_json()
    create_team(data)

@teams_bp.route('/<team_id>', methods=['PUT'])
def update_team(team_id):
    return jsonify(ut(team_id))
@teams_bp.route('/<team_id>', methods=['GET'])
def get_team(team_id):
    team = Player.query.get_or_404(team_id)
    return jsonify(team.to_dict())



@teams_bp.route('/<team_id>', methods=['DELETE'])
def delete_team(team_id):
    team = Player.query.get_or_404(team_id)
    db.session.delete(team)
    db.session.commit()
    return jsonify({'message': 'Team deleted successfully'}), 200



