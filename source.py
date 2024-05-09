from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Pradeep Yadav"
PAGE_ICON = ":wave:"
NAME = "Pradeep Yadav"
DESCRIPTION = """
Software Developer.
"""
EMAIL = "yadavpradeep2313@gmail.com"

# --- Social Links ---
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/pradeep-yadav-5aa47a20b/",
    "GitHub": "https://github.com/Pradeep9651",
    "leetcode":"https://leetcode.com/u/yadavpradeep2313/"
}
PROJECTS = {
    "🏆 Sales Dashboard - Comparing sales across three stores": "https://youtu.be/Sb0A9i6d320",
    "🏆 Income and Expense Tracker - Web app with NoSQL database": "https://youtu.be/3egaMfE9388",
    "🏆 Brain Tumor Detection System-Web app using Python & Streamlit":"https://github.com/Pradeep9651/Brain_tumor"
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- Education & QUALIFICATIONS ---
st.write("#")
st.subheader("Education & QUALIFICATIONS")
st.write(
    """
- ✔️ Bachelor of Information Technology., United Institute Of Technology Expected 2024
- ✔️ High School (X) , Kendriya Vidyalaya, CBSE Board . 2018
- ✔️Intermediate (XII) , Ramanujan Public School, CBSE Board . 2020

"""
)


# --- SKILLS ---
st.write("#")
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python, SQL, VBA, C++
- 📊 Data Visulization: PowerBi, MS Excel, Plotly
- 📚 Modeling: Logistic regression, linear regression, decition trees
- 🗄️ Databases: MongoDB, MySQL
"""
)


# --- TRAINING/ CERTIFICATION COURSES ---
st.write("#")
st.subheader("TRAINING/ CERTIFICATION COURSES")
st.write("---")

# --- Certification 1
st.write("🚧", "**Python Programming**")


# --- Certification 2
st.write("#")
st.write("🚧", "**Data Analytics Virtual experience**")


# --- Certification 3
st.write("#")
st.write("🚧", "**Full stack development**")

# --- Projects & Accomplishments ---
st.write("#")
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")