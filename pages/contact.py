import streamlit as st
from funcs import send_email
from email.message import EmailMessage
st.title("CONTACT")
st.divider()

st.subheader("This web application was made by Capătă Ciprian."
             " Please reach out for any questions/ information by:")

st.markdown("#")

st.text("Phone: +40075 870 5895")
st.text("Gmail: cipriangheorghecapata@gmail.com")

st.markdown("#")

st.subheader("Or by completing the from below:")
with st.form(key='emails_form'):
    user_email = st.text_input("Your email")
    raw_message = st.text_area("Your message")

    button = st.form_submit_button("Submit")
    if button:

        send_email(user_email, message_raw=raw_message)
        st.info("Email sent successfully!")