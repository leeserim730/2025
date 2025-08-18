import streamlit as st
from datetime import datetime

# 탄생석 데이터
birthstones = {
    1: {"name": "가넷 (Garnet)", "meaning": "진실, 우정, 충성", "image": "https://upload.wikimedia.org/wikipedia/commons/6/6d/Almandine_Garnet.jpg"},
    2: {"name": "자수정 (Amethyst)", "meaning": "평화, 성실, 진실된 사랑", "image": "https://upload.wikimedia.org/wikipedia/commons/6/6b/Amethyst._Magaliesburg%2C_South_Africa.jpg"},
    3: {"name": "아쿠아마린 (Aquamarine)", "meaning": "용기, 희망, 행복", "image": "https://upload.wikimedia.org/wikipedia/commons/5/5f/Aquamarine-Schorl-188364.jpg"},
    4: {"name": "다이아몬드 (Diamond)", "meaning": "순결, 영원한 사랑", "image": "https://upload.wikimedia.org/wikipedia/commons/7/70/Diamond_polished.png"},
    5: {"name": "에메랄드 (Emerald)", "meaning": "행운, 건강, 지혜", "image": "https://upload.wikimedia.org/wikipedia/commons/f/f8/Emerald_-_Colombia.jpg"},
    6: {"name": "진주 (Pearl)", "meaning": "순수, 장수, 부귀", "image": "https://upload.wikimedia.org/wikipedia/commons/d/d5/Pearl_on_white_background.jpg"},
    7: {"name": "루비 (Ruby)", "meaning": "사랑, 용기, 열정", "image": "https://upload.wikimedia.org/wikipedia/commons/e/e3/Ruby_crystal.jpg"},
    8: {"name": "감람석 (Peridot)", "meaning": "우정, 행복, 화합", "image": "https://upload.wikimedia.org/wikipedia/commons/6/61/Peridot_-_Olivine.jpg"},
    9: {"name": "사파이어 (Sapphire)", "meaning": "지혜, 성실, 고결", "image": "https://upload.wikimedia.org/wikipedia/commons/8/82/Sapphire_-_Sri_Lanka.jpg"},
    10: {"name": "오팔 (Opal)", "meaning": "희망, 순결, 창의성", "image": "https://upload.wikimedia.org/wikipedia/commons/9/96/Opal-PeterGraham.jpg"},
    11: {"name": "토파즈 (Topaz)", "meaning": "우정, 희망, 건강", "image": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Topaz-Brazil.jpg"},
    12: {"name": "터키석 (Turquoise)", "meaning": "성공, 승리, 행복", "image": "https://upload.wikimedia.org/wikipedia/commons/0/0c/Turquoise-Persia.jpg"},
}

# 페이지 설정
st.set_page_config(page_title="탄생석 알아보기", layout="centered")

# 제목
st.title("💎 나의 탄생석을 알아보자!")
st.write("생일이나 월을 입력하면, 당신의 탄생석과 의미를 알려드립니다.")

# 입력 (달 선택)
month = st.selectbox("당신의 출생 월을 선택하세요", range(1, 13), format_func=lambda x: f"{x}월")

# 결과 출력
if month:
    stone = birthstones[month]
    st.subheader(f"✨ {month}월의 탄생석은 **{stone['name']}** 입니다 ✨")
    st.image(stone["image"], caption=stone["name"], use_column_width=True)
    st.markdown(f"**의미:** {stone['meaning']}")
