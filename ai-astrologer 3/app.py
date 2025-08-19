import streamlit as st
from datetime import datetime, time, date
from astrology_engine import generate_reading

st.set_page_config(page_title="AI Astrologer", page_icon="🔮", layout="centered")

st.title("🔮 AI Astrologer")
st.caption("For entertainment & reflection purposes only.")

with st.form("birth_form"):
    cols = st.columns(2)
    name = cols[0].text_input("Name", placeholder="Ada Lovelace")
    place = cols[1].text_input("Birth Place (City, Country)", placeholder="Jaipur, India")

    c1, c2 = st.columns(2)

    # ✅ Primary Date Picker (1800 - today)
    birth_date = c1.date_input(
        "Birth Date (use calendar if working)",
        value=date(1990, 1, 1),
        min_value=date(1800, 1, 1),
        max_value=date.today()
    )

    # ✅ Manual DOB fallback
    manual_dob = c1.text_input(
        "Or enter DOB manually (YYYY-MM-DD)",
        placeholder="1985-06-15"
    )
    if manual_dob:
        try:
            birth_date = datetime.strptime(manual_dob, "%Y-%m-%d").date()
        except ValueError:
            st.warning("⚠️ Invalid date format. Please use YYYY-MM-DD.")

    birth_time = c2.time_input("Birth Time", value=time(12, 0))

    st.markdown("**Ask a question (optional):**")
    question = st.text_area("Free-text question", placeholder="e.g., What's next for my career?")

    submitted = st.form_submit_button("Get My Reading ✨")

if submitted:
    # Combine date and time into datetime
    dt = datetime.combine(birth_date, birth_time)
    reading = generate_reading(name or "Friend", dt, place or "Unknown", question or "")

    with st.container():
        st.subheader(f"Your Reading, {reading['name']}")
        st.write(reading["summary"])
        st.divider()

        c1, c2, c3 = st.columns(3)
        c1.metric("Sun Sign", reading["sun_sign"])
        c2.metric("Moon Phase", reading["moon_phase"])
        c3.metric("Lucky Number", reading["lucky_number"])
        c1.metric("Element", reading["element"])
        c2.metric("Chinese Zodiac", reading["chinese_zodiac"])
        c3.metric("Birth Place", reading["place"])

        if reading["question_answer"]:
            st.markdown("### Your Question")
            st.info(reading["question_answer"])

        # Download reading
        st.markdown("### Save Your Reading")
        text = (
            f"AI Astrologer Reading for {reading['name']}\n"
            f"Birth: {birth_date} {birth_time} at {reading['place']}\n"
            f"Sun Sign: {reading['sun_sign']} ({reading['element']})\n"
            f"Traits: {reading['traits']}\n"
            f"Moon Phase: {reading['moon_phase']}\n"
            f"Chinese Zodiac: {reading['chinese_zodiac']}\n"
            f"Lucky Number: {reading['lucky_number']}\n\n"
            f"Summary:\n{reading['summary']}\n\n"
            + (f"Your Question:\n{question}\n\nAnswer:\n{reading['question_answer']}\n" if question else "")
        )
        st.download_button("Download as .txt", data=text, file_name="reading.txt")

else:
    st.info("Fill your details and click **Get My Reading ✨** to generate a personalized reading.")

st.markdown("---")
st.caption("Built with Streamlit. No external APIs required.")
