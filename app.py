import streamlit as st

st.title("Тест по география")
st.write("Отговори на въпросите и натисни **Изпрати**")

q1 = st.text_input("1️⃣ Коя е столицата на България?")
q2 = st.text_input("2️⃣ На кой континент се намира България?")
q3 = st.text_input("3️⃣ Кое е най-голямото море до България?")
q4 = st.text_input("4️⃣ Коя планина е в България?")
q5 = st.text_input("5️⃣ Коя река минава през Русе?")

if st.button("Изпрати"):
    score = 0

    if q1.strip().lower() == "софия":
        score += 1
    if q2.strip().lower() == "европа":
        score += 1
    if q3.strip().lower() == "черно море":
        score += 1
    if q4.strip().lower() == "рила":
        score += 1
    if q5.strip().lower() == "дунав":
        score += 1

    st.write("### Резултат:")
    st.write(f"Верни отговори: **{score} / 5**")

    if score == 5:
        st.success("Отлично! Географията ти е супер!")
    elif score >= 3:
        st.warning("Добре, но може още малко!")
    else:
        st.error("Опитай отново!")
