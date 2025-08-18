import streamlit as st

# MBTI별 직업 추천 데이터 예시
mbti_jobs = {
    "INTJ": ["연구원", "전략 기획자", "데이터 과학자"],
    "ENFP": ["마케터", "강사", "콘텐츠 크리에이터"],
    "ISTJ": ["공무원", "회계사", "엔지니어"],
    "ESFP": ["배우", "이벤트 플래너", "영업 전문가"],
    # ... 나머지 MBTI 추가
}

st.set_page_config(page_title="MBTI 진로 추천", layout="centered")

st.title("🎯 MBTI 기반 진로 추천 웹 앱")
st.write("당신의 MBTI 유형을 선택하면 어울리는 직업을 추천해 드립니다!")

# 사용자 입력 (MBTI 선택)
user_mbti = st.selectbox(
    "당신의 MBTI를 선택하세요",
    options=mbti_jobs.keys()
)

# 추천 직업 출력
if user_mbti:
    st.subheader(f"✨ {user_mbti} 유형 추천 직업 ✨")
    for job in mbti_jobs[user_mbti]:
        st.markdown(f"- {job}")

