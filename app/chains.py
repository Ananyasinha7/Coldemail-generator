import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv

# Load environment variables from .env file (for local development)
load_dotenv()

class Chain:
    def __init__(self):
        # Try to get API key from environment variable first (local .env)
        api_key = os.getenv("GROQ_API_KEY")
        
        # If not found, try Streamlit secrets (for cloud deployment)
        if not api_key:
            try:
                import streamlit as st
                api_key = st.secrets["GROQ_API_KEY"]
            except:
                raise ValueError("GROQ_API_KEY not found in environment variables or Streamlit secrets")
        
        self.llm=ChatGroq(
            temperature=0,
            groq_api_key=api_key,
            model_name='llama3-70b-8192'
        )

    def extract_jobs(self,cleaned_text):
        prompt_extract=PromptTemplate.from_template(
    """
     ### Scraped Text from website:
     {page_data}
     ### Instruction:
     The scraped text is from the career's page of a website.
     Your job is to extract the job postings and return them in JSON format containing
     following keys: 'role','experience','skills' and 'description'. 
     Only return the valid JSON.
     ### Valid Json (No preamble): 
"""
    )
        chain_extract=prompt_extract | self.llm #getting the prompt and passing it to the llm
        res=chain_extract.invoke(input={'page_data':cleaned_text})
        try:
            json_parser=JsonOutputParser()
            res=json_parser.parse(res.content)

        except OutputParserException:
            raise OutputParserException("Context too big..Unable to parse jobs")
        return res if isinstance(res,list) else [res]

    def write_mail(self,job,links):
        prompt_email=PromptTemplate.from_template(
    """
### JOB DESCRIPTION:
{job_description}

###INSTRUCTIONS:
You are Aarav, a business development executive at TechNexa Solutions. TechNexa specializes in end-to-end software development, offering cutting-edge web, mobile, and cloud solutions using a wide range of modern technologies.
Over the years, we have helped startups and enterprises alike by delivering high-performing applications, scalable cloud infrastructure, and seamless digital transformation strategies across diverse industries.
Your job is to write a cold email to the client regarding the job mentioned above, highlighting how TechNexa’s expertise in their required tech stack can support them in building reliable, scalable, and efficient software products.
Also, based on the client’s technology needs, add the most relevant portfolio links to showcase TechNexa's portfolio:{link_list}
Do not provide a preamble.
Remember you are Aarav, BDE at TechNexa.
### EMAIL (NO PREAMBLE):
"""
)
        chain_email=prompt_email | self.llm
        res=chain_email.invoke({"job_description": str(job),"link_list":links})
        return res.content


if __name__=="__main__":
        print(os.getenv("GROQ_API_KEY"))

