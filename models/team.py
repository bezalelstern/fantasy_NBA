from db import db
from models.player import Player
class Team(db.Model):
    __tablename__ = 'teams'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    PG = db.column(db.Integer, default=0)
    SG = db.column(db.Integer, default=0)
    SF = db.column(db.Integer, default=0)
    PF = db.column(db.Integer, default=0)
    C = db.column(db.Integer, default=0)

    def to_dict(self):
        return {"id": self.id, "name": self.name,
                "PG": find_player_by_id(self.PG),
                "SG": find_player_by_id(self.SG),
                "SF": find_player_by_id(self.SF),
                "PF": find_player_by_id(self.PF),
                "C": find_player_by_id(self.C)}

def find_player_by_id(player_id):
    player =  Player.query.filter_by(id=player_id).first()
    if player:
        return player.name
    return None