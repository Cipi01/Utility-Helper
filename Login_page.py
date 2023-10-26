import streamlit as st
from Electrica.main import get_data_el
from EONgaz.main import get_data_gaz

st.set_page_config(
    page_title="Utility helper"
)
st.title("Welcome to Utility Helper v.1.0. !")
st.subheader(
    "This is the early version of an application meant to support users with their utility index transmission dates,"
    "aswell as their current bill.")

service = st.radio(
    "Please select the utility.",
    ["1", "2", '3'],
    captions=["EON/ Gas", "Electrica/ Electricity", 'Both'],
    horizontal=True,
    index=None
)

if service == "1":
    st.text("Please insert login credentials for EON")
    user_name = st.text_input("User name")
    user_pass = st.text_input("Password", type="password")
    if st.button("Start", key="eon_button"):
        if not user_name or not user_pass:
            st.error("Please input a value inside the username or password field!", icon="🚨")
        else:
            data_list_raw = get_data_gaz(username=user_name, password=user_pass)
            if isinstance(data_list_raw, list):
                data_list = [data_list_raw[1], data_list_raw[3]]

                st.success("Login successful!",icon="✅")
                log_in_stat = True
                st.text(data_list[0])
                st.text(data_list[1])
            else:
                st.error("Incorrect credentials.", icon="🚨")
                log_in_stat = False

if service == "2":
    st.text("Please insert login credentials for Electrica")
    user_name = st.text_input("User name")
    user_pass = st.text_input("Password", type="password")
    if st.button("Start", key="El_button"):
        if not user_name or not user_pass:
            st.error("Please input a value inside the username or password field!", icon="🚨")
        else:
            data_list_raw = get_data_el(username=user_name, password=user_pass)
            if isinstance(data_list_raw, list):
                data_list = [data_list_raw[3], data_list_raw[4]]

                st.success("Log-in successful!",icon="✅")
                log_in_stat = True

                st.text(data_list[0])
                st.text(data_list[1])
            else:
                st.error("Incorrect credentials.", icon="🚨")
                log_in_stat = False

if service == '3':
    st.text("Please insert login credentials for EON and Electrica.")
    st.subheader("EON")
    user_name_g = st.text_input("User name EON")
    user_pass_g = st.text_input("Password EON", type="password")
    st.subheader("Electrica")
    user_name_e = st.text_input("User name Electrica")
    user_pass_e = st.text_input("Password Electrica", type="password")

    if st.button("Start", key="Mixed_button"):
        if not user_name_g or not user_pass_g or not user_name_e or not user_pass_e:
            st.error("Please input a value inside the username or password field!", icon="🚨")
        else:
            data_list_raw_e = get_data_el(username=user_name_e, password=user_pass_e)
            data_list_raw_g = get_data_gaz(username=user_name_g, password=user_pass_g)

            if isinstance(data_list_raw_e, list) and isinstance(data_list_raw_g, list):
                data_list_e = [data_list_raw_e[3], data_list_raw_e[4]]
                data_list_g = [data_list_raw_g[1], data_list_raw_g[3]]
                st.success("Log-in successful!",icon="✅")
                st.subheader("EON")
                st.text(f"Current bill: {data_list_g[0]}")
                st.text(f"Current date for auto-index: {data_list_g[1]}")

                st.subheader("Electrica")
                st.text(f"Current bill: {data_list_e[0]}")
                st.text(f"Current date for auto-index: {data_list_e[1]}")
            else:
                st.error("Incorrect credentials!", icon="🚨")
