from flask import render_template, request, redirect, url_for, flash
from app import app, db

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         # Handle login
#         return redirect(url_for('index'))
#     return render_template('login.html')

# @app.route('/stats')
# def stats():
#     player_stats = db.session.execute('SELECT * FROM player_stats').fetchall()
#     return render_template('stats.html', stats=player_stats)
