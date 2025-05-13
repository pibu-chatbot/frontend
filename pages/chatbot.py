import streamlit as st
import requests

st.set_page_config(
    page_title="Piboo-chat",
    page_icon="🌸",
    layout="centered",
    initial_sidebar_state="collapsed"
)

query = st.text_input("질문을 입력하세요: ")

if st.button("질문하기") and query.strip():
    with st.spinner("답변 생성 중..."):
        try:
            response = requests.post(
                "http://localhost:8000/ask",
                json={"query": query}
            )
            if response.status_code == 200:
                st.success("✅ 답변:")
                st.write(response.json().get("answer", "답변이 없습니다."))
            else:
                st.error("❌ 오류 발생: 백엔드 상태 확인")
        except Exception as e:
            st.error(f"❌ 요청 실패: {e}")