import pandas as pd
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_community.embeddings import HuggingFaceEmbeddings
import uuid

class Portfolio:
    def __init__(self,file_path='app/resource/my_portfolio.csv'):
        self.file_path=file_path
        self.data=pd.read_csv(file_path)
        
      
        documents = []
        for _, row in self.data.iterrows():
            doc = Document(
                page_content=row['Techstack'],
                metadata={'Links': row['Links']}
            )
            documents.append(doc)
        
 
        embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        self.vectorstore = FAISS.from_documents(documents, embeddings)

    def load_portfolio(self):
       
        documents = []
        for _, row in self.data.iterrows():
            doc = Document(
                page_content=row['Techstack'],
                metadata={'Links': row['Links']}
            )
            documents.append(doc)
  
        self.vectorstore.add_documents(documents)
                
    def query_links(self,skills):
        results = self.vectorstore.similarity_search(skills, k=2)
       
        return [doc.metadata for doc in results]