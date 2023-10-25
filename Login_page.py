import streamlit as st
from Electrica.main import get_data_el
from EONgaz.main import get_data_gaz
st.set_page_config(
    page_title="Title"
)
st.text("Welcome ... etc")

service = st.radio(
    "Select for which service ... etc",
    ["1", "2", '3'],
    captions= ["EON/ Gas", "Electrica/ Electricity", 'Both'],
    horizontal=True
)

if service == "1":
    st.text("Please insert login credentials for EON")
    user_name = st.text_input("User name")
    user_pass = st.text_input("Password")
    if user_name and user_pass:
        data_list_raw = get_data_gaz(username=user_name, password=user_pass)
        if isinstance(data_list_raw, list):
            data_list = [data_list_raw[1], data_list_raw[3]]

            st.text("Login successful!")
            log_in_stat = True
            st.text(data_list[0])
            st.text(data_list[1])
        else:
            st.text("Incorrect credentials.")
            log_in_stat = False
if service == "2":
    st.text("Please insert login credentials for Electrica")
    user_name = st.text_input("User name")
    user_pass = st.text_input("Password")
    if user_name and user_pass:
        data_list_raw = get_data_el(username=user_name, password=user_pass)
        if isinstance(data_list_raw, list):
            data_list = [data_list_raw[3], data_list_raw[4]]

            st.text("Log-in successful!")
            log_in_stat = True

            st.text(data_list[0])
            st.text(data_list[1])
        else:
            st.text("Incorrect credentials.")
            log_in_stat = False

if service == '3':
    st.text("Please insert login credentials for *as follows*")
    st.subheader("EON")
    user_name_g = st.text_input("User name EON")
    user_pass_g = st.text_input("Password EON")
    st.subheader("Electrica")
    user_name_e = st.text_input("User name Electrica")
    user_pass_e = st.text_input("Password Electrica" )