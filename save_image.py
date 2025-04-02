import os
import time
import json
from PIL import UnidentifiedImageError


def save_history(filename, timestamp, template, texts, log_path="./history.json"):
    log_entry = {
        "filename": filename,
        "create_time": timestamp,
        "template": template,
        "texts": texts
    }

    try:
        # 기존 로그 불러오기
        if os.path.exists(log_path):
            with open(log_path, "r", encoding="utf-8") as f:
                try:
                    logs = json.load(f)
                except json.JSONDecodeError:
                    logs = []
        else:
            logs = []

        # 로그 추가
        logs.append(log_entry)

        # 로그 다시 저장
        with open(log_path, "w", encoding="utf-8") as f:
            json.dump(logs, f, indent=4, ensure_ascii=False)

        print(f"📘 로그 저장 완료: {log_path}")
        return log_path

    except Exception as e:
        print(f"❌ 로그 저장 실패! 에러: {e}")
        return None



def save_image_and_log(meme_image, template, texts):
    # 출력 경로 설정, 폴더가 없을 경우 생성
    save_dir = "./outputs"
    os.makedirs(save_dir, exist_ok=True)

    # 생성시간
    timestamp = time.strftime("%Y%m%d_%H%M%S", time.localtime())
    filename = f"{template}_{timestamp}.png"

    filepath = os.path.join(save_dir, filename)

    try:
        meme_image.save(filepath)
        print(f"✅ 파일 저장 성공: {filepath}")
        save_history(filename=filename, timestamp=timestamp, template=template, texts=texts)
        return filepath
    except (OSError, ValueError, UnidentifiedImageError) as e:
        print(f"❌ 파일 저장 실패! 에러: {e}")
        return None