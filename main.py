import streamlit as st
import datetime

# 월별 탄생석 데이터
birthstones = {
    1: ("garnet 💗", "진실, 우정 ✨"),
    2: ("amethyst 💜", "평화, 성실 🕊️"),
    3: ("aquamarine 💙", "용기, 지혜 🌊"),
    4: ("diamond 💎", "순결, 영원한 사랑 💍"),
    5: ("emerald 💚", "행운, 희망 🍀"),
    6: ("pearl 🤍 / alexandrite 🌈", "건강, 부귀 🏆"),
    7: ("ruby ❤️", "사랑, 열정 🔥"),
    8: ("peridot 💚", "화합, 행복 🌿"),
    9: ("sapphire 💙", "지혜, 진실 📘"),
    10: ("opal 🌸 / tourmaline 🌈", "희망, 순결 🦄"),
    11: ("topaz 🧡", "우정, 인내 🌞"),
    12: ("turquoise 🩵 / tanzanite 🔮 / lapis lazuli 💙", "성공, 번영 🌟")
}

st.title("🌸🎂 나의 생일로 알아보는 탄생석 💎✨")

birthday = st.date_input("👉 생일을 골라주세요!", value=datetime.date(2000,1,1))
month = birthday.month
stone, meaning = birthstones[month]

st.markdown("---")
st.markdown(
    f"""
    ## 🎀 {month}월의 탄생석은...  
    ### ✨ {stone} ✨  
    #### 💡 의미: {meaning}
    """
)

st.markdown("---")
st.info("💖 탄생석은 고대부터 행운과 보호의 의미로 여겨졌어요. "
        "귀여운 보석 친구들과 함께 나만의 행운을 찾아보세요! ✨🎀")

st.markdown("💕 만든이: 탄생석 요정 🧚‍♀️")
