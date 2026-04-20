from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('one.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    # 모든 비디오 데이터를 가져옵니다.
    # 실무에서는 카테고리별로 쿼리를 나누겠지만, 여기서는 전체를 가져와 출력하는 예시입니다.
    videos = conn.execute('SELECT * FROM video').fetchall()
    conn.close()
    return render_template('main.html', videos=videos)