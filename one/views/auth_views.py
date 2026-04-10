from flask import Blueprint, session, render_template, redirect
from one.forms import LoginForm, UserCreateForm

bp = Blueprint('auth', __name__, url_prefix='/')


@bp.route('/signup', methods=['GET', 'POST'])
def signup():
    form = UserCreateForm()
    if form.validate_on_submit():
        # 사용자가 입력한 데이터 가져오기
        email = form.email.data
        password = form.password.data
        # TODO: 데이터베이스에 사용자 저장 로직 추가 (예: User 모델 생성 및 저장)
        # 가입 완료 후 로그인 페이지로 이동
        return redirect(url_for('auth.login'))
    # 폼 객체를 템플릿에 전달
    return render_template('auth/signup.html', form=form)


@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        # TODO: DB 확인
        session['user'] = username
        return "로그인 성공"
    return render_template('auth/login.html', form=form)


@bp.route('/logout')
def logout():
    session.clear()
