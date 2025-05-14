import streamlit as st
import base64
from style import get_intro_style

# 1. 페이지 설정
st.set_page_config(
    page_title="PiBoo",
    page_icon="🌸",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. 이미지 → Base64 변환 함수
def get_base64_image(img_path):
    with open(img_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# 3. 로고 이미지 경로 및 base64 변환
img_path = "intro.png"  # ← 업로드된 파일명으로 변경!
base64_logo = get_base64_image(img_path)

# 4. UI 구성
style_html = get_intro_style(base64_logo)
st.markdown(style_html, unsafe_allow_html=True)

# 버튼 배치
with st.container():
    st.markdown("<div>", unsafe_allow_html=True)
    if st.button("시작하기"):
        st.switch_page("pages/chatbot.py")
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)