import streamlit as st
import time

st.title("To jest strona Iwony Milewskiej")
col1, col2 = st.columns([1, 1])


col1.markdown("## Witam na stronie Iwonki!")
col1.markdown("Więcej o stronie: [iwonamilewska.pl](https://iwonamilewska.pl/)")

uploades_photo = col2.file_uploader("Upload a photo")