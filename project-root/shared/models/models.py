from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Text, create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
db = SQLAlchemy()

DATABASE_URL = "postgresql://user:password@db:5432/gamedb"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Player(db.Model):
    __tablename__ = "player"
    id = db.Column(db.Integer, primary_key=True, index=True)
    username = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(60), nullable=False)

class PlayerGame(db.Model):
    __tablename__ = "player_game"
    player_id = db.Column(db.Integer, ForeignKey('player.id'), primary_key=True)
    game_id = db.Column(db.Integer, ForeignKey('game.id'), primary_key=True)

class Character(db.Model):
    __tablename__ = "characters"
    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String(200), nullable=False, index=True)
    sex = db.Column(db.String(50), nullable=False, index=True)  # Increased length
    age = db.Column(db.String(50), nullable=False, index=True)  # Increased length
    traits = db.Column(db.Text, nullable=False)
    behaviors = db.Column(db.Text, nullable=False)
    background_summary = db.Column(db.Text, nullable=False)
    book_title = db.Column(db.String(200), nullable=True, index=True)
    author = db.Column(db.String(200), nullable=True, index=True)
    dialogue_examples = db.Column(db.Text, nullable=True)
    genre = db.Column(db.String(100), nullable=True, index=True)

class Quest(db.Model):
    __tablename__ = "quests"
    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String(200), nullable=False, index=True)
    storyline_summary = db.Column(db.Text, nullable=False)
    expected_gameplay_duration = db.Column(db.String(50), nullable=False)
    book_title = db.Column(db.String(200), nullable=True, index=True)
    author = db.Column(db.String(200), nullable=True, index=True)
    genre = db.Column(db.String(100), nullable=True, index=True)

class Setting(db.Model):
    __tablename__ = "setting"
    id = db.Column(db.Integer, primary_key=True, index=True)
    key = db.Column(db.String(50), nullable=False, unique=True)
    value = db.Column(db.Text, nullable=False)

class Game(db.Model):
    __tablename__ = "game"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)

Base.metadata.create_all(bind=engine)
