import os
from tempfile import NamedTemporaryFile
import streamlit as st
from PIL import Image
from langchain.agents import create_csv_agent
from langchain.llms import OpenAI
import pandas as pd
from dotenv import load_dotenv

def app():

    #Load api keys from environment file
    load_dotenv()
    #if os.getenv("OPENAI_API_KEY") is not None or os.getenv("OPENAI_API_KEY")!="":
    #    print("Key is present")
    #else:
    #    print("Key not set. Check key!")

    # Set page configurations
    st.set_page_config(page_title="Chat with your CSV")
    st.title("Chat with your CSV")

    # image on left side
    with st.sidebar:    
        image=Image.open("logo.jpeg")
        st.image(image,width=200)
    
    #Upload a CSV file
    upload_file= st.file_uploader("Choose a CSV file",type="csv")
       
    if upload_file:
        with NamedTemporaryFile() as f:
            f.write(upload_file.getvalue())
            llm=OpenAI(temperature=0)
            question=st.text_input("Type your question")
            button=st.button("Execute")
            agent=create_csv_agent(llm,f.name,verbose=True)
        
            if button:
                if question is not None and question!="":
                    with st.spinner("Generating response..."):
                        response=agent.run(question)
                        st.write(response)
                else:
                    st.error("Please eneter your question")
    

if __name__ == "__main__":
    app()