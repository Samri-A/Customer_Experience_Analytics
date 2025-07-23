from sentence_transformers import SentenceTransformer
from anaylsis.models import embeded_store
from pgvector.django import CosineDistance
from dotenv import load_dotenv
from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
from langchain_chroma import Chroma
from openai import OpenAI
import os
load_dotenv()
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')


class rag():
      def __init__(self , model , app_id ):
        self.client = OpenAI(
          base_url="https://openrouter.ai/api/v1",
          api_key= os.getenv("token"),  
         )
        self.app_id = app_id
        self.model = model
      def embed_document(self , df):
          text_splitter = RecursiveCharacterTextSplitter(
              chunk_size=256,
              chunk_overlap=20,
              length_function=len,
              is_separator_regex=False,
          )
      
      
          chunks = []
          for doc in df["preprocessed"].tolist():
              if isinstance(doc, str) and doc.strip():
                  doc_chunks = text_splitter.split_text(doc)
                  chunks.extend(doc_chunks)
          
          
          embeddings = model.encode(chunks)
          
          for text , embedding in zip( df["preprocessed"], embeddings):
               embeded_store.objects.create(app_id= self.app_id , content = text , embedding = embedding.tolist())

               
      def get_chunks(query , app_id , model):
          embedding = model.encode(query)
          app_review_data = embeded_store.objects.filter(app_id= app_id)
          chunks = app_review_data.annotate(
              distance = CosineDistance("embedding" , embedding).order_by("distance")
          )
          retrived = [chunk.content for chunk in chunks]
          return retrived
      
      def run_query( self , prompt):
          try:
                 chunks = self.get_chunks(self.query , self.app_id , self.model)
                 context = "\n\n".join(chunks)
                 response = self.client.chat.completions.create(
                   model="tngtech/deepseek-r1t2-chimera:free",
                   messages=[
                     {
                           "role": "system",
                           "content": """"
                           You are an App Review Assistant chatbot, designed to analyze and respond to user feedback based on real reviews submitted on the Google Play Store.

                           You have access to a knowledge base composed of actual user-submitted reviews. Your role is to provide accurate, formal, and helpful responses using only the information retrieved from this data.
                           
                           Always maintain a formal tone and incorporate any relevant insights that align with historical complaints, suggestions, or resolutions.
                           
                           If the retrieved documents do not contain sufficient information to answer the query, clearly respond with:
                           “The users review do not contain enough information to accurately respond to your query.”
                           
                           ⚠️ Do not guess, speculate, or generate responses beyond what is supported by the provided review.
                           Always cite the relevant text chunks from the documents used to form your answer.
                               Reviews:
                               {context}
                              """ 
                          
                          
               
                       },
                     {
                       "role": "user",
                       "content": 
                       f"""
                       Question:
                        {prompt}
                        
                       
                        
                        Please provide a complete answer with proper citations from the provided review.
                        """
                     }
                     
                   ]
                 )
                 return response.choices[0].message.content
          except Exception as e:
                return f"Error ocurred{str(e)}"
          

