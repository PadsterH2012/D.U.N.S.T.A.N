from app import app
from database.models import db

# Create the database and the database table
with app.app_context():
    db.create_all()
    print('Database tables created')