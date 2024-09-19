from flask import Flask
from db import db
from import_stat import get_stats
from flask import Blueprint, request, jsonify
from bluprints.players import players_bp
from models.player import Player
from models.stats import Stats

teams_bp = Blueprint('teams', __name__, url_prefix='api/teams')