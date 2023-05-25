import streamlit as st

st.title("Mon application Streamlit")

try:
    with open('html.pbit', 'r', encoding='utf-8') as f:
        html_contents = f.read()
except FileNotFoundError:
    st.error("Le fichier html.pbit n'a pas été trouvé.")
    html_contents = ""
except Exception as e:
    st.error(f"Une erreur s'est produite lors de la lecture du fichier html.pbit : {e}")
    html_contents = ""

if html_contents:
    st.componentsThis updated code includes some error handling that attempts to read in the contents of `html.pbit` and displays an error message if there are any issues.

If the file is read in successfully, the code calls the `st.components.v1.html` function to display the dashboard in the Streamlit app. This should help you identify any issues with reading in the file and ensure that your Streamlit app runs without errors.
