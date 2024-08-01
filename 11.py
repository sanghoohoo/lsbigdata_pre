import json
geo = json.load(open('data/SIG.geojson', encoding = 'UTF-8'))
geo['features'][0]['properties']
geo['features'][0]['geometry']

import pandas as pd
df_pop = pd.read_csv('data/Population_SIG.csv')
df_pop.info()

df_pop['code'] = df_pop['code'].astype(str)

import folium
folium.Map(location = [35.95, 127.7], zoom_start = 8)

#지도를 볼 수 없어 스킵
