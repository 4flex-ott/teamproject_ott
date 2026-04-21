from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, RadioField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from datetime import date, datetime
from wtforms.validators import Length, Regexp
from wtforms.validators import ValidationError
import re

from one.models import User


class LoginForm(FlaskForm):
    email = StringField('email', validators=[
        DataRequired(message="이메일을 입력해주세요."),
        Email(message="올바른 이메일 형식이 아닙니다.")
    ])
    password = PasswordField('password', validators=[
        DataRequired(message="비밀번호를 입력해주세요.")
    ])


class UserCreateForm(FlaskForm):
    # 기본 정보
    name = StringField('이름', validators=[
        DataRequired(message="이름을 입력해주세요.")
    ])

    email = StringField('이메일', validators=[
        DataRequired(message="이메일을 입력해주세요."),
        Email(message="올바른 이메일 형식이 아닙니다.")
    ])

    phone = StringField('휴대전화', validators=[
        DataRequired(message="휴대전화 번호를 입력해주세요.")
    ])

    # 비밀번호
    password1 = PasswordField('비밀번호', validators=[
        DataRequired(message="비밀번호를 입력해주세요."),
        Length(min=8, message="비밀번호는 8자 이상이어야 합니다."),
        Regexp(
            r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[!@#$%^&*]).+$',
            message="영문, 숫자, 특수문자를 모두 포함해야 합니다."
        )
    ])

    password2 = PasswordField(
        '비밀번호 확인',
        validators=[
            DataRequired(message="비밀번호 확인을 입력해주세요."),
            EqualTo('password1', message="비밀번호가 일치하지 않습니다.")
        ]
    )

    # 생년월일
    birth_year = SelectField(
        '연도',
        choices=[],
        validate_choice=False,
        validators=[DataRequired(message="연도를 선택해주세요.")]
    )

    birth_month = SelectField(
        '월',
        choices=[],
        validate_choice=False,
        validators=[DataRequired(message="월을 선택해주세요.")]
    )

    birth_day = SelectField(
        '일',
        choices=[],
        validate_choice=False,
        validators=[DataRequired(message="일을 선택해주세요.")]
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        current_year = datetime.now().year

        self.birth_year.choices = [('', '년도')] + [
            (str(y), str(y)) for y in range(current_year, 1949, -1)
        ]

        self.birth_month.choices = [('', '월')] + [
            (str(m), str(m)) for m in range(1, 13)
        ]

        self.birth_day.choices = [('', '일')] + [
            (str(d), str(d)) for d in range(1, 32)
        ]

    # 성별
    gender = RadioField(
        '성별',
        choices=[('M', '남자'), ('F', '여자')],
        validators=[DataRequired(message="성별을 선택해주세요.")]
    )

    # 이메일 중복 체크
    def validate_email(self, field):
        user = User.query.filter_by(user_email=field.data).first()
        if user:
            raise ValidationError("이미 사용 중인 이메일입니다.")

    # 나이 제한 체크 (14세)
    def validate_birth_year(self, field):
        if not (self.birth_year.data and self.birth_month.data and self.birth_day.data):
            raise ValidationError("생년월일을 모두 선택해주세요.")

        try:
            birth = date(
                int(self.birth_year.data),
                int(self.birth_month.data),
                int(self.birth_day.data)
            )
        except:
            raise ValidationError("올바른 생년월일을 선택해주세요.")

        today = date.today()
        age = today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))

        if age < 14:
            raise ValidationError("14세 미만은 가입할 수 없습니다.")


class FindIdForm(FlaskForm):
    name = StringField('이름', validators=[
        DataRequired(message="이름을 입력해주세요.")
    ])
    phone = StringField('휴대전화', validators=[
        DataRequired(message="휴대전화 번호를 입력해주세요.")
    ])


class ResetPasswordForm(FlaskForm):
    email = StringField('이메일', validators=[
        DataRequired(message="이메일을 입력해주세요."),
        Email(message="올바른 이메일 형식이 아닙니다.")
    ])

    name = StringField('이름', validators=[
        DataRequired(message="이름을 입력해주세요.")
    ])

    password1 = PasswordField('새 비밀번호', validators=[
        DataRequired(message="비밀번호를 입력해주세요.")
    ])

    password2 = PasswordField(
        '비밀번호 확인',
        validators=[
            DataRequired(message="비밀번호 확인을 입력해주세요."),
            EqualTo('password1', message="비밀번호가 일치하지 않습니다.")
        ]
    )

    # 🔥 여기 추가
    def validate_password1(self, field):
        pw = field.data

        if len(pw) < 8 or \
                not re.search(r'[A-Za-z]', pw) or \
                not re.search(r'[0-9]', pw) or \
                not re.search(r'[!@#$%^&*]', pw):
            raise ValidationError("영문, 숫자, 특수문자를 포함한 8자 이상으로 입력해주세요.")


class FindIdForm(FlaskForm):
    name = StringField('이름', validators=[DataRequired()])
    phone = StringField('휴대전화', validators=[DataRequired()])
