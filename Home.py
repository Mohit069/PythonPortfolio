import pandas
import streamlit as st
import pandas as pd
st.set_page_config(layout="wide")

col1,col2 = st.columns([2,2])
with col1:
    st.image("images/mohit.jpg",width=400)
with col2:
    st.title("Mohit Singh")
    content = '''I'm an individual currently pursuing a Master's Degree in MCA (Masters of Computer Application)
     from St. Xavier Collage. With a strong passion for technology,
     I constantly exploring the latest advancements in the field. My primary focus lies in
      the domains of Software, Web and App Development.'''
    st.info(content)

col3,empty_col,col4 = st.columns([1.5,.5,1.5])
df=pd.read_csv("data.csv")
with col3:
    for index,row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+row["image"],width=300)
        st.write(f"[source_code]({row['url']})")

with col4:
    for index,row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+row["image"],width=300)
        st.write(f"[source_code]({row['url']})")
