from flask import Blueprint, request, jsonify
from models.stats import Stats
from models.player import Player
from db import db
import requests

players_bp = Blueprint('players', __name__, url_prefix='/api' )

@players_bp.route('/players', methods=['GET'])
def get_players():
    position =request.args.get('position', default="SG", type=str)
    season = request.args.get('season', default="2024", type=str)
    print(position, season)
    query = db.session.query(Stats).join(Player).filter(Stats.position == position, Stats.season == season)
    players = query.all()
    print(players)
    print(type(position), type(season)  )
    results = []
    for stat in players:
        player = db.session.query(Player).filter_by(id=stat.playerId).first()
        results.append({
            'stat': stat.to_dict(),
            'player': {
                'id': player.id,
                'name': player.name
            }
        })

    return jsonify(results)
