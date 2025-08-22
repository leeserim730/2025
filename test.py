import streamlit as st

st.set_page_config(page_title="교사-학생 주제 추천", page_icon="🎓", layout="centered")

st.title("🎓 교사-학생 주제 추천 웹앱")

# 사용자 유형 선택
user_type = st.radio("👥 사용자 유형을 선택하세요", ["👩‍🏫 교사", "👩‍🎓 학생"])

if user_type == "👩‍🏫 교사":
    st.markdown("## 👩‍🏫 교사용 입력")
    subject = st.text_input("📚 과목/주제 입력 (예: 국어, 수학, 환경)")
    grade = st.selectbox("🏫 학년 선택", ["초등학교", "중학교", "고등학교"])
    goal = st.text_area("🎯 수업 목표 / 키워드")

    if st.button("✨ 추천 주제 생성"):
        if "국어" in subject:
            st.success("💡 추천 주제: 광고 속 설득 기법 분석하기 📺")
        elif "수학" in subject:
            st.success("💡 추천 주제: 피보나치 수열과 자연의 패턴 🌱")
        elif "환경" in subject:
            st.success("💡 추천 주제: 우리 지역 쓰레기 배출 현황 조사 ♻️")
        else:
            st.warning("🤔 입력한 과목/키워드에 맞는 주제를 준비 중입니다!")

elif user_type == "👩‍🎓 학생":
    st.markdown("## 👩‍🎓 학생용 입력")
    interest = st.text_input("💭 관심 분야 입력 (예: 과학, 음악, 인공지능)")
    style = st.selectbox("🎨 선호하는 활동 방식", ["탐구", "실험", "발표", "창작"])

    if st.button("✨ 추천 주제 받기"):
        if "과학" in interest:
            st.success("🔍 추천 주제: 일상생활 속 과학 원리 찾기 🔬")
        elif "음악" in interest:
            st.success("🎶 추천 주제: 좋아하는 음악 장르 분석 및 발표 🎤")
        elif "인공지능" in interest:
            st.success("🤖 추천 주제: AI가 바꾸는 미래 직업 탐구 📡")
        else:
            st.info("⏳ 관심 분야에 맞는 주제를 생성하고 있습니다...")
