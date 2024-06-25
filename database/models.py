from flask_sqlalchemy import SQLAlchemy

# Initialize the SQLAlchemy object. This will be used to communicate with the database.
db = SQLAlchemy()

# Define the Player model that will represent the players' table in the database.
class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    health = db.Column(db.Integer, nullable=False)
    inventory = db.Column(db.String(200), nullable=True)

    def __repr__(self):
        return f'<Player {self.name}>'