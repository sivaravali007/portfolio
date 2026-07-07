import streamlit as st

st.set_page_config(page_title="A V Siva Ravali", page_icon="👩‍💻", layout="wide")

st.markdown("""
<style>

.main-title{
font-size:50px;
font-weight:bold;
color:#1F77B4;
}

.sub-title{
font-size:25px;
color:gray;
}

.card{
padding:20px;
border-radius:15px;
background-color:#F8F9FA;
box-shadow:0px 0px 10px #CCCCCC;
}

</style>
""", unsafe_allow_html=True)


col1,col2=st.columns([1,2])

with col1:
    st.image("assets/Siva_Ravali_Photo.jpg",width=280)

with col2:

    st.markdown("<div class='main-title'>A V Siva Ravali</div>",unsafe_allow_html=True)

    st.markdown("<div class='sub-title'>Quality Analyst | ETL Tester | SQL | Senior drug safety associate | Datascience Learner</div>",unsafe_allow_html=True)

    st.write("")

    st.success("""
✔ 5+ Years Professional Experience

✔ Quality Analyst 

✔ ETL Testing

✔ SQL Validation

✔ Manual Testing

✔ Pharmacovigilance & Quality Control

✔ Learning Datascience with machine learning and Python
""")

st.write("")

# st.markdown("## Career Objective")

# st.info("""
# To utilize my technical and analytical skills in Software Testing and Data Validation while continuously improving myself and contributing to organizational growth.
# """)

st.write("")

st.markdown("""
<style>

.highlight-title{
    font-size:42px;
    font-weight:700;
    color:#1F3C88;
    margin-bottom:20px;
}

.card{
    background:linear-gradient(135deg,#F8FAFC,#EEF4FF);
    padding:25px;
    border-radius:18px;
    text-align:center;
    box-shadow:0px 4px 12px rgba(0,0,0,0.12);
    border-top:6px solid #2563EB;
    transition:0.3s;
    height:270px;
}

.card:hover{
    transform:translateY(-8px);
    box-shadow:0px 8px 20px rgba(0,0,0,0.18);
}

.icon{
    font-size:40px;
}

.heading{
    color:#4B5563;
    font-size:18px;
    font-weight:600;
    margin-top:10px;
}

.value{
    font-size:34px;
    font-weight:700;
    color:#1E3A8A;
    margin-top:20px;
}

.desc{
    color:#6B7280;
    font-size:10px;
    margin-top:15px;
}

</style>
""", unsafe_allow_html=True)

st.markdown("<div class='highlight-title'>Professional Highlights</div>", unsafe_allow_html=True)

col1,col2,col3,col4=st.columns(4)

# st.markdown("## Highlights")

# c1, c2, c3, c4 = st.columns(4)

# c1.metric("Experience", "5+ Years")

# c2.metric("Healthcare", "Pharma & PV")

# c3.metric("Clinical Trials", "ICSR • SAE • SUSAR")

# c4.metric("QA Testing", "ETL • UAT • SQL")

with col1:
    st.markdown("""
    <div class="card">
        <div class="icon">💼</div>
        <div class="heading">Experience</div>
        <div class="value">5+ Years</div>
        <div class="desc">
        Healthcare & Software Industry
        </div>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div class="card">
        <div class="icon">💊</div>
        <div class="heading">Healthcare Domain</div>
        <div class="value">4 Years</div>
        <div class="desc">
        Pharmacovigilance<br>
        Drug Safety<br>
        Regulatory Compliance
        </div>
    </div>
    """, unsafe_allow_html=True)
with col3:
    st.markdown("""
    <div class="card">
        <div class="icon">🧬</div>
        <div class="heading">Clinical Trials</div>
        <div class="value">ICSR</div>
        <div class="desc">
        SAE • SUSAR<br>
        MedDRA • ARGUS<br>
        RAVE Database
        </div>
    </div>
    """, unsafe_allow_html=True)
with col4:
    st.markdown("""
    <div class="card">
        <div class="icon">💻</div>
        <div class="heading">Quality Assurance</div>
        <div class="value">ETL & SQL</div>
        <div class="desc">
        Manual Testing<br>
        UAT Testing<br>
        Data Validation
        </div>
    </div>
    """, unsafe_allow_html=True)
st.write("")

st.info("""
### ⭐ My Strength

I bring a unique combination of **5+ years of Healthcare & Pharmacovigilance expertise**
and **Software Quality Assurance** experience. My background in clinical trials,
drug safety, regulatory compliance, ETL testing, SQL validation, and manual testing
helps me ensure high-quality, compliant, and reliable software solutions for the healthcare domain.
""")