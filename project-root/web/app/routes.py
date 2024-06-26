from flask import render_template, url_for, flash, redirect, request, send_file
from app import app, db, bcrypt
from app.forms import RegistrationForm, LoginForm, GameForm, SettingForm, BackupForm
from app.models import Player, Game, PlayerGame, Setting
from flask_login import login_user, current_user, logout_user, login_required
import json
import io

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('welcome'))
    form = LoginForm()
    if form.validate_on_submit():
        player = Player.query.filter_by(username=form.username.data).first()
        if player and bcrypt.check_password_hash(player.password, form.password.data):
            login_user(player)
            return redirect(url_for('welcome'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('welcome'))
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

@app.route('/welcome')
@login_required
def welcome():
    return render_template('welcome.html')

@app.route('/settings', methods=['GET', 'POST'])
@login_required
def settings():
    form = SettingForm()
    backup_form = BackupForm()

    if form.validate_on_submit():
        ollama_url = Setting.query.filter_by(key='ollama_url').first()
        ollama_model = Setting.query.filter_by(key='ollama_model').first()

        if not ollama_url:
            ollama_url = Setting(key='ollama_url', value=form.ollama_url.data)
        else:
            ollama_url.value = form.ollama_url.data

        if not ollama_model:
            ollama_model = Setting(key='ollama_model', value=form.ollama_model.data)
        else:
            ollama_model.value = form.ollama_model.data

        db.session.add(ollama_url)
        db.session.add(ollama_model)
        db.session.commit()
        flash('Settings have been saved!', 'success')
        return redirect(url_for('settings'))

    elif backup_form.submit_backup.data:
        settings = Setting.query.all()
        settings_data = {setting.key: setting.value for setting in settings}
        buffer = io.StringIO()
        json.dump(settings_data, buffer)
        buffer.seek(0)
        return send_file(io.BytesIO(buffer.getvalue().encode()), mimetype='application/json', as_attachment=True, attachment_filename='settings_backup.json')

    elif backup_form.submit_restore.data:
        file = request.files['file']
        if file:
            settings_data = json.load(file)
            for key, value in settings_data.items():
                setting = Setting.query.filter_by(key=key).first()
                if not setting:
                    setting = Setting(key=key, value=value)
                else:
                    setting.value = value
                db.session.add(setting)
            db.session.commit()
            flash('Settings have been restored!', 'success')
            return redirect(url_for('settings'))

    if request.method == 'GET':
        ollama_url = Setting.query.filter_by(key='ollama_url').first()
        ollama_model = Setting.query.filter_by(key='ollama_model').first()

        if ollama_url:
            form.ollama_url.data = ollama_url.value
        if ollama_model:
            form.ollama_model.data = ollama_model.value

    return render_template('settings.html', form=form, backup_form=backup_form)
