

def ppg_calculate(player,data):
    ppg = []
    player_ppg = division(player["points"], player["games"])
    for entiti in data:
        if entiti["position"] == player["position"] and entiti["season"] == player["season"]:
            ppg.append(division(entiti["points"], entiti["games"]))
    avj =  division(sum(ppg), len(ppg))
    return division(player_ppg, avj)

def division(a, b):
    if b > 0:
        return a / b
    return 0

