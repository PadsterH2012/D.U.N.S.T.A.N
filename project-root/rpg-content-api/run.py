from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@db:5432/gamedb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Import your models here to make sure Alembic detects them
from models.models import Character, Quest, Setting, Player, PlayerGame, Game

@app.route('/health')
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
