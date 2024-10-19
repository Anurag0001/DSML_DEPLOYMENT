import streamlit as st

st.header("Basic Calculator!")

def square(num):
    return num*num

num = st.number_input("Insert a NUmber")
st.write("The current Number is", num)




if st.button("Calcualte Square"):
    result=square(num)

    st.text(result)


