import streamlit as st

st.title("Mon application Streamlit")

try:
   with open('html.pbit', 'r', encoding='cp1252') as f:
    html_contents = f.read()
except FileNotFoundError:
    st.error("Le fichier html.pbit n'a pas été trouvé.")
    html_contents = ""
except Exception as e:
    st.error(f"Une erreur s'est produite lors de la lecture du fichier html.pbit : {e}")
    html_contents = ""

if html_contents:
    st.components
