from datetime import datetime

# -----------------------------
# Sun Sign Calculation
# -----------------------------
def get_sun_sign(birth_date):
    # (month, day, sign)
    zodiac_dates = [
        ((1, 20), "Capricorn"), ((2, 19), "Aquarius"), ((3, 20), "Pisces"),
        ((4, 20), "Aries"), ((5, 21), "Taurus"), ((6, 21), "Gemini"),
        ((7, 22), "Cancer"), ((8, 22), "Leo"), ((9, 22), "Virgo"),
        ((10, 23), "Libra"), ((11, 22), "Scorpio"), ((12, 21), "Sagittarius"),
        ((12, 31), "Capricorn")  # Capricorn continues after Dec 22
    ]

    for (month, day), sign in zodiac_dates:
        if (birth_date.month, birth_date.day) <= (month, day):
            return sign
    return "Capricorn"


# -----------------------------
# Traits Dictionary
# -----------------------------
TRAITS = {
    "Aries": "Energetic, confident, bold, passionate.",
    "Taurus": "Reliable, practical, loves comfort, loyal.",
    "Gemini": "Curious, adaptable, witty, sociable.",
    "Cancer": "Emotional, nurturing, intuitive, caring.",
    "Leo": "Charismatic, ambitious, generous, proud.",
    "Virgo": "Analytical, detail-oriented, helpful, modest.",
    "Libra": "Balanced, fair, diplomatic, social.",
    "Scorpio": "Mysterious, intense, determined, loyal.",
    "Sagittarius": "Adventurous, optimistic, philosophical.",
    "Capricorn": "Ambitious, disciplined, practical, wise.",
    "Aquarius": "Innovative, independent, humanitarian.",
    "Pisces": "Compassionate, artistic, intuitive, dreamy."
}

ELEMENTS = {
    "Aries": "Fire", "Leo": "Fire", "Sagittarius": "Fire",
    "Taurus": "Earth", "Virgo": "Earth", "Capricorn": "Earth",
    "Gemini": "Air", "Libra": "Air", "Aquarius": "Air",
    "Cancer": "Water", "Scorpio": "Water", "Pisces": "Water"
}


# -----------------------------
# Chinese Zodiac
# -----------------------------
def get_chinese_zodiac(year):
    animals = [
        "Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake",
        "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig"
    ]
    return animals[(year - 1900) % 12]


# -----------------------------
# Moon Phase (very simplified)
# -----------------------------
def get_moon_phase(date):
    diff = date - datetime(2001, 1, 1)
    days = diff.days % 29.53
    if days < 7.4:
        return "New Moon"
    elif days < 14.8:
        return "First Quarter"
    elif days < 22.1:
        return "Full Moon"
    else:
        return "Last Quarter"


# -----------------------------
# Lucky Number (simple rule)
# -----------------------------
def get_lucky_number(date):
    return (date.day + date.month + date.year) % 9 + 1


# -----------------------------
# Question Answer (basic)
# -----------------------------
def answer_question(question, sun_sign):
    if not question:
        return ""
    q = question.lower()
    if "love" in q:
        return f"As a {sun_sign}, love will feel natural when you express your true self."
    elif "career" in q:
        return f"Your {sun_sign} determination will bring career success soon."
    elif "money" in q or "finance" in q:
        return f"Finances may fluctuate, but your {sun_sign} discipline will guide you."
    else:
        return f"The stars suggest reflection, {sun_sign} energy will guide your path."


# -----------------------------
# Main Generator
# -----------------------------
def generate_reading(name, birth_datetime, place, question=""):
    sun_sign = get_sun_sign(birth_datetime)
    traits = TRAITS.get(sun_sign, "Unique and special qualities.")
    element = ELEMENTS.get(sun_sign, "Spirit")
    chinese_zodiac = get_chinese_zodiac(birth_datetime.year)
    moon_phase = get_moon_phase(birth_datetime)
    lucky_number = get_lucky_number(birth_datetime)

    summary = (
        f"You are a {sun_sign}, ruled by {element}. "
        f"People see you as {traits} "
        f"Born under the {moon_phase} moon, you carry cycles of renewal. "
        f"In Chinese astrology, you are a {chinese_zodiac}, "
        f"which adds unique depth to your personality. "
        f"Your lucky number is {lucky_number}."
    )

    q_answer = answer_question(question, sun_sign)

    return {
        "name": name,
        "place": place,
        "sun_sign": sun_sign,
        "traits": traits,
        "element": element,
        "chinese_zodiac": chinese_zodiac,
        "moon_phase": moon_phase,
        "lucky_number": lucky_number,
        "summary": summary,
        "question_answer": q_answer
    }
