import pandas as pd
from langchain_community.vectorstores import FAISS
import uuid

class Portfolio:
    def __init__(self,file_path='app/resource/my_portfolio.csv'):
        self.file_path=file_path
        self.data=pd.read_csv(file_path)
        self.vectorstore=FAISS.from_documents(self.data['Techstack'], self.data['Links'])

    def load_portfolio(self):
        self.vectorstore.add_documents(self.data['Techstack'], self.data['Links'])

                                   
                

    def query_links(self,skills):
        return self.vectorstore.query(query_texts=skills,n_results=2).get('metadatas',[])