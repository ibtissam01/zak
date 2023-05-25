import streamlit as st

st.title("Mon application Streamlit")

# Incorporer le tableau de bord Power BI
st.components.v1.html(open('html.pbit', 'r', encoding='utf-8').read(), height=600)
