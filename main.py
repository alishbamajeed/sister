import streamlit as st

st.set_page_config(page_title="Pyari Behn ke Naam", page_icon="💌", layout="centered")

# Inject CSS for styling
st.markdown(
    """
    <style>
        .title {
            font-family: 'Comic Sans MS', cursive;
            color: #FF69B4;
            font-size: 40px;
            text-align: center;
        }
        .heart {
            font-size: 30px;
            text-align: center;
            color: red;
        }
        .msg {
            background-color: #fff0f5;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0 0 20px #ffb6c1;
            font-size: 20px;
            font-family: 'Verdana';
        }
        audio {
            display: block;
            margin: 0 auto;
            padding-top: 20px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and Hearts
st.markdown('<div class="title">💌 Pyari Behn ke Naam 💌</div>', unsafe_allow_html=True)
st.markdown('<div class="heart">❤❤❤❤❤❤❤❤❤❤❤❤</div>', unsafe_allow_html=True)

# Main Message
st.markdown(
    """
    <div class="msg">
        Assalam-o-Alaikum meri pyari behn 🌸<br><br>

        Main jaanti hoon hum dono ke darmiyan thodi si doori aa gayi hai...<br>
        Lekin main chahti hoon ke hum dobara waise hi ban jayein,<br>
        Jese hum bachpan mein ek dosray ka haath nahi chhodte the 🥺🤝<br><br>

        Main tumse naraz nahi hoon, bas udaas hoon...<br>
        Kyun ke meri apni behn, meri dosti, mujhse naraz hai 😔<br><br>

        Agar tumne Shahmeer bhai ke liye kuch galat keh diya ho toh,<br>
        Chhoti si sorry keh dena 🌷 isse tum aur bhi badi lagogi<br><br>

        Main tumse mohabbat karti hoon behna ❤️<br>
        Aur chahti hoon humara rishta hamesha mazboot rahe 🫂<br><br>

        Tum meri Jaan ho, meri izzat ho, meri khushi ho.<br>
        Chalo sulah karte hain... kyun ke zindagi choti hai 💕<br><br>

        <b>🌟 Tumhari Baji - Alishba 🌟</b>
    </div>
    """,
    unsafe_allow_html=True
)

# Song (replace with any public direct MP3 link you like)
st.markdown("### 🎶 Play This Song While Reading:")

st.audio("https://mr-jat.in/ek-hazaaron-mein-meri-behna-hai")

st.markdown('<div class="heart">❤❤❤❤❤❤❤❤❤❤❤❤</div>', unsafe_allow_html=True)
