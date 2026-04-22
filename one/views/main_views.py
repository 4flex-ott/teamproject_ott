
from flask import Blueprint, redirect, render_template, url_for, session, flash
from ..models import Video, Plan

bp = Blueprint('home', __name__, url_prefix='/')



@bp.route('/')
def index():
    if session.get('user'):   # 🔥 로그인 상태 체크
        return redirect(url_for('home.main'))
    return render_template('main/home.html')

@bp.route('/home')
def home():
    video_list = Video.query.order_by(Video.video_unique_id.desc()).all()
    plan_list = Plan.query.order_by(Plan.price.asc()).all()
    return render_template('main/home.html', video_list=video_list,
                           plans=plan_list)


@bp.route('/main')
def main():
    video_list = Video.query.order_by(Video.video_unique_id.desc()).all()
    
    # 2. 템플릿에 video_list 데이터를 전달합니다.
    # 기존에 'main.html'을 사용 중이라면 아래와 같이 작성합니다.
    return render_template('main/main.html', video_list=video_list)

@bp.route('/movie')
def movie():
    return render_template('main/movie.html')

@bp.route('/drama')
def drama():
    # DB에서 드라마 데이터만 가져오기 (예시)
    return render_template('main/drama.html')

@bp.route('/entertainment')
def entertainment():
    return render_template('main/entertainment.html')

@bp.route('/anime')
def anime():
    return render_template('main/anime.html')


@bp.route('/support_check')
def support_check():
    # 1. 세션에 유저 정보가 있는지 확인
    if session.get('user'):
        # 2. 로그인 상태면 고객센터 페이지로 (mypage 블루프린트의 support_center 함수)
        return redirect(url_for('mypage.support_center'))
    else:
        # 3. 로그인 안 되어 있으면 로그인 페이지로 (auth 블루프린트의 login 함수)
        flash("로그인이 필요한 서비스입니다.", "info")
        return redirect(url_for('auth.login'))


