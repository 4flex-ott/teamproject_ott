import os
import uuid
from datetime import datetime

from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app
from werkzeug.utils import secure_filename

from .. import db
from ..models import Video

bp = Blueprint('video', __name__, url_prefix='/video')

# 파일 확장자 검사
ALLOWED_VIDEO_EXTENSIONS = {'mp4'}
ALLOWED_IMAGE_EXTENSIONS = {'png', 'jpg', 'jpeg', 'webp'}


def allowed_file(filename, allowed_extensions):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions


# 콘텐츠 등록
@bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':

        # 1. 폼 데이터 받기
        video_title = request.form.get('video_title')
        video_director = request.form.get('video_director')
        video_actor = request.form.get('video_actor')
        video_age_limit = request.form.get('video_age_limit')
        video_date = request.form.get('video_date')
        video_synopsis = request.form.get('video_synopsis')
        video_genres = request.form.get('video_genres')
        video_is_movie = request.form.get('video_is_movie')

        video_file = request.files.get('video_file')
        thumbnail_file = request.files.get('thumbnail_file')

        # 2. 필수값 체크
        if not video_title:
            flash('제목을 입력해주세요.')
            return redirect(request.url)

        if not video_file or video_file.filename == '':
            flash('동영상 파일을 선택해주세요.')
            return redirect(request.url)

        if not allowed_file(video_file.filename, ALLOWED_VIDEO_EXTENSIONS):
            flash('mp4 파일만 업로드 가능합니다.')
            return redirect(request.url)

        # 3. 썸네일 처리
        thumbnail_path = None

        if thumbnail_file and thumbnail_file.filename != '':
            if not allowed_file(thumbnail_file.filename, ALLOWED_IMAGE_EXTENSIONS):
                flash('썸네일은 이미지 파일만 가능합니다.')
                return redirect(request.url)

            thumb_ext = thumbnail_file.filename.rsplit('.', 1)[1].lower()
            thumb_filename = f"{uuid.uuid4()}.{thumb_ext}"

            thumb_save_path = os.path.join(
                current_app.config['UPLOAD_FOLDER_THUMBNAILS'],
                thumb_filename
            )
            thumbnail_file.save(thumb_save_path)

            thumbnail_path = f"/static/uploads/thumbnails/{thumb_filename}"

        # 4. 영상 파일 저장
        video_ext = video_file.filename.rsplit('.', 1)[1].lower()
        video_filename = f"{uuid.uuid4()}.{video_ext}"

        video_save_path = os.path.join(
            current_app.config['UPLOAD_FOLDER_VIDEOS'],
            video_filename
        )
        video_file.save(video_save_path)

        video_path = f"/static/uploads/videos/{video_filename}"

        # 5. 날짜 처리
        parsed_date = None
        if video_date:
            parsed_date = datetime.strptime(video_date, '%Y-%m-%d')

        # 6. DB 저장
        new_video = Video(
            video_title=video_title,
            video_director=video_director,
            video_actor=video_actor,
            video_url=video_path,  # 업로드 파일 경로 저장
            video_thumbnail=thumbnail_path,  # 썸네일 경로 저장
            video_date=parsed_date,
            video_age_limit=video_age_limit,
            video_synopsis=video_synopsis,
            video_is_movie=True if video_is_movie == 'True' else False,
            video_genres=video_genres,

            # ⚠️ 임시값 (나중에 로그인 관리자 연결)
            admin_unique_id=1
        )

        db.session.add(new_video)
        db.session.commit()

        flash('동영상이 등록되었습니다.')
        return redirect(url_for('video.list'))

    return render_template('admin/content_form.html', mode='create', content=None)


# 목록 페이지
@bp.route('/list')
def list():
    video_list = Video.query.order_by(Video.video_unique_id.desc()).all()
    return render_template('main.html', video_list=video_list)


# 상세(재생) 페이지
@bp.route('/detail/<int:video_id>')
def detail(video_id):
    video = Video.query.get_or_404(video_id)
    return render_template('video_detail.html', video=video)
