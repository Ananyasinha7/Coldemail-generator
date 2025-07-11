import streamlit as st
from utils import clean_text
from chains import Chain
from portfolio import Portfolio
import langchain
import os
os.environ["USER_AGENT"] = "cold-email-generator/1.0"

from langchain_community.document_loaders import WebBaseLoader

def create_streamlit_app(llm,portfolio,clean_text):
        st.title("Cold Mail Generator")
        url_input=st.text_input("Enter a URL:",value="")
        submit_button=st.button("Submit")
        if submit_button:
                try:
                    loader=WebBaseLoader([url_input])
                    data=clean_text(loader.load().pop().page_content)
                    portfolio.load_portfolio()
                    jobs=llm.extract_jobs(data)
                    for job in jobs:
                           skills=job.get('skills',[])
                           links=portfolio.query_links(skills)
                           email=llm.write_mail(job,links)
                           st.code(email,language='markdown')

                except Exception as e:
                       st.error(f'Error occurred:{e}')

if __name__=='__main__':
    chain=Chain()
    portfolio=Portfolio()
    st.set_page_config(layout='wide',page_title='Cold Email Generator')
    create_streamlit_app(chain,portfolio,clean_text)
