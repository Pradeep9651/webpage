from pathlib import Path
import streamlit as st



from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
profile_pic = current_dir / "assets" / "profile-pic.png"
# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")
with st.container():
    st.subheader("Hi, I am Pradeep  :wave:")
    st.title("A Software engineer from India")
    st.write("i am passionate about finding ways to use python and VBA to be moreeffective")
    st.write("Know more :")
    st.write("[Linkedin >](https://www.linkedin.com/in/pradeep-yadav-5aa47a20b/)")
    st.write("[Github >](https://github.com/Pradeep9651)")

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