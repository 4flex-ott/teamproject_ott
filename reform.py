import os


def rename_contents():
    # 1. 파일들이 들어있는 폴더 경로를 입력하세요. (예: './static/data')
    target_folder = 'one/static/text'

    # 2. 바꿀 규칙 설정 (기존 단어: 바꿀 단어)
    replace_rules = {
        "TVING": "4FLEX",
        "tving": "4FLEX",
        "티빙": "넷플렉스"
    }

    # 폴더 내 파일 탐색
    if not os.path.exists(target_folder):
        print("❌ 폴더 경로를 찾을 수 없습니다. 경로를 확인해주세요.")
        return

    for filename in os.listdir(target_folder):
        if filename.endswith('.txt'):  # 텍스트 파일만 대상
            file_path = os.path.join(target_folder, filename)

            # 파일 읽기
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                # 규칙대로 단어 치환
                new_content = content
                changed = False

                for old, new in replace_rules.items():
                    if old in new_content:
                        new_content = new_content.replace(old, new)
                        changed = True

                # 변경 사항이 있을 때만 파일 저장
                if changed:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"✅ 수정 완료: {filename}")
                else:
                    print(f"➖ 변경사항 없음: {filename}")

            except Exception as e:
                print(f"❌ 에러 발생 ({filename}): {e}")


if __name__ == "__main__":
    rename_contents()