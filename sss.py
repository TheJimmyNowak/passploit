import streamlit as st

# from passpilot import db.py // tu ma być połączenie z generatorem do haseł, nie wiem, który to plik

# Styl strony
st.set_page_config(page_title="Generator Możliwych Haseł", layout="centered")

# CSS dla stylizacji
st.markdown(
    """
    <style>
        body {
            font-family: Helvetica, sans-serif;
            background-color: white;
            color: black;
        }
        .stTitle {
            font-size: 18px;
            color: red;
        }
        .stMarkdown {
            font-size: 14px;
        }
        .stTextInput, .stButton, .stBox {
            background-color: #f2f2f2;
            border: 1px solid black;
        }
    </style>
    """,
    unsafe_allow_html=True
)

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
        # Wyświetlenie wprowadzonych informacji
        st.subheader("Informacje Użytkownika")
        st.write(user_input)

        # Parsowanie informacji użytkownika
        user_info = [info.strip() for info in user_input.split(",")]

        # Generowanie możliwych haseł
        # passwords = db(user_info) // to db to jest plik który podłączamy, nie wiem czy to ten
        # user_info to jest to co wpisuje użytkownik na stronie
        # passwords to jest wynik z kodu, czyli te możliwe hasła

        # Wyświetlanie wyników
        st.subheader("Możliwe Hasła")
        # st.write(passwords)
    else:
        st.error("Proszę wprowadzić informacje.")

# Informacja o stopce
st.markdown("\*\*Uwaga:\*\* Wszystkie dane wprowadzone w aplikacji są przetwarzane lokalnie.")

