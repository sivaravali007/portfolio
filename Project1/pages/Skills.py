import streamlit as st

st.title("💻 Technical Skills")

st.write("---")

col1,col2=st.columns(2)

with col1:

    st.subheader("Testing")

    st.progress(90)
    st.write("Manual Testing")
    
    st.progress(90)
    st.write("Playwright automation Testing")

    st.progress(85)
    st.write("ETL Testing")

    st.progress(85)
    st.write("UAT Testing")

    st.progress(80)
    st.write("Functional Testing")

with col2:

    st.subheader("Programming")

    st.progress(80)
    st.write("SQL")

    st.progress(70)
    st.write("Python")

    st.progress(60)
    st.write("NumPy & Pandas")

st.write("---")

st.subheader("Tools")

tools=[
"SSMS",
"Azure DevOps",
"VS Code",
"MS Excel",
"GitHub"
]

for tool in tools:
    # st.markdown(f"<span style='color:green'>{tool}</span>", unsafe_allow_html=True)
    st.success(tool)

st.write("---")

st.subheader("Soft Skills")


skills = [
    "Communication",
    "Problem Solving",
    "Team Work",
    "Time Management",
    "Quick Learning",
    "Attention to Detail"
]

for skill in skills:
    st.write(f"✅ {skill}")