import pandas as pd
mpg=pd.read_csv('data/mpg.csv')

import plotly.express as px
import matplotlib.pyplot as plt
scat=px.scatter(data_frame = mpg, x = 'cty', y = 'hwy', color = 'drv')
#scat.show()

df= mpg.groupby('category', as_index=False).agg(n=('category','count'))
df

bar=px.bar(data_frame=df, x='category', y='n', color='category')
#bar.show()

economics=pd.read_csv('data/economics.csv')
line=px.line(data_frame=economics, x='date', y='psavert')
#line.show()

box=px.box(data_frame=mpg, x='drv', y='hwy', color='drv')
box.show()
