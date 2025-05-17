import streamlit as st
import base64
from style.style import get_intro_style

def get_base64_image(img_path):
    with open(img_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

def main():
    st.set_page_config(
        page_title="PiBoo",
        page_icon="🌸",
        layout="centered",
        initial_sidebar_state="collapsed"
    )

    img_path = "intro.png"
    base64_logo = get_base64_image(img_path)

    style_html = get_intro_style(base64_logo)
    st.markdown(style_html, unsafe_allow_html=True)

    with st.container():
        st.markdown("<div>", unsafe_allow_html=True)
        if st.button("시작하기"):
            st.switch_page("pages/chatbot.py")
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

if __name__=='__main__':
    main()