import streamlit as st

st.title("👩 About Me")

st.write("---")

col1, col2 = st.columns([2, 1])

with col1:

    st.markdown("""
### Hi, I'm **A V Siva Ravali**

I am a **Quality Analyst** with **1 year of experience** in **ETL Testing, SQL Validation, Manual Testing, Functional Testing, and UAT**.

My most recent role was as a **Quality Analyst at AtkinsRéalis**, where I worked on ETL testing, SQL-based data validation, and quality assurance activities.

Prior to transitioning into software testing, I built **4+ years of experience in Pharmacovigilance and Healthcare**, gaining expertise in **Clinical Trials, Drug Safety, Regulatory Compliance, and Patient Safety**.

I am currently enhancing my skills in **Python, Data Analysis, and Datascience with machine learning and deep learning** while actively seeking opportunities in **Software Testing and Quality Assurance**.
""")

with col2:

    st.info("""
### 💼 Career Focus

🎯 Healthcare Data Analyst

🏥 Healthcare Domain Expert

📊 SQL | Python | Data Analysis

📍 Open to Work – Hyderabad

🤝 Ready for New Opportunities
""")

st.write("---")

st.subheader("🚀 Professional Summary")

col1, col2 = st.columns(2)

with col1:

    st.success("""
               
✔ 1 Year in ETL Testing

✔ SQL Data Validation

✔ Manual Testing

✔ Functional Testing

✔ User Acceptance Testing (UAT)
""")

with col2:

    st.success("""
✔ 4+ Years in Healthcare

✔ Clinical Trial Knowledge

✔ Pharmacovigilance

✔ Strong Analytical Skills

✔ Excellent Communication
""")

st.write("---")

st.subheader("🎓 Education")

st.markdown("""
**🎓 M.Pharmacy (Pharmacology)**  
Sri Padmavathi Mahila Visvavidyalayam

**🎓 B.Pharmacy**  
Creative Educational Society's College of Pharmacy
""")

st.write("### 🏆 Academic Achievements")

col1, col2 = st.columns(2)

with col1:
    st.success("🏅 GPAT AIR 1354")

with col2:
    st.success("🏅 PGECET Rank 14")
    
    