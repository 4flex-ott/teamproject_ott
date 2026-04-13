from one import db
from datetime import datetime, timezone


# https://blog.naver.com/red0808/223888577210
class users(db.Model):
    __tablename__ = 'user'
    # 프라이머리 키
    user_unique_id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)

    # 사용자 기본 정보
    user_id = db.Column(db.String(50), unique=True, nullable=False)  # 로그인 아이디
    user_password = db.Column(db.String(255), nullable=False)  # 암호화된 비번
    user_email = db.Column(db.String(100), unique=True, nullable=False)  # 이메일
    user_name = db.Column(db.String(50), nullable=False)  # 이름
    user_birth = db.Column(db.Date)  # 생년월일
    user_gender = db.Column(db.String(10))  # 성별 (M/F 등)

    # --- 관계 설정 (Relationship) ---
    # 다른 테이블에서 이 사용자를 참조할 때 편리하게 가져오기 위함입니다.

    # 1:N 관계 (구독, 시청기록, 리뷰, 문의 등)
    subscriptions = db.relationship('Subscription', backref='user', lazy=True)
    watch_histories = db.relationship('WatchHistory', backref='user', lazy=True)
    reviews = db.relationship('Review', backref='user', lazy=True)
    supports = db.relationship('Support', backref='user', lazy=True)
    payments = db.relationship('Payment', backref='user', lazy=True)
    # backref -> 역참조 : 리뷰 입장에서 작성자를 바로 알고 싶거나 할때 사용
    # lazy : 성능을 위한 설정. 예를들어 유저 정보를 불러올 때 오든 리뷰, 시청기록 등을 다 가져오지 말고
    # 필요할때, 호출을 직접 할때만 DB에서 가져오라는 뜻

    # 찜하기 & 좋아요 (M:N 성격의 1:N)
    likes = db.relationship('VideoLike', backref='user', lazy=True)
    wishlist = db.relationship('VideoWish', backref='user', lazy=True)

    # __repr__ 매직메서드중 하나 : 객체를 출력했을 때 어떻게 보여줄 것인지.
    # 예를들어 print(user)를 할 경우 메모리 주소값이 나오게 되는데 이 함수가 있으면 f-string를 통해 user아이디를 보여준다.
    # 관례적으로 개발자가 코드를 짜고 디버깅할 때 편하기 위해 꼭 넣는 코드라 해서 넣어봄
    def __repr__(self):
        return f'<User {self.user_id}>'

    # 1. 연결 테이블 (M:N 관계의 징검다리)
    # 실제 클래스로 만들지 않고 db.Table을 사용하는 것이 조인(Join) 시 성능과 관리에 유리.


video_genres = db.Table('video_genres',
                        db.Column('video_unique_id', db.BigInteger, db.ForeignKey('video.video_unique_id'),
                                  primary_key=True),
                        db.Column('genre_id', db.Integer, db.ForeignKey('genre.genre_id'), primary_key=True)
                        )


class Video(db.Model):
    # 프라이머리 키
    video_unique_id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)

    # 영상 상세 정보 (이미지의 컬럼 반영)
    video_title = db.Column(db.String(200), nullable=False)  # 제목
    video_director = db.Column(db.String(100))  # 감독
    video_actor = db.Column(db.String(255))  # 출연진
    video_url = db.Column(db.String(500), nullable=False)  # 실제 영상 주소
    video_thumbnail = db.Column(db.String(500), nullable=False)  # 썸네일 이미지 주소
    video_date = db.Column(db.Date)  # 개봉/등록 날짜
    video_age_limit = db.Column(db.String(20))  # 시청 등급 (예: 15세, All)
    video_synopsis = db.Column(db.Text)  # 줄거리요약

    # --- 관계 설정 (Relationship) ---

    # 1. 장르와 다대다(M:N) 연결
    # secondary 설정을 통해 미리 만들어둔 video_genres 테이블을 거쳐 Genre 테이블과 연결됩니다.
    # lazy='dynamic' 데이터를 가져오기전 추가 조건을 걸 수 있는 쿼리형태로 넘어옴.(데이터가 많을 경우 최적화를 위해 사용)
    # True같은 경우 파이썬 리스트로 넘어옴.
    genres = db.relationship('Genre', secondary=video_genres, backref=db.backref('videos', lazy='dynamic'))

    # 2. 1:N 관계 (시청 기록, 리뷰, 좋아요, 찜하기 등)
    watch_histories = db.relationship('WatchHistory', backref='video', lazy=True)
    reviews = db.relationship('Review', backref='video', lazy=True)
    likes = db.relationship('VideoLike', backref='video', lazy=True)
    wishlist = db.relationship('VideoWish', backref='video', lazy=True)

    def __repr__(self):
        return f'<Video {self.video_title}>'


# 2. 장르 테이블
class Genre(db.Model):
    genre_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    genre_name = db.Column(db.String(50), unique=True, nullable=False)  # 액션, 로맨스, SF 등

    def __repr__(self):
        return f'<Genre {self.genre_name}>'


class VideoLike(db.Model):

    # 프라이머리 키
    like_id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)

    # 외래키 연결 (누가, 어떤 영상에)
    user_unique_id = db.Column(db.BigInteger, db.ForeignKey('user.user_unique_id'), nullable=False)
    video_unique_id = db.Column(db.BigInteger, db.ForeignKey('video.video_unique_id'), nullable=False)

    # 생성일 (언제 눌렀는지)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
