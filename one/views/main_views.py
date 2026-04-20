from flask import Blueprint, redirect, render_template, url_for

bp=Blueprint('home',__name__,url_prefix='/')

@bp.route('/')
def index():
    # 127.0.0.1:5000/ 접속 시 바로 templates/main/home.html을 보여줍니다.
    return render_template('main/home.html')

@bp.route('/home')
def home():
    # 127.0.0.1:5000/home 접속 시에도 같은 페이지를 보여주고 싶을 경우
    return render_template('main/home.html')

@bp.route('/main')
def main():
    return render_template('main/main.html')

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

