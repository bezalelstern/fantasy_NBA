from db import db
class Stats(db.Model):
    __tablename__ = 'stats'
    id = db.Column(db.Integer, primary_key=True)
    playerId = db.Column(db.Integer, db.ForeignKey('players.id'), nullable=False)
    playerName = db.Column(db.String(80), nullable=False)
    team = db.Column(db.String(80), nullable=False)
    position = db.Column(db.String(80), nullable=False)
    season = db.Column(db.String(80), nullable=False)
    points = db.Column(db.Integer, nullable=False, default=0)
    twoPercent = db.Column(db.Float, nullable=False, default=0.0)
    threePercent = db.Column(db.Float, nullable=False, default=0.0)
    ATR = db.Column(db.Float, nullable=False)
    PPG_Ratio = db.Column(db.Float, nullable=False)


    def to_dict(self):
        return {
            "id": self.id,
            "playerId": self.playerId,
            "playerName": self.playerName,
            "team": self.team,
            "position": self.position,
            "season": self.season,
            "points": self.points,
            "twoPercent": self.twoPercent,
            "threePercent": self.threePercent,
            "ATR": self.ATR,
            "PPG_Ratio": self.PPG_Ratio
        }
