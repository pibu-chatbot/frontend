import streamlit as st
import streamlit.components.v1 as components
import base64

st.set_page_config(page_title="Piboo-chat", page_icon="🌸", layout="centered")

def get_base64_image(img_path):
    with open(img_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

logo_base64 = get_base64_image("intro.png")

# HTML 파일 읽기
with open("./pages/ui.html", "r", encoding="utf-8") as f:
    html_code = f.read()

# 플레이스홀더 치환
html_code = html_code.replace("LOGO_BASE64_PLACEHOLDER", logo_base64)

# Streamlit에서 렌더링
components.html(html_code, height=700, scrolling=False)
