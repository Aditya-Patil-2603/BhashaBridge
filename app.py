import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="BhashaBridge",
    page_icon="🇮🇳",
    layout="centered"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
    .main-title {
        text-align: center;
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        color: #666;
        font-size: 18px;
        margin-bottom: 30px;
    }

    .feature-card {
        padding: 18px;
        border-radius: 12px;
        border: 1px solid #ddd;
        margin-bottom: 10px;
    }

    .section-title {
        font-size: 24px;
        font-weight: 600;
        margin-top: 25px;
    }
</style>
""", unsafe_allow_html=True)


# ---------------- HEADER ----------------
st.markdown(
    '<div class="main-title">🇮🇳 BhashaBridge</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">AI Government Services Assistant</div>',
    unsafe_allow_html=True
)

st.write(
    "Government services ko samajhna ab simple hai. "
    "Marathi, Hindi aur English mein information paaiye."
)


# ---------------- LANGUAGE ----------------
st.markdown(
    '<div class="section-title">🌐 Choose your language</div>',
    unsafe_allow_html=True
)

language = st.selectbox(
    "Language",
    ["English", "हिंदी", "मराठी"],
    label_visibility="collapsed"
)


# ---------------- QUESTION ----------------
st.markdown(
    '<div class="section-title">💬 Ask BhashaBridge</div>',
    unsafe_allow_html=True
)

question = st.text_area(
    "Your question",
    placeholder="Example: Driving licence renew karne ke liye kya documents chahiye?",
    height=120,
    label_visibility="collapsed"
)


# ---------------- BUTTONS ----------------
col1, col2 = st.columns(2)

with col1:
    ask = st.button(
        "🔎 Ask BhashaBridge",
        use_container_width=True
    )

with col2:
    voice = st.button(
        "🎤 Voice Input",
        use_container_width=True
    )


# ---------------- RESPONSE ----------------
if ask:

    if question.strip():

        st.markdown(
            '<div class="section-title">🤖 BhashaBridge Response</div>',
            unsafe_allow_html=True
        )

        st.info(
            "Your question has been received. "
            "AI response system will be connected in the next stage."
        )

        st.success(f"Language selected: {language}")

    else:
        st.warning("Please enter your question first.")


# ---------------- FEATURES ----------------
st.markdown(
    '<div class="section-title">✨ What BhashaBridge can help with</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:
    st.markdown(
        '<div class="feature-card">📄 Eligibility & Documents</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="feature-card">💰 Fees & Charges</div>',
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        '<div class="feature-card">📝 Application Process</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="feature-card">🔗 Verified Information</div>',
        unsafe_allow_html=True
    )


# ---------------- FOOTER ----------------
st.divider()

st.caption(
    "BhashaBridge • Making Government Services Easier for Everyone 🇮🇳"
)