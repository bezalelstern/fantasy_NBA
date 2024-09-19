import requests
from db import db
from models.player import Player
from models.stats import Stats

def get_stats():
    url = "http://b8c40s8.143.198.70.30.sslip.io/api/PlayerDataTotals/query?season=2024&&pageSize=1000"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        players = []
        for player in data:
            if player["playerName"] in players:
                db.session.add(Stats(
                                    team = player["team"], position = player["position"], season = player["season"],
                                     points = player["points"], twoPercent = player["twoPercent"], threePercent = player["threePercent"],
                                     ATR = division(player["assists"], player['turnovers']), PPG_Ratio = ppg_calculate(player ,data)))
            else:
                players.append(player["playerName"])
        for name  in players:
            db.session.add(Player(name=name))
        db.session.commit()
    else:
        print(f"Error: {response.status_code}")
        return None


def division(a, b):
    if b > 0:
        return a / b
    return 0

def ppg_calculate(player,data):
    ppg = []
    player_ppg = division(player["points"], player["games"])
    for entiti in data:
        if entiti["position"] == player["position"] and entiti["season"] == player["season"]:
            ppg.append(division(entiti["points"], entiti["games"]))
    avj =  division(sum(ppg), len(ppg))
    return division(player_ppg, avj)

