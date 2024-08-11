from pathlib import Path
import streamlit as st



from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
profile_pic = current_dir / "assets" / "profile-pic.png"
resume_file = current_dir / "assets" / "CV_Pradeep_Yadav.pdf"
# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")
with st.container():
    left_column, right_column = st.columns(2)
with left_column:
    st.subheader("Hi, I am Pradeep  :wave:")
    st.title("A Software engineer from India")

    st.write("i am passionate about Laveraging my technical skills which i have gained during my studies")
   
with right_column:
    if profile_pic.exists():
        img = Image.open(profile_pic)
        st.image(img, width=250)
    else:
        st.write("Profile picture not found.")
        st.subheader("Know more :")
    st.write("[Linkedin >](https://www.linkedin.com/in/pradeep-yadav-5aa47a20b/)")
    st.write("[Github >](https://github.com/Pradeep9651)")
with open(resume_file, "rb") as pdf_file:
        PDFbyte = pdf_file.read()
        st.download_button(label="Download Resume", 
                           data=PDFbyte,
                           file_name="CV_Pradeep_Yadav.pdf",
                           mime='application/octet-stream')

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
           - "there has to be a better way.
            """
        )