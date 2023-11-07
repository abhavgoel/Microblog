from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import DataRequired,ValidationError,Email,EqualTo
from app.models import User

class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Sign in')

class RegisterForm(FlaskForm):
    username = StringField('username',validators=[DataRequired()])
    email = StringField('email',validators=[DataRequired(),Email()])
    password = PasswordField('password',validators=[DataRequired()])
    password2 = PasswordField('Re-enter password',validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self,username): # check for duplicate user
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError("This username is already taken")
    
    def validate_email(self,email):#check for duplicate email
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError("This Email is already taken")



