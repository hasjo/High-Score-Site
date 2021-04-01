from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, ValidationError, Regexp

class TimeSubmit(FlaskForm):
    choices = []
    regexstring = '^(?:(?:((\d*):)?([0-5]?\d):)?([0-5]?\d)(\.\d*)?)$'
    username = StringField(label='Username',
                           validators=[DataRequired(message="Enter your username")])
    secret_code = PasswordField(label='Secret Code',
                              validators=[DataRequired(message="Enter your secret code")])
    track = SelectField(label='Track',
                        choices=choices)
    time = StringField('Time', validators=[Regexp(regexstring, message="Needs to be a valid time")])
    lap1 = StringField('Lap 1', validators=[Regexp(regexstring, message="Needs to be a valid time")])
    lap2 = StringField('Lap 2', validators=[Regexp(regexstring, message="Needs to be a valid time")])
    lap3 = StringField('Lap 3', validators=[Regexp(regexstring, message="Needs to be a valid time")])
    proof = StringField('Proof URL', validators=[DataRequired(message="Need proof link plz")])

class UserEdit(FlaskForm):
    username = StringField(label='Username',
                           validators=[DataRequired(message="Enter your username")])
    secret_code = PasswordField(label='Secret Code',
                              validators=[DataRequired(message="Enter your secret code")])
    new_name = StringField('New Display Name')
    new_pass1 = PasswordField('New Password')
    new_pass2 = PasswordField('Confirm New Password')

class SelectForm(FlaskForm):
    choices = []
    field = SelectField(label='Select', choices=choices)
