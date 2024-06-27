from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Character(db.Model):
    __tablename__ = 'characters'  # Make sure to use the correct table name
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


    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'sex': self.sex,
            'age': self.age,
            'traits': self.traits,
            'behaviors': self.behaviors,
            'background_summary': self.background_summary,
            'book_title': self.book_title,
            'author': self.author,
            'dialogue_examples': self.dialogue_examples,
            'genre': self.genre,
        }

class Quest(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String(200), nullable=False, index=True)
    storyline_summary = db.Column(db.Text, nullable=False)
    expected_gameplay_duration = db.Column(db.String(50), nullable=False)
    book_title = db.Column(db.String(200), nullable=True, index=True)
    author = db.Column(db.String(200), nullable=True, index=True)
    genre = db.Column(db.String(100), nullable=True, index=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'storyline_summary': self.storyline_summary,
            'expected_gameplay_duration': self.expected_gameplay_duration,
            'book_title': self.book_title,
            'author': self.author,
            'genre': self.genre,
        }
