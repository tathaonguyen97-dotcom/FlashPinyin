import streamlit as st
import random
from gtts import gTTS
import io

# ----------------------
# DATA: Taiwan Mandarin Flashcards
# ----------------------
flashcards = [
    {
        "hanzi": "你好",
        "zhuyin": "ㄋㄧˇ ㄏㄠˇ",
        "pinyin": "nǐ hǎo",
        "meaning": "Xin chào"
    },
    {
        "hanzi": "謝謝",
        "zhuyin": "ㄒㄧㄝˋ ㄒㄧㄝ˙",
        "pinyin": "xiè xie",
        "meaning": "Cảm ơn"
    },
    {
        "hanzi": "再見",
        "zhuyin": "ㄗㄞˋ ㄐㄧㄢˋ",
        "pinyin": "zài jiàn",
        "meaning": "Tạm biệt"
    },
    {
        "hanzi": "是",
        "zhuyin": "ㄕˋ",
        "pinyin": "shì",
        "meaning": "Là / Phải"
    },
    {
        "hanzi": "不是",
        "zhuyin": "ㄅㄨˊ ㄕˋ",
        "pinyin": "bú shì",
        "meaning": "Không phải"
    }
]

# ----------------------
# FUNCTIONS
# ----------------------
def play_audio(text):
    tts = gTTS(text=text, lang="zh-TW")
    audio_bytes = io.BytesIO()
    tts.write_to_fp(audio_bytes)
    st.audio(audio_bytes.getvalue(), format="audio/mp3")

def next_card():
    st.session_state.card = random.choice(flashcards)
    st.session_state.show_answer = False

# ----------------------
# SESSION STATE
# ----------------------
if "card" not in st.session_state:
    st.session_state.card = random.choice(flashcards)
    st.session_state.show_answer = False

# ----------------------
# UI
# ----------------------
st.set_page_config(
    page_title="Taiwan Mandarin Flashcards",
    page_icon="🇹🇼",
    layout="centered"
)

st.title("🇹🇼 Taiwan Mandarin Flashcards")
st.caption("Phồn thể • Zhuyin • Giọng Đài Loan")

card = st.session_state.card

# Flashcard display
st.markdown(
    f"""
    <div style="
        border: 3px solid #e5e7eb;
        border-radius: 20px;
        padding: 35px;
        text-align: center;
        font-size: 42px;
        background-color: #ffffff;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.05);
        ">
        {card['hanzi']}
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("👀 看答案"):
        st.session_state.show_answer = True

with col2:
    if st.button("🔊 聽發音"):
        play_audio(card["hanzi"])

with col3:
    if st.button("➡️ 下一個"):
        next_card()

# ----------------------
# ANSWER
# ----------------------
if st.session_state.show_answer:
    st.markdown("### 📖 單字資訊")
    st.write(f"**注音 (Zhuyin):** {card['zhuyin']}")
    st.write(f"**Pinyin:** {card['pinyin']}")
    st.write(f"**Nghĩa:** {card['meaning']}")
