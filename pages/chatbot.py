import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Piboo-chat", page_icon="🌸", layout="centered")

# HTML 파일 읽기
with open("./pages/ui.html", "r", encoding="utf-8") as f:
    html_code = f.read()

# Streamlit에서 렌더링
components.html(html_code, height=700, scrolling=False)
