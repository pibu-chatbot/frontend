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
st.markdown(f"""
    <style>
    .phone {{
        width: 320px;
        height: 640px;
        margin: 50px auto;
        border-radius: 40px;
        background-color: #f9f9f9;
        box-shadow: 0 0 15px rgba(0,0,0,0.1);
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        align-items: center;
        padding: 60px 20px 40px;
        position: relative;
        text-align: center;
    }}
    .logo {{
        width: 120px;
        height: auto;
        margin-top: 40px;
    }}
    .brand {{
        font-size: 28px;
        font-weight: bold;
        color: #ff3b5c;
        margin-top: 20px;
    }}
    .start-btn {{
        background-color: #ff3b5c;
        color: white;
        padding: 14px 32px;
        font-size: 18px;
        font-weight: bold;
        border: none;
        border-radius: 25px;
        cursor: pointer;
        margin-bottom: 20px;
    }}
    .start-btn:hover {{
        background-color: #e93555;
    }}
    </style>

    <div class="phone">
        <div>
            <img src="data:image/png;base64,{base64_logo}" class="logo" />
            <div class="brand">Piboo</div>
        </div>
        <form action="/" method="post">
            <button class="start-btn" type="submit">시작하기</button>
        </form>
    </div>
""", unsafe_allow_html=True)
