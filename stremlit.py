import streamlit as st
from passploit import Passploit

passploit = Passploit()
# Styl strony
st.set_page_config(page_title="Generator Możliwych Haseł", layout="centered")



# Tytuł aplikacji
st.title("Generator Możliwych Haseł")

# Opis aplikacji
st.write("Aplikacja umożliwia generowanie możliwych haseł na podstawie wprowadzonych informacji.")

# Pole do wprowadzania danych przez użytkownika
user_input = st.text_input(
    label="Wprowadź Informacje O Sobie",
    placeholder="Przykład: Jan, Kowalski, 2000, kot, niebieski"
)

# Przycisk do generowania wyników
if st.button("Generuj Hasła"):
    if user_input:
        st.subheader("Informacje Użytkownika")
        st.write(user_input)
        
        user_info = [info.strip() for info in user_input.split(",")]
        passwords = passploit.find_similar_passwords(user_info, 500)
        st.subheader("Możliwe Hasła")
        for i in passwords:
            st.write(i)
    else:
        st.error("Proszę wprowadzić informacje.")

