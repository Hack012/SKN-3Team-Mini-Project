import streamlit as st
from streamlit_image_select import image_select
import os
from PIL import Image, UnidentifiedImageError

# 📁 이미지 폴더 경로
TEMPLATE_DIR = "images"

template_map = {
    "drake.jpg": "드레이크 HotBling밈",
    "fry.png": "닥치고 내돈 가져가 밈",
    "muscle.jpg": "공부는 접는다 밈",
    "squirrel.png": "람쥐썬더 밈",
    "chillguy.jpg": "chill guy 밈",
    "disappointed-guy.jpg": "실망한 남자 밈"
}

st.title("🖼️ 짤/밈 생성기 - 템플릿 클릭 선택")

# ✅ 실제 존재하는 유효한 이미지만 필터링
valid_images = []
valid_captions = []

for filename, label in template_map.items():
    image_path = os.path.join(TEMPLATE_DIR, filename)

    if not os.path.exists(image_path):
        st.warning(f"❗ 이미지 파일 없음: {filename}")
        continue

    try:
        # 이미지 유효성 체크
        with Image.open(image_path) as img:
            img.verify()
        valid_images.append(image_path)
        valid_captions.append(label)
    except UnidentifiedImageError:
        st.error(f"⚠️ 지원되지 않는 이미지 형식: {filename}")
    except Exception as e:
        st.error(f"❌ 오류 발생 ({filename}): {e}")

# 🚫 예외 처리: 유효한 이미지가 없을 경우
if not valid_images:
    st.error("❌ 사용할 수 있는 템플릿 이미지가 없습니다.\n📁 'images/' 폴더를 확인해주세요.")
    st.stop()

# ✅ 이미지 클릭 선택 기능
selected_image_path = image_select(
    label="💬 사용할 템플릿 이미지를 클릭하세요",
    images=valid_images,
    captions=valid_captions,
    use_container_width=False
)

# ✅ 선택된 이미지 표시
if selected_image_path:
    selected_name = os.path.basename(selected_image_path)
    st.markdown(f"### ✅ 선택된 템플릿: {template_map.get(selected_name, selected_name)}")
    st.image(selected_image_path, use_column_width=True)
    st.session_state["selected_template_path"] = selected_image_path
