import requests
from db import db
from models.player import Player
from models.stats import Stats
import caculat_ATR_PPG as ca

def get_stats():
    seasons = ["2024", "2023", "2022"]
    for season in seasons:
        url = f"http://b8c40s8.143.198.70.30.sslip.io/api/PlayerDataTotals/query?season={season}&&pageSize=1000"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            create_players_table(data)
            create_stats_table(data)
        else:
            print(f"Error: {response.status_code}")
            return None


def create_players_table(data):
    for player in data:
        db.session.add(Player(name = player["playerName"]))
        try:
            db.session.commit()
        except:
            db.session.rollback()



def create_stats_table(data):
    for player in data:
        player_id = find_player_id(player["playerName"])
        db.session.add(Stats(team = player["team"],playerId = player_id,playerName = player["playerName"], position = player["position"], season = player["season"],
                             points = player["points"], twoPercent = player["twoPercent"], threePercent = player["threePercent"],
                             ATR = ca.division(player["assists"], player['turnovers']), PPG_Ratio =ca.ppg_calculate(player ,data)))
        try:
            db.session.commit()
        except:
            db.session.rollback()

def find_player_id(name):
    player = Player.query.filter_by(name=name).first()
    if player:
        return player.id
    return None