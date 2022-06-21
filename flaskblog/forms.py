from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,TextAreaField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired,Length,EqualTo,ValidationError
# from wtforms import ValidationError
from flask_login import current_user
from flaskblog.models import User

class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired(),Length(min=8)])
    Confirm_password = PasswordField('Confirm Password',validators=[DataRequired(),Length(min=8),EqualTo('password')])
    remember = BooleanField('Remember Me')
    Submit = SubmitField('Log In')


class RegistrationForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    Last_name = StringField('Last Name', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired(),Length(min=2,max=20)])
    email = StringField('Email',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired(),Length(min=8)])
    Confirm_password = PasswordField('Confirm Password',validators=[DataRequired(),Length(min=8),EqualTo('password')])
    Submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose another username')


    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose another email')

class UpdateAccountForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    Last_name = StringField('Last Name', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired(),Length(min=2,max=20)])
    email = StringField('Email',validators=[DataRequired()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed([ 'jpg', 'png' ])])
    Submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:

            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. Pls choose another username')
    
    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Pls choose another email')

class PostForm(FlaskForm):
    title = StringField('Title' , validators = [DataRequired()])
    content = TextAreaField('Content' , validators = [DataRequired()])
    Submit = SubmitField('Create Post')

class UpdatePostForm(FlaskForm):
    title = StringField('Title' , validators = [DataRequired()])
    content = TextAreaField('Content' , validators = [DataRequired()])
    Submit = SubmitField('Create Post')

class RequestResetForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    Submit = SubmitField('Request Password Reset')
    def validate_email(self, email):
        # if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user is None:
                raise ValidationError('There is no account with that email.You must register first')

class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired(),Length(min=8)])
    Confirm_password = PasswordField('Confirm Password',validators=[DataRequired(),Length(min=8),EqualTo('password')])
    Submit = SubmitField('Reset Password')
