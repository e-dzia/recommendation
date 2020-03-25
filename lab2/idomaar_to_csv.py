import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn import metrics
from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.decomposition import TruncatedSVD
# from sklearn.pipeline import make_pipeline
# from sklearn.preprocessing import Normalizer
import pickle
import json


course_df = pd.read_csv("datasets/tracks.idomaar", sep="\t", header=None)
course_df = course_df.head(1000000).tail(500000)  # Not all, because it has over 5M songs and it doesn't fit in my RAM
json_str = course_df.to_json(orient='index')
a_json = json.loads(json_str)
rows = [] 

for key, data in a_json.items():
    one_row = {}
    one_row['id'] = data['1']
    
    one_row.update(json.loads(data['3']))
    
    artists = json.loads(data['4'])
    
    for key, value in artists.items():
        if type(value) == list and len(value) > 0:
            artists[key] = value[0]['id']
        else:
            artists[key] = None
    
    one_row.update(artists)
    rows.append(one_row)


df = pd.DataFrame(rows) 

df.to_csv("datasets/tracks_test.csv")