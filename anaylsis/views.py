from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
import pandas as pd
import json
from .models import App , embeded_store
from sentence_transformers import SentenceTransformer
from anaylsis.scripts.playstore_data_pipeline import data_pipeline
from transformers import pipeline
from anaylsis.scripts.rag_utils import rag

classifer =pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')



@require_http_methods(['POST'])
@csrf_exempt  
def chat(request):
    try:
        data = json.loads(request.body)
        message , app_id = data.get("message", "app_id")
        rag_pipeline = rag( model , app_id)
        response = rag_pipeline.run_query(message)
        return JsonResponse({'reply': response}, status=201)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

@require_http_methods(["POST"])
@csrf_exempt
def analytics(request):
    try:
        data = json.loads(request.body)
        app_id = data.get('appid')
        analytics = data_pipeline(app_id , classifer)
        if App.objects.filter(app_id = app_id).exists():
            data = App.objects.filter(app_id = app_id)
            painpoints = data.painpoints
            drivers = data.drivers
            df = pd.read_csv(data.csv)
            theme_counts = df["identified_theme"].value_counts()
            theme_values = theme_counts.values.tolist()
            theme_labels = theme_counts.index.tolist()
    
            rating_count = df["score"].value_counts().to_dict()
            rating_labels = list(rating_count.keys())
            rating_values = list(rating_count.values())

            sentiment_trend = df.groupby("year")["sentiment"].value_counts().unstack().fillna(0)
            sentiment_dict = sentiment_trend.to_dict()
            years = sorted(sentiment_trend.index.tolist())

            sentiment_data = {
                "labels": years,
                "datasets": [
                    {
                        "label": sentiment,
                        "data": [sentiment_dict[sentiment].get(year, 0) for year in years]
                    } for sentiment in sentiment_dict
                ]
            }
          
            return JsonResponse({
                "theme_values": theme_values,
                "theme_labels": theme_labels,
                "rating_values": rating_values,
                "rating_labels": rating_labels,
                "sentiment_trend": sentiment_data ,
                 "painpoints" : painpoints ,
                 "drivers" : drivers 
            }, status=201)
    
            
        else:
            df, painpoints, drivers = analytics.main()
            rag_pipe = rag(app_id ,model)
            rag_pipe.embed_document(df)
            
            theme_counts = df["identified_theme"].value_counts()
            theme_values = theme_counts.values.tolist()
            theme_labels = theme_counts.index.tolist()
    
            rating_count = df["score"].value_counts().to_dict()
            rating_labels = list(rating_count.keys())
            rating_values = list(rating_count.values())
    
            df["at"] = pd.to_datetime(df["at"])
            df["year"] = df["at"].dt.year
            sentiment_trend = df.groupby("year")["sentiment"].value_counts().unstack().fillna(0)
            sentiment_dict = sentiment_trend.to_dict()
            years = sorted(sentiment_trend.index.tolist())
            sentiment_data = {
                "labels": years,
                "datasets": [
                    {
                        "label": sentiment,
                        "data": [sentiment_dict[sentiment].get(year, 0) for year in years]
                    } for sentiment in sentiment_dict
                ]
            }
            App.objects.create(app_id , csv = df.to_csv(index=False) )
            
            return JsonResponse({
                "theme_values": theme_values,
                "theme_labels": theme_labels,
                "rating_values": rating_values,
                "rating_labels": rating_labels,
                "sentiment_trend": sentiment_data ,
                 "painpoints" : painpoints ,
                 "drivers" : drivers 
            }, status=201)
       

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
