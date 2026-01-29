import streamlit as st

st.set_page_config(page_title="Simple Form", page_icon="📝")

st.title("📝 Registration Form")

with st.form("user_form"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    department = st.selectbox(
        "Department",
        ["IT", "CS", "ECE", "Mechanical", "Other"]
    )
    feedback = st.text_area("Feedback")

    submitted = st.form_submit_button("Submit")

if submitted:
    if name and email:
        st.success("✅ Form submitted successfully!")
        st.write("**Name:**", name)
        st.write("**Email:**", email)
        st.write("**Department:**", department)
        st.write("**Feedback:**", feedback)
    else:
        st.error("❌ Please fill Name and Email")
