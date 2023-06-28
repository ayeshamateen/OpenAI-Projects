import os
import streamlit as st
import pandas as pd
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI
#from langchain.agents import create_pandas_dataframe_agent
#from langchain.llms import OpenAI
from apikey import apikey
import matplotlib

os.environ["OPENAI_API_KEY"]=apikey

# Instantiate an llm
llm= OpenAI(api_token=apikey)
pandas_ai= PandasAI(llm)

# Initialize to display charts
matplotlib.use('TkAgg')

#Define Streamlit app

def app():
    st.title("Analysis with PandasAI")
    st.write("Upload a CSV file")
    file= st.file_uploader("Upload a CSV file",type=['csv'])
    if not file:
        st.stop()
    
    df = pd.read_csv(file)
    # data preview
    st.write(df.head())

    prompt = st.text_area("Enter your question:")

    if st.button("Execute"):
        if prompt:
            with st.spinner("Generating response..."):
                st.write(pandas_ai.run(df,prompt=prompt))
        else:
            st.warning("Please enter a prompt")

if __name__ == "__main__":
    app()