from flask import render_template, url_for, flash, redirect, request
from app import app, db, bcrypt
from app.forms import RegistrationForm, LoginForm, GameForm
from app.models import Player, Game, PlayerGame
from flask_login import login_user, current_user, logout_user, login_required

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        player = Player.query.filter_by(username=form.username.data).first()
        if player and bcrypt.check_password_hash(player.password, form.password.data):
            login_user(player)
            return redirect(url_for('index'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        player = Player(username=form.username.data, password=hashed_password)
        db.session.add(player)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/stats')
@login_required
def stats():
    return render_template('stats.html')

@app.route('/games', methods=['GET', 'POST'])
@login_required
def games():
    form = GameForm()
    if form.validate_on_submit():
        game = Game(name=form.name.data, description=form.description.data)
        db.session.add(game)
        db.session.commit()
        flash('Game has been created!', 'success')
        return redirect(url_for('games'))
    games = Game.query.all()
    return render_template('games.html', form=form, games=games)

@app.route('/join_game/<int:game_id>')
@login_required
def join_game(game_id):
    game = Game.query.get_or_404(game_id)
    if not PlayerGame.query.filter_by(player_id=current_user.id, game_id=game.id).first():
        player_game = PlayerGame(player_id=current_user.id, game_id=game.id)
        db.session.add(player_game)
        db.session.commit()
        flash('You have joined the game!', 'success')
    return redirect(url_for('games'))
