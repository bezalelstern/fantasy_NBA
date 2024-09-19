from db import db
class Stats(db.Model):
    __tablename__ = 'stats'
    id = db.Column(db.Integer, primary_key=True)
    #playerId = db.Column(db.Integer, db.ForeignKey('players.id'), nullable=False)
    #team = db.Column('Team', backref=db.backref('players', lazy=True))
    team = db.Column(db.String(80), nullable=False)
    position = db.Column(db.String(80), nullable=False)
    season = db.Column(db.String(80), nullable=False)
    points = db.Column(db.Integer, nullable=False)
    twoPercent = db.Column(db.Float, nullable=True)
    threePercent = db.Column(db.Float, nullable=True)
    ATR = db.Column(db.Float, nullable=False)
    PPG_Ratio = db.Column(db.Float, nullable=False)
    # team_id = db.Column(db.Integer, db.ForeignKey('teams.id'), nullable=True)

    # games = db.relationship('Game', backref=db.backref('players', lazy=True))
    # goals = db.relationship('Goal', backref=db.backref('players', lazy=True))
    # assists = db.relationship('Assist', backref=db.backref('players', lazy=True))
    # clean_sheets = db.relationship('CleanSheet', backref=db.backref('players', lazy=True))
    # yellow_cards = db.relationship('YellowCard', backref=db.backref('players', lazy=True))
    # red_cards = db.relationship('RedCard', backref=db.backref('players', lazy=True))
