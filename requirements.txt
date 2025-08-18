import streamlit as st

# 페이지 설정
st.set_page_config(page_title="탄생석 알아보기", layout="centered")

# CSS 커스터마이징 (세련된 흑백 스타일)
st.markdown("""
    <style>
    body {
        background-color: black;
        color: white;
        font-family: 'Helvetica Neue', sans-serif;
    }
    .stone-card {
        background-color: #1a1a1a;
        padding: 20px;
        border-radius: 16px;
        margin: 20px 0;
        text-align: center;
        box-shadow: 0px 4px 12px rgba(255, 255, 255, 0.1);
    }
    </style>
""", unsafe_allow_html=True)

# 리키 흑백 이미지 (Hero)
st.image("https://i.imgur.com/dkN0r8b.jpeg", use_column_width=True)  # 리키 이미지 URL 예시

# 제목
st.title("💎 제로베이스원 리키와 함께하는 탄생석 찾기 ⚫⚪🍓🥤🐰💫")

st.write("세련된 흑백 감성으로, 당신의 탄생석과 의미를 알아보세요.")

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

# 사용자 입력
month = st.selectbox("출생 월을 선택하세요 🍓🐰", range(1, 13), format_func=lambda x: f"{x}월")

# 결과 출력
if month:
    stone = birthstones[month]
    st.markdown(f"""
    <div class="stone-card">
        <h2>✨ {month}월의 탄생석: {stone['name']} ✨</h2>
        <img src="{stone['image']}" width="300">
        <p><b>의미:</b> {stone['meaning']}</p>
        <p>⚫⚪ 딸기라떼도 한 잔 곁들이면서 🍓🥤, 리니니와 함께 🐰💫</p>
    </div>
    """, unsafe_allow_html=True)

