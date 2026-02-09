import streamlit as st

st.title("Тест по математика")
st.write("Отговори на въпросите и натисни **Изпрати**")

q1 = st.number_input("1️⃣ Колко е 5 × 5 ?")
q2 = st.number_input("2️⃣ Колко е 10 + 2 ?")
q3 = st.number_input("3️⃣ Колко е 8 − 3 ?")
q4 = st.number_input("4️⃣ Колко е 4 × 2 ?")
q5 = st.number_input("5️⃣ Колко е 20 ÷ 4 ?")

if st.button("Изпрати"):
    score = 0

    if q1 == 25:
        score += 1
    if q2 == 12:
        score += 1
    if q3 == 5:
        score += 1
    if q4 == 8:
        score += 1
    if q5 == 5:
        score += 1

    st.write("###Резултат:")
    st.write(f"Верни отговори: **{score} / 5**")

    if score == 5:
        st.success("Отлично! Всичко е вярно!")
    elif score >= 3:
        st.warning("Добре, но можеш и по-добре!")
    else:
        st.error("Опитай отново!")

