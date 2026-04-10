from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField
from wtforms.validators import DataRequired,Email,Length


class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])


class UserCreateForm(FlaskForm):
    email = EmailField('이메일', validators=[
        DataRequired('이메일은 필수 입력 항목입니다.'),
        Email('유효한 이메일 형식이 아닙니다.')
    ])
    password = PasswordField('비밀번호', validators=[
        DataRequired('비밀번호는 필수 입력 항목입니다.'),
        Length(min=8, max=20, message='비밀번호는 8자 이상 20자 이하로 입력해주세요.')
    ])
