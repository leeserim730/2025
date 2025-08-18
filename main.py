import streamlit as st

# 페이지 설정
st.set_page_config(page_title="MBTI Career Recommender", layout="centered")

# CSS 스타일 (흑백 세련된 테마)
st.markdown("""
    <style>
    body {
        background-color: black;
        color: white;
        font-family: 'Helvetica Neue', sans-serif;
    }
    .stSelectbox label, .stRadio label, .stMarkdown, .stSubheader {
        color: white !important;
    }
    .job-card {
        background-color: #1a1a1a;
        padding: 20px;
        border-radius: 12px;
        margin: 10px 0;
        box-shadow: 0px 4px 12px rgba(255, 255, 255, 0.1);
    }
    </style>
""", unsafe_allow_html=True)

# 상단 리키 이미지 (흑백)
st.image("https://i.imgur.com/dkN0r8b.jpeg", use_column_width=True)  # 리키 흑백 사진 URL

st.title("🎯 MBTI 기반 진로 추천")
st.write("제로베이스원 리키와 함께하는 진로 탐색")

# MBTI 직업 매핑 데이터
mbti_jobs = {
    "INTJ": ["연구원", "전략 기획자", "데이터 과학자"],
    "ENFP": ["마케터", "강사", "콘텐츠 크리에이터"],
    "ISTJ": ["공무원", "회계사", "엔지니어"],
    "ESFP": ["배우", "이벤트 플래너", "영업 전문가"],
    # 필요에 따라 추가
}

# MBTI 선택
user_mbti = st.selectbox("당신의 MBTI를 선택하세요", options=mbti_jobs.keys())

# 결과 출력
if user_mbti:
    st.subheader(f"✨ {user_mbti} 유형 추천 직업 ✨")
    for job in mbti_jobs[user_mbti]:
        st.markdown(f"""
        <div class="job-card">
            <b>{job}</b>
        </div>
        """, unsafe_allow_html=True)
