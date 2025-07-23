from google_play_scraper import reviews_all , Sort
import pandas as pd
import numpy as np
import spacy 
import os
from dotenv import load_dotenv
from openai import OpenAI
import re
import json
from textblob import TextBlob as tb
from transformers import pipeline

load_dotenv()
nlp = spacy.load("en_core_web_sm")


class data_pipeline():

    def __init__(self , app_id , classifier):
        self.app_id = app_id
        self.client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
         api_key= os.getenv("token"),  
        )
        self.classifier = classifier
        self.result_dict = []

    def playstore_Review_scraping(self):
        try:
            g_reviews = reviews_all(
                self.app_id,
                sleep_milliseconds=0, 
                lang='en', 
                country='us',
                sort=Sort.NEWEST, 
            )
            g_df = pd.DataFrame(np.array(g_reviews),columns=['review'])
            g_df2 = g_df.join(pd.DataFrame(g_df.pop('review').tolist()))
            return g_df2
        except Exception as e:
            print("Error occured" , e)

    def preprocess(self , text):
        if not isinstance(text, str):
            return ""
        doc = nlp(text.lower())
        result = []
        for token in doc:
            if not (token.is_stop or token.is_punct or token.like_num or token.like_email or token.like_url):
                result.append(token.lemma_)
        return " ".join(result)
    
    def get_theme(self , df):
        context = df["preprocessed"].to_list()
        response = self.client.chat.completions.create(
        model="tngtech/deepseek-r1t2-chimera:free",
        messages=[
          {
            "role": "system",
            "content": """"
            You are a smart assistant that reads a customer feedback document and extracts insights for business analysis.

            Your task is to analyze the context and group related phrases and keywords into:
            - 3–5 overarching **themes** (what the feedback is generally about)
            - A list of **drivers** (motivations or reasons behind the user behavior)
            - A list of **painpoints** (problems or frustrations expressed)
            
            Return your result in the following format**:
            
            {
                "drivers": ["...", "...", "..."], "painpoints": ["...", "...", "..."], "theme": ["...", "...", "..."]
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
          
            ])
        
        raw_json = response.choices[0].message.content
        match = re.search(r'{.*}', raw_json, re.DOTALL)
        if match:
            result_dict = json.loads(match.group())
        else:
            raise ValueError("No valid JSON found in LLM response.")
        
        self.result_dict = result_dict

    def classify_theme(self, text):
        candidate_labels = self.result_dict["theme"]
        result = self.classifier(text, candidate_labels)
        return result['labels'][0]

    def get_sentiment_score(self ,text):
        analysis = tb(text)
        return analysis.sentiment.polarity 
    
    def main(self):
        df = self.playstore_Review_scraping()
        df["preprocessed"] = df["content"].apply(self.preprocess)
        df = df[~(df["preprocessed"] == "")]
        df["sentiment"] = df["content"].apply(self.get_sentiment_score)
        df["sentiment"] = df["sentiment"].apply( lambda x: "negative" if x < -0.1 else ("positive" if x > 0.1 else "neutral"))
        self.get_theme(df)
        df["identified_theme"] = df["content"].apply(self.classify_theme)

        return df , self.result_dict["painpoints"] , self.result_dict["drivers"]





        
    
       