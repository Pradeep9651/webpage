import streamlit as st



# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")
with st.container():
    st.subheader("Hi, I am Pradeep  :wave:")
    st.title("A Software engineer from India")
    st.write("i am passionate about finding ways to use python and VBA to be moreeffective")
    st.write("[Learn More >](https://pythonandvba.com)")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            - are looking for a way to leverage the power of Python in their day-to-day work.
            - are struggling with repetitive tasks in Excel and are looking for a way to use Python and VBA.
            - want to learn Data Analysis & Data Science to perform meaningful and impactful analyses.
            - are working with Excel and found themselves thinking - "there has to be a better way.
            """
        )