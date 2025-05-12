import streamlit as st
import base64

# 1. 페이지 설정
st.set_page_config(
    page_title="Piboo",
    page_icon="🌸",
    layout="centered"
)

# 2. 이미지 → Base64 변환 함수
def get_base64_image(img_path):
    with open(img_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# 3. 로고 이미지 경로 및 base64 변환
img_path = "frontend/intro.png"  # ← 업로드된 파일명으로 변경!
base64_logo = get_base64_image(img_path)

# 4. UI 구성
st.markdown(css, unsafe_allow_html=True)
