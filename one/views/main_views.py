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
    video_list = Video.query.order_by(Video.video_unique_id.desc()).all()
    return render_template('main/main.html', video_list=video_list)