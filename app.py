from flask import Flask, render_template
from database.models import db, Player

app = Flask(__name__)

# Configure the PostgreSQL database URI. This format is 'postgresql://<user>:<password>@<host>/<dbname>'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@db/mydb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # To suppress warning messages

# Initialize the SQLAlchemy object with the Flask app context
db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)