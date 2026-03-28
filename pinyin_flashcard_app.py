import streamlit as st
import random
from gtts import gTTS
import os

st.set_page_config(page_title="Chinese Flashcards Pro", page_icon="📚")

st.title("📚 Flashcard Học Từ Vựng (Pro Version)")

# ================= DATA =================
vocab = [
    ("現在", "xiànzài", "Bây giờ"),("點鐘", "diǎnzhōng", "Giờ"),("分鐘", "fēnzhōng", "Phút"),("早上", "zǎoshàng", "Buổi sáng"),("中午", "zhōngwǔ", "Buổi trưa"),("下午", "xiàwǔ", "Buổi chiều"),("晚上", "wǎnshàng", "Buổi tối"),("今天", "jīntiān", "Hôm nay"),("明天", "míngtiān", "Ngày mai"),("昨天", "zuótiān", "Hôm qua"),("後天", "hòutiān", "Ngày mốt"),("禮拜", "lǐbài", "Tuần"),("週末", "zhōumò", "Cuối tuần"),("一下子", "yíxiàzi", "Một lát"),("最近", "zuìjìn", "Dạo này"),("以後", "yǐhòu", "Sau này"),("以前", "yǐqián", "Trước đây"),("平常", "píngcháng", "Thường thường"),("準時", "zhǔnshí", "Đúng giờ"),("整天", "zhěngtiān", "Cả ngày"),
    ("捷運站", "jiéyùn zhàn", "Trạm MRT"),("便利商店", "biànlì shāngdiàn", "Cửa hàng tiện lợi"),("夜市", "yèshì", "Chợ đêm"),("超市", "chāoshì", "Siêu thị"),("百貨公司", "bǎihuò gōngsī", "TTTM"),("早餐店", "zǎocān diàn", "Tiệm ăn sáng"),("飲料店", "yǐnliào diàn", "Tiệm nước"),("銀行", "yínháng", "Ngân hàng"),("郵局", "yóujú", "Bưu điện"),("醫院", "yīyuàn", "Bệnh viện"),("藥局", "yàojú", "Hiệu thuốc"),("公司", "gōngsī", "Công ty"),("辦公室", "bàngōngshì", "Văn phòng"),("學校", "xuéxiào", "Trường học"),("圖書館", "túshūguǎn", "Thư viện"),("公園", "gōngyuán", "Công viên"),("洗手間", "xǐshǒujiān", "Nhà vệ sinh"),("停車場", "tíngchē chǎng", "Bãi xe"),("加油站", "jiāyóu zhàn", "Trạm xăng"),("宿舍", "sùshè", "Ký túc xá"),
    ("起床", "qǐchuáng", "Thức dậy"),("刷牙", "shuāyá", "Đánh răng"),("洗澡", "xǐzǎo", "Tắm"),("出門", "chūmén", "Ra ngoài"),("搭車", "dāchē", "Đi xe"),("走路", "zǒulù", "Đi bộ"),("上班", "shàngbān", "Đi làm"),("下班", "xiàbān", "Tan làm"),("上課", "shàngkè", "Đi học"),("下課", "xiàkè", "Tan học"),("吃飯", "chīfàn", "Ăn cơm"),("喝水", "hēshuǐ", "Uống nước"),("結帳", "jiézhàng", "Thanh toán"),("外帶", "wàidài", "Mang về"),("內用", "nèiyòng", "Ăn tại chỗ"),("休息", "xiūxí", "Nghỉ ngơi"),("運動", "yùndòng", "Tập thể dục"),("聊天", "liáotiān", "Tám chuyện"),("用手機", "yòng shǒujī", "Dùng điện thoại"),("睡覺", "shuìjiào", "Đi ngủ")
]

# ================= STATE =================
if "card" not in st.session_state:
    st.session_state.card = random.choice(vocab)

if "show" not in st.session_state:
    st.session_state.show = False

if "score" not in st.session_state:
    st.session_state.score = 0

if "total" not in st.session_state:
    st.session_state.total = 0

mode = st.radio("Chọn chế độ:", ["Flashcard", "Quiz"])

# ================= AUDIO =================
def play_audio(text):
    tts = gTTS(text=text, lang='zh-tw')
    file = "audio.mp3"
    tts.save(file)
    audio_file = open(file, 'rb')
    st.audio(audio_file.read(), format='audio/mp3')

# ================= FLASHCARD MODE =================
if mode == "Flashcard":
    chinese, pinyin, meaning = st.session_state.card

    st.markdown(f"## 🀄 {chinese}")

    if st.button("🔊 Phát âm"):
        play_audio(chinese)

    if st.session_state.show:
        st.markdown(f"### {pinyin}")
        st.markdown(f"### {meaning}")
    else:
        st.write("🤔 Đoán nghĩa đi!")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("👀 Xem đáp án"):
            st.session_state.show = True

    with col2:
        if st.button("🔄 Từ mới"):
            st.session_state.card = random.choice(vocab)
            st.session_state.show = False

# ================= QUIZ MODE =================
else:
    question = random.choice(vocab)
    correct = question[2]

    options = [correct]
    while len(options) < 4:
        choice = random.choice(vocab)[2]
        if choice not in options:
            options.append(choice)

    random.shuffle(options)

    st.markdown(f"## 🀄 {question[0]}")

    answer = st.radio("Chọn nghĩa đúng:", options)

    if st.button("✅ Kiểm tra"):
        st.session_state.total += 1
        if answer == correct:
            st.success("Đúng rồi!")
            st.session_state.score += 1
        else:
            st.error(f"Sai! Đáp án: {correct}")

# ================= PROGRESS =================
st.markdown("---")
st.markdown(f"📊 Điểm: {st.session_state.score}/{st.session_state.total}")

if st.session_state.total > 0:
    accuracy = st.session_state.score / st.session_state.total * 100
    st.progress(accuracy/100)
    st.write(f"Độ chính xác: {accuracy:.1f}%")
