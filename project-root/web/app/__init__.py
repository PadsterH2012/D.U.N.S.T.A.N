from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@db:5432/gamedb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'auth.login'
login_manager.login_message_category = 'info'

from app import models

@login_manager.user_loader
def load_user(user_id):
    return models.Player.query.get(int(user_id))

# Import and register blueprints
from app.auth_routes import auth as auth_blueprint
app.register_blueprint(auth_blueprint, url_prefix='/auth')

from app.settings_routes import settings as settings_blueprint
app.register_blueprint(settings_blueprint, url_prefix='/settings')

from app.upload_routes import upload as upload_blueprint
app.register_blueprint(upload_blueprint, url_prefix='/upload')

from app.main_routes import main as main_blueprint
app.register_blueprint(main_blueprint, url_prefix='/')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
