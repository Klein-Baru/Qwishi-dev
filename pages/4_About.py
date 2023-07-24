import streamlit as st
from PIL import Image

st.set_page_config(page_title='QWISHI', page_icon='🏢', layout="centered", initial_sidebar_state="auto")

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.title("QWISHI")
st.image("data:image/jpeg;base64,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")
st.write("This site made by a DeKUT student aims to give DeKUT students, freshmen and ongoing, local and international, an easy time while searching for a hostel by providing the information they need, at their palm of their hands. We also help hostels publicise and market themselves, widely and directly, to students.")


st.subheader("Endorsed by The Dedan Kimathi University of Technology.", anchor= "Endorsed by The Dedan Kimathi University of Technology")
img = Image.open('dekut_logo.png')
st.image(img)
