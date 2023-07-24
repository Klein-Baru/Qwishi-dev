import streamlit as st


st.set_page_config(page_title='QWISHI', page_icon='🏢', layout="centered", initial_sidebar_state="auto")
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.title("QWISHI.")

st.image("https://images.unsplash.com/photo-1562577309-4932fdd64cd1?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OHx8c29jaWFsJTIwbWVkaWF8ZW58MHx8MHx8fDA%3D&auto=format&fit=crop&w=500&q=60")
st.write("Help others Find a Home away from home by sharing widely.")

st.write(" ")
st.code("https://qwishi.streamlit.app/", language="python")
st.write(" ")
st.write("Copy the above link to SHARE across your favourite social media platforms.... and awwh!🫣 remember to bookmark this site☺️😇.")

