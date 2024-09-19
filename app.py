from flask import Flask
from db import db
from import_stat import get_stats
from flask import Blueprint, request, jsonify
from bluprints.players import players_bp
from models.player import Player
from models.stats import Stats
from bluprints.teams import teams_bp

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///NBA.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
app.register_blueprint(players_bp)
app.register_blueprint(teams_bp)

# db.init_app(app)
# with app.app_context():
#     db.create_all()
#     get_stats()

if __name__ == '__main__':
    app.run(debug=True)