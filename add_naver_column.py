import sqlite3

conn = sqlite3.connect('one.db') 
cur = conn.cursor()

try:
    cur.execute("ALTER TABLE user ADD COLUMN naver_id VARCHAR(100)")
    conn.commit()
    print("naver_id 컬럼 추가 완료")
except Exception as e:
    print("오류:", e)
finally:
    conn.close()