import streamlit as st

st.title("Password complexity checker")

password = st.text_input("Password",placeholder="Enter password")
special = "@_!#$%^&*()<>?/\|}{~:"

if password is not None:
    strength = 0
    for i in password:
        if i.islower():
            strength+=1
            break
    for i in password:
        if i.isupper():
            strength+=1
            break
    for i in password:
        if i.isnumeric():
            strength+=1
            break
    for i in password:
        if i in special:
            strength+=1
            break

    if strength==1 or strength==2 or (len(password)<5 and len(password)>0):
        st.write("Password strength is Weak")
    elif strength==3 or (len(password)<8 and len(password)>0):
        st.write("Password strength is medium")
    elif strength==4 or len(password)>7:
        st.write("Password strength is strong")