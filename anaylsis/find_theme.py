from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from openai import OpenAI
import os
load_dotenv()


client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key= os.getenv("token"),  
)


def run_query(prompt):
  embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={'device': 'cpu'}
     )
  vector_store = Chroma(persist_directory="../data/vector_store", embedding_function=embeddings)
  retriever = vector_store.as_retriever()
  docs = retriever.invoke(prompt)
  context = "\n".join([doc.page_content for doc in docs])

  response = client.chat.completions.create(
    model="openrouter/cypher-alpha:free",
    messages=[
      {
            "role": "system",
            "content": """"
            You are a smart assistant that reads a customer feedback document and extracts insights for business analysis.

            Your task is to analyze the context and group related phrases and keywords into:
            - 3–5 overarching **themes** (what the feedback is generally about)
            - A list of **drivers** (motivations or reasons behind the user behavior)
            - A list of **painpoints** (problems or frustrations expressed)
            
            Return your result as a Python dictionary in the following **flat format**:
            
            {
                "drivers": ["...", "...", "..."],
                "painpoints": ["...", "...", "..."],
                "theme": ["...", "...", "..."]
            }
            
            Each list should contain concise, human-readable phrases, and must not contain duplicates. Avoid long sentences — focus on clear, actionable terms that can be directly used for further processing.
            
            Now analyze the following document and extract insights in this format.

             """ 
        },
      {
        "role": "user",
        "content": 
        f"""
        Question:
         Documents:
         {context}
         """
      }
      
    ],
    stream = False
  )
  return response.choices[0].message.content

