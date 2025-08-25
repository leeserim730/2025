import streamlit as st    #st라는 별칭 붙여서 st.~의 형태로 쉽게 사용


#웹앱 탭에 표시될 제목과 아이콘 설정 / config : configuration (구성,설정)의 줄임말, 
st.set_page_config(page_title="주제씨앗", page_icon="🎓", layout="centered")

#set_page_config : 앱의 초기 화면 설정 (config)을 바꾸는 함수 -> 원래 기본값으로 설정되기 때문
#page_title = ~  : 제목
#page_icon = ~   : 아이콘, 이모지 가능
#layout = "centered" : 화면 배치 (중앙 정)


st.title("🎓 주제씨앗")  #앱 상단에 제목을 출력


# 사용자 유형 선택
user_type = st.radio("👥 사용자 유형을 선택하세요", ["👩‍🏫 교사", "👩‍🎓 학생"])

#st.radio() : 여러 옵션 중 하나만 선택할 수 있는 버튼
#(버튼의 질문 요구, 선택지목록)
#선택한 값이 user_type 변수에 저장됨


#사용자가 교사 선택
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
