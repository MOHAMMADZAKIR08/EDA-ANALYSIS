import streamlit as st
import seaborn as sns
import pandas as pd
import numpy as np
from streamlit_pandas_profiling import st_profile_report
from pandas_profiling import ProfileReport
# TITLE 
st.markdown('''
# **Exploratory data analysis**
.Developed by **x,y,z**''')
with st.sidebar.header("Upload dataset in (csv.file)"):
    uploaded_file = st.sidebar.file_uploader("UPLOAD YOUR FILE",type=['csv'])
    df=sns.load_dataset("titanic")
    st.write(df)
    st.sidebar.markdown("[Example csv file],(https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset)")
#profiling reports for pandas
if uploaded_file is not None:
    @st.cache
    def load_csv():
        csv=pd.read_csv(uploaded_file)
        return csv
    df = load_csv
    pr = ProfileReport(df,explorative=True)
    st.header('**Input df**')
    st.write(df)
    st.write('---')
    st.header('**Profile Reports with pandas**')
    st_profile_report(pr)
else:
    st.info('Awaiting for upload a file')
    if st.button('Press to use example data'):
    # examplr data
        @st.cache
        def load_data():
             a=pd.DataFrame(np.random.rand(100,5),
               columns=['age','bostan','clerks','haryana','ear'])
             return a
        df=load_data()
        pr = ProfileReport(df,explorative=True)
        st.header('**Input df**')
        st.write(df)
        st.write('---')
        st.header('**Profile Reports with pandas**')
        st_profile_report(pr)
        

    
