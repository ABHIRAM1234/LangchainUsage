# QA Chatbot
import os
import streamlit as st
from langchain.llms import OpenAI
from dotenv import load_dotenv

load_dotenv()  # take env variables from .env

def get_openai_reponse(question):
    llm = OpenAI(openai_api_key=os.getenv("OPEN_API_KEY"), model_name = "text-davinci-003", temperature=0.5)
    response = llm(question)
    return response

st.set_page_config(page_title="Q&A Demo")

st.header("Langchain Application")

input = st.text_input("Input: ", key="input")
response = get_openai_reponse(input)

submit = st.button("Ask the question")

#Checking if button is clicked

if submit:
    st.subheader("The response is")
    st.write(response)
