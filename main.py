import streamlit as st
import datetime

# 월별 탄생석 데이터 (예시)
birthstones = {
    1: ("가넷 (Garnet)", "진실, 우정"),
    2: ("자수정 (Amethyst)", "평화, 성실"),
    3: ("아쿠아마린 (Aquamarine)", "용기, 지혜"),
    4: ("다이아몬드 (Diamond)", "순결, 영원한 사랑"),
    5: ("에메랄드 (Emerald)", "행운, 희망"),
    6: ("진주 / 알렉산드라이트", "건강, 부귀"),
    7: ("루비 (Ruby)", "사랑, 열정"),
    8: ("감람석 (Peridot)", "화합, 행복"),
    9: ("사파이어 (Sapphire)", "지혜, 진실"),
    10: ("오팔 / 토르말린", "희망, 순결"),
    11: ("토파즈 (Topaz)", "우정, 인내"),
    12: ("터키석 / 탄자나이트 / 청옥", "성공, 번영")
}

# 앱 제목
st.title("🎂 생일로 알아보는 탄생석 💎")

# 사용자 생일 입력
birthday = st.date_input("생일을 선택하세요", value=datetime.date(2000,1,1))

# 월 추출
month = birthday.month

# 탄생석 정보 가져오기
stone, meaning = birthstones[month]

# 결과 출력
st.subheader(f"{month}월의 탄생석은?")
st.success(f"💎 {stone}\n\n의미: {meaning}")

# 추가 학습 정보
st.markdown("---")
st.info("탄생석은 고대부터 행운과 보호의 의미로 사용되었습니다. "
        "각 달마다 상징하는 보석이 있으며, 교육적인 목적으로 배우는 데 도움이 됩니다.")
