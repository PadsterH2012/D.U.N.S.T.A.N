from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=50)])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class GameForm(FlaskForm):
    name = StringField('Game Name', validators=[DataRequired(), Length(min=2, max=100)])
    description = TextAreaField('Description', validators=[DataRequired()])
    submit = SubmitField('Create Game')

class SettingForm(FlaskForm):
    ollama_url = StringField('Ollama URL', validators=[DataRequired(), Length(max=200)])
    model = StringField('Model', validators=[DataRequired(), Length(max=200)])
    submit = SubmitField('Save Settings')

class BackupForm(FlaskForm):
    submit_backup = SubmitField('Backup Settings')
    submit_restore = SubmitField('Restore Settings')
