import streamlit as st
import random
import string

st.title("password best generator")

length = st.slider("password length", 8, 1000, 16)
chars= string.ascii_letters + string.digits + "@$#&!^&*"
if st.button("Generate Passwordd"):
    password= "".join(random.choice(chars) for _ in range (length))
    st.code(password)
    st.text_area("generated pass", password, height=300)
