import streamlit as st
from Send_Email import  sendemail


st.header("Contact Us")

with st.form(key="contactform"):
    user_email = st.text_input("Enter Your Email")
    message = st.text_area("Enter Your Message")
    message = message + '\n' + user_email
    btn = st.form_submit_button()

    if btn:
        sendemail(message)
        st.info("Sent Sucessfully")
