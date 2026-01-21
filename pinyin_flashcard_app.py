# ==============================
# PHẦN 1: HỌC BẢNG CHỮ CÁI PINYIN
# ==============================

import streamlit as st
from gtts import gTTS
import io

# -------- DATA --------
initials = [
    "b", "p", "m", "f",
    "d", "t", "n", "l",
    "g", "k", "h",
    "j", "q", "x",
    "zh", "ch", "sh", "r",
    "z", "c", "s"
]

finals = [
    "a", "o", "e", "i", "u", "ü",
    "ai", "ei", "ao", "ou",
    "an", "en", "ang", "eng",
    "ong", "er"
]

tones = {
    "ā": "Thanh 1 (cao – ngang)",
    "á": "Thanh 2 (lên)",
    "ǎ": "Thanh 3 (xuống rồi lên)",
    "à": "Thanh 4 (xuống mạnh)"
}

# -------- AUDIO FUNCTION --------
def play_audio(text):
    tts = gTTS(text=text, lang="zh-TW")
    audio_bytes = io.BytesIO()
    tts.write_to_fp(audio_bytes)
    st.audio(audio_bytes.getvalue(), format="audio/mp3")

# -------- UI --------
st.title("🔤 Phần 1: Học bảng chữ cái Pinyin")
st.caption("Nền tảng phát âm – học theo phong cách Đài Loan 🇹🇼")

tab1, tab2, tab3 = st.tabs(
    ["🅰️ Thanh mẫu (Initials)", "🅱️ Vận mẫu (Finals)", "🎵 Thanh điệu (Tones)"]
)

# -------- INITIALS --------
with tab1:
    st.subheader("Thanh mẫu (聲母)")
    st.write("👉 Nhấn vào từng âm để nghe phát âm")

    cols = st.columns(6)
    for i, sound in enumerate(initials):
        with cols[i % 6]:
            if st.button(sound, key=f"init_{sound}"):
                play_audio(sound)

# -------- FINALS --------
with tab2:
    st.subheader("Vận mẫu (韻母)")
    st.write("👉 Luyện phát âm phần nguyên âm")

    cols = st.columns(6)
    for i, sound in enumerate(finals):
        with cols[i % 6]:
            if st.button(sound, key=f"fin_{sound}"):
                play_audio(sound)

# -------- TONES --------
with tab3:
    st.subheader("Thanh điệu (聲調)")
    st.write("👉 Nghe và cảm nhận cao độ")

    for tone, desc in tones.items():
        col1, col2 = st.columns([1, 4])
        with col1:
            if st.button(tone, key=f"tone_{tone}"):
                play_audio(tone)
        with col2:
            st.write(desc)
