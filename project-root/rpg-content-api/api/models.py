from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

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
