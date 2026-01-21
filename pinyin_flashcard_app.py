# ==============================
# PHẦN 1: HỌC BẢNG CHỮ CÁI PINYIN
# (AUDIO FIX – STABLE VERSION)
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
    "ā": "Thanh 1",
    "á": "Thanh 2",
    "ǎ": "Thanh 3",
    "à": "Thanh 4"
}

# -------- HANZI AUDIO MAP (KEY FIX) --------
audio_map = {
    "b": "巴", "p": "趴", "m": "媽", "f": "發",
    "d": "搭", "t": "他", "n": "拿", "l": "拉",
    "g": "高", "k": "咖", "h": "哈",
    "j": "雞", "q": "七", "x": "西",
    "zh": "渣", "ch": "叉", "sh": "沙", "r": "日",
    "z": "資", "c": "擦", "s": "思",

    "a": "啊", "o": "喔", "e": "鵝", "i": "衣", "u": "烏", "ü": "魚",
    "ai": "愛", "ei": "欸", "ao": "熬", "ou": "歐",
    "an": "安", "en": "恩", "ang": "昂", "eng": "嗯",
    "ong": "翁", "er": "兒",

    "ā": "媽", "á": "麻", "ǎ": "馬", "à": "罵"
}

# -------- AUDIO FUNCTION --------
def play_audio(sound):
    text = audio_map.get(sound, sound)
    tts = gTTS(text=text, lang="zh-CN")  # zh-CN ổn định hơn
    audio_bytes = io.BytesIO()
    tts.write_to_fp(audio_bytes)
    st.audio(audio_bytes.getvalue(), format="audio/mp3")

# -------- UI --------
st.title("🔤 Phần 1: Học bảng chữ cái Pinyin")
st.caption("Audio ổn định – học phát âm nền tảng 🇹🇼")

tab1, tab2, tab3 = st.tabs(
    ["🅰️ Thanh mẫu", "🅱️ Vận mẫu", "🎵 Thanh điệu"]
)

# -------- INITIALS --------
with tab1:
    st.subheader("Thanh mẫu (Initials)")
    cols = st.columns(6)
    for i, sound in enumerate(initials):
        with cols[i % 6]:
            if st.button(sound, key=f"i_{sound}"):
                play_audio(sound)

# -------- FINALS --------
with tab2:
    st.subheader("Vận mẫu (Finals)")
    cols = st.columns(6)
    for i, sound in enumerate(finals):
        with cols[i % 6]:
            if st.button(sound, key=f"f_{sound}"):
                play_audio(sound)

# -------- TONES --------
with tab3:
    st.subheader("Thanh điệu (Tones)")
    for tone, desc in tones.items():
        col1, col2 = st.columns([1, 4])
        with col1:
            if st.button(tone, key=f"t_{tone}"):
                play_audio(tone)
        with col2:
            st.write(desc)
