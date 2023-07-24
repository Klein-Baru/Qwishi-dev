import streamlit as st

st.set_page_config(page_title='QWISHI', page_icon='🏢', layout="centered", initial_sidebar_state="auto")

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.title("QWISHI")
st.image("https://images.unsplash.com/photo-1596524430615-b46475ddff6e?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8Y29udGFjdCUyMHVzfGVufDB8fDB8fHww&auto=format&fit=crop&w=500&q=60")
st.subheader("We care about you, reach us using the following contacts ONLY:")

st.write(" ")
st.write(" ")
st.write("📲Phone Call and Messages:")
st.code("+254 714632602", language="python")

st.write("WhatsApp:")
st.code("+254 714632602", language="python")

st.write("📧Email:")
st.code("qwishi@gmail.com", language="python")
