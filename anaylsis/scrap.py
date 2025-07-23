from google_play_scraper import app , Sort , reviews_all
import numpy as np
import pandas as pd

def playstore_Review_scraping(app_id):
    g_reviews = reviews_all(
        app_id,
        sleep_milliseconds=0, 
        lang='en', 
        country='us',
        sort=Sort.NEWEST, 
    )
    g_df = pd.DataFrame(np.array(g_reviews),columns=['review'])
    g_df2 = g_df.join(pd.DataFrame(g_df.pop('review').tolist()))
    return g_df2