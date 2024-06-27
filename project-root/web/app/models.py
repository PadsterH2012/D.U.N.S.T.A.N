from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from models.models import Character, Quest, Setting

db = SQLAlchemy()

class Player(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    games = db.relationship('PlayerGame', backref='player', lazy=True)

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    players = db.relationship('PlayerGame', backref='game', lazy=True)

class PlayerGame(db.Model):
    player_id = db.Column(db.Integer, db.ForeignKey('player.id'), primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'), primary_key=True)
