import streamlit as st

st.title("📞 Contact")

st.write("---")

col1,col2=st.columns(2)

with col1:

    st.subheader("Contact Information")

    st.write("📧 Email")
    st.info("sivaravali007@gmail.com")

    st.write("📱 Phone")
    st.info("+91 6300295003")

    st.write("💻 GitHub")
    st.code("https://github.com/sivaravali007")

    st.write("📍 Location")
    st.info("Hyderabad, India")

with col2:

    st.subheader("Career Interests")

    st.success("""
Looking for opportunities in

✔ Healthcare Data Analyst

✔ Clinical Data Analyst

✔ Healthcare Analytics

✔ SQL & Data Analysis

✔ Python & Data Visualization
""")

st.write("---")

st.markdown(
"""
### Thank You!

Thanks for visiting my portfolio.

Let's connect and build something amazing together.
"""
)