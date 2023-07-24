import streamlit as st
from PIL import Image

st.set_page_config(page_title='QWISHI', page_icon='🏢', layout="centered", initial_sidebar_state="expanded")


hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.success("This is a demo...")
           
img1 = Image.open("logo.png", "r")
st.sidebar.image(img1)
st.sidebar.write("Where students find a home away from home, and where hostels make themselves known. Welcome!!")

st.title("QWISHI.")

img = Image.open('home_pic.jpg')
st.image(img, caption="Qwishi's developer hostel room.")


st.subheader("🔎Find a home away from home.")

st.text_input("Search by keywords e.g. example1 Hostels, nickname")
# filters

expander1 = st.expander(label = "Use filters.", expanded=False)

# filter by price

expander1.slider('Price: ', min_value=1000, max_value=15000, step=500, value=2000)

# filter by number of room occupants

rad_butt = expander1.radio("No. of room occupants:", options = ("1", "2", "3", "4", "5"))

# filter by availabity of a kitchenette

kitchenette = ["Available.", "Unavailable.", "Available but utensils washing area outside."]
selected_kitchnette = expander1.selectbox("Select kitchenette status:", kitchenette)


# TEMPLATE.

expander2 = st.expander(label = "Use a TEMPLATE to summarise everything", expanded=False)
expander2.subheader("Under rigorous development")



# HOSTELS.
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.subheader("🚀Explore")
st.subheader("   Example1 Hostels.")
st.image("https://images.unsplash.com/photo-1460317442991-0ec209397118?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NXx8YXBhcnRtZW50fGVufDB8fDB8fHww&auto=format&fit=crop&w=500&q=60")
data = "Check out example1 Hostels"
expander3 = st.expander(label = data , expanded = False)
expander3.write("Room occupation: Single room @ 7000 Kshs, Double room @ 4500 Kshs per person")
expander3.write("Food: Kitchenette available")
expander3.write("Security: Gate, 24/7 security guard, 24/7 CCTV surveillance, Perimeter fence, Fire extinguishers and siren")
expander3.write("Electricity: Catered under rent")

tab1, tab2, tab3 = expander3.tabs(["Kitchenette", "Bathroom", "Toilet"])

with tab1:

    st.image("https://images.unsplash.com/photo-1556037843-347ddff9f4b0?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTJ8fGtpdGNoZW58ZW58MHx8MHx8fDA%3D&auto=format&fit=crop&w=500&q=60")

with tab2:

    st.image("https://images.unsplash.com/photo-1571781418606-70265b9cce90?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8Y2FtcHVzJTIwYmF0aHJvb218ZW58MHx8MHx8fDA%3D&auto=format&fit=crop&w=500&q=60")

with tab3:

    st.image("https://images.unsplash.com/photo-1587527901949-ab0341697c1e?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NHx8Y2FtcHVzJTIwYmF0aHJvb218ZW58MHx8MHx8fDA%3D&auto=format&fit=crop&w=500&q=60")



st.subheader("   Example2 Hostels.")
st.image("https://images.unsplash.com/photo-1515263487990-61b07816b324?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8YXBhcnRtZW50fGVufDB8fDB8fHww&auto=format&fit=crop&w=500&q=60")
data = "Check out example2 Hostels"
expander4 = st.expander(label = data , expanded = False)

expander4.write(" ")
expander4.write(" ")
expander4.write(" ")
expander4.write("Room occupation: Single room @ 7000 Kshs, Double room @ 4500 Kshs per person")
expander4.write("Food: Kitchenette unavailable, restaurant in the hostel")
expander4.write("Water: Metre, Pay NYEWASCO")
expander4.write("Electricity: Token, Pay KPLC")

tab4, tab5, tab6 = expander4.tabs(["Kitchenette", "Bathroom", "Toilet"])

with tab4:

    st.image("https://images.unsplash.com/photo-1550223026-0d6fd780c560?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTV8fGtpdGNoZW58ZW58MHx8MHx8fDA%3D&auto=format&fit=crop&w=500&q=60")

with tab5:

    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRdk0NFSfguJAwX6mgWkjkQ-VvFHk8_YOnKAg&usqp=CAU")

with tab6:

    st.image("https://images.unsplash.com/photo-1569597967185-cd6120712154?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8dG9pbGV0fGVufDB8fDB8fHww&auto=format&fit=crop&w=500&q=60")



st.subheader("   Example3 Hostels.")
st.image("https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OHx8YXBhcnRtZW50fGVufDB8fDB8fHww&auto=format&fit=crop&w=500&q=60")
data = "Check out example3 Hostels"
expander5 = st.expander(label = data , expanded = False)

expander5.write(" ")
expander5.write(" ")
expander5.write(" ")
expander5.write("Room occupation: Single room @ 7000 Kshs, Double room @ 4500 Kshs per person")
expander5.write("Food: Kitchenette available, sink outside")
expander5.write("Water: Metre, Pay NYEWASCO")
expander5.write("Electricity: Token, Pay KPLC")

tab7, tab8, tab9 = expander5.tabs(["Kitchenette", "Bathroom", "Toilet"])

with tab7:

    st.image("https://images.unsplash.com/photo-1574739782594-db4ead022697?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTh8fGtpdGNoZW58ZW58MHx8MHx8fDA%3D&auto=format&fit=crop&w=500&q=60")

with tab8:

    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTuIMcDvzQNFwtObvPCMed72JjbmyFbX4v8bA&usqp=CAU")

with tab9:

    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR5qC0ImilaymhamG_BCeSBUTy-I8PvWQrRmw&usqp=CAU")
