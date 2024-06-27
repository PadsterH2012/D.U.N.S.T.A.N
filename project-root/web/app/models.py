from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

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

class Setting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(50), nullable=False, unique=True)
    value = db.Column(db.String(200), nullable=False)

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String(200), nullable=False, index=True)
    sex = db.Column(db.String(10), nullable=False, index=True)
    age = db.Column(db.String(10), nullable=False, index=True)
    traits = db.Column(db.Text, nullable=False)
    behaviors = db.Column(db.Text, nullable=False)
    background_summary = db.Column(db.Text, nullable=False)
    book_title = db.Column(db.String(200), nullable=True, index=True)
    author = db.Column(db.String(200), nullable=True, index=True)
    dialogue_examples = db.Column(db.Text, nullable=True)
    genre = db.Column(db.String(100), nullable=True, index=True)

class Quest(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String(200), nullable=False, index=True)
    storyline_summary = db.Column(db.Text, nullable=False)
    expected_gameplay_duration = db.Column(db.String(50), nullable=False)
    book_title = db.Column(db.String(200), nullable=True, index=True)
    author = db.Column(db.String(200), nullable=True, index=True)
    genre = db.Column(db.String(100), nullable=True, index=True)
