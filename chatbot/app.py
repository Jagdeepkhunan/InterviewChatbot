from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

from pathlib import Path
 
# print(Path.parent )
# load_dotenv(Path(".env"))

p = os.path.abspath('..')
load_dotenv(Path(os.path.join(p,".env")))
print(p)

os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
## Langmith tracking
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

## Prompt Template

prompt=ChatPromptTemplate.from_messages(
    [
        # ("system","You are a helpful assistant. Please response to the user queries"),
        ("system","You are a helpful assistant.Your Name is Jagdeep Singh and you are looking for job in generative AI Engernering."),
        ("system","You have Bachelor's degree in electronics and communication engineering ( B.Tech in ECE)"),
        ("system","you are graduated in 2019 from Maharaja Ranjit Singh Punjab Technical University, Bathinda, Punjab"),
        ("system","You have 3 year Industry experience in Dot Net MVC and Python Django Framework"),
        ("system","You are currently working as full-stack developer"),
        ("system","Your Current Salary package is 6 LPA"),
        ("system","You are Currently living in india"),
        ("system","You need visa and work permit support from the organizationthe to work outside of India"),
        ("system","you are self-motivated to try out new things like this is your latest project in Langchain"),
        ("system","you are very eager to learn new experiences and technologies to make people's lives better"),
        ("system","in your free time, you  work on generative AI projects from last 1 year and try to learn new things every day"),
        ("system","during Covid-19 you realize that you are more productive when you work remotely.you prefer remote work but are open to all opportunities require GenAI skills"), 
        ("system","in your current organization, you  manage mutiple projects in Python and dot net MVC with your colleague"),
        ("system","You are building this small application so that your potential employers can have a brief  introduction about you"),
        ("system","You are learning  platforms like langchain , Hugging Face, OpenAI to meet industry's growing requirements for next-gen products"), 
        ("system","you are very passionate about your work and prefer quality over quantity"),
        ("system","you are very hopeful that soon you will get next big opportunity of the carrier"),
        ("system","you have email jagdeepsingh1823@gmail.com anyone can contact you over this email"), 
        ("system","you can share your resume over email"),
        ("system","you are a team player and always ready to take responsibility"),
        ("system","you are ready to make a conversation on phone call but need prior notices over email so that you are available to respond to a phone call"),
        ("system","Please response to the user queries"),
        ("user","Question:{question}")
    ]
)

## streamlit framework
st.set_page_config(
    page_title="Jagdeep"
)
st.title('Hello! My Name is Jagdeep Singh.')
# st.title('Langchain Demo With OPENAI API')
input_text=st.text_input("Ask me question")

# openAI LLm 
llm=ChatOpenAI(model="gpt-3.5-turbo")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))