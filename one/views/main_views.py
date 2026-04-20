from flask import Blueprint, render_template
from ..models import Video

bp = Blueprint('home', __name__, url_prefix='/')


@bp.route('/')
def index():
    video_list = Video.query.order_by(Video.video_unique_id.desc()).all()
    return render_template('main/home.html', video_list=video_list)


@bp.route('/home')
def home():
    video_list = Video.query.order_by(Video.video_unique_id.desc()).all()
    return render_template('main/home.html', video_list=video_list)


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


